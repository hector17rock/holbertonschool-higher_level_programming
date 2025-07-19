from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- Data Loaders ---


def load_json_data():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception:
        return []


def load_csv_data():
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception:
        return []


def load_sql_data(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        if product_id:
            cursor.execute(
                'SELECT id, name, category, price FROM Products WHERE id = ?',
                (product_id,))
            row = cursor.fetchone()
            if row:
                data = [dict(id=row[0], name=row[1], category=row[2],
                             price=row[3])]
            else:
                data = []
        else:
            cursor.execute('SELECT id, name, category, price FROM Products')
            rows = cursor.fetchall()
            data = [dict(id=r[0], name=r[1], category=r[2], price=r[3])
                    for r in rows]

        conn.close()
        return data

    except sqlite3.Error:
        return None

# --- Route ---


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = []
    error = None

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            error = "Invalid ID format"
            return render_template('product_display.html', error=error)

    if source == 'json':
        data = load_json_data()
        if product_id:
            data = [p for p in data if p['id'] == product_id]
    elif source == 'csv':
        data = load_csv_data()
        if product_id:
            data = [p for p in data if int(p['id']) == product_id]
    elif source == 'sql':
        data = load_sql_data(product_id)
        if data is None:
            error = "Database error occurred"
        elif not data:
            error = "Product not found"
    else:
        error = "Wrong source"

    return render_template('product_display.html', products=data, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
