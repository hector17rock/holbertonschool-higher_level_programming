from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


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


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    products = []
    error = None

    if source == 'json':
        products = load_json_data()
    elif source == 'csv':
        products = load_csv_data()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id:
        try:
            product_id = str(int(product_id))  # Normalize to string for CSV
        except ValueError:
            error = "Invalid ID format"
            return render_template('product_display.html', error=error)

        filtered = [p for p in products if str(p.get('id')) == product_id or
                    str(p['id']) == product_id]
        if not filtered:
            error = "Product not found"
        else:
            products = filtered

    return render_template('product_display.html', products=products,
                           error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
