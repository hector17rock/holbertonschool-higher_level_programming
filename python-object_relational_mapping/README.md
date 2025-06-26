# Python Object Relational Mapping

This project explores the integration of Python with relational databases using two different approaches:

1. **MySQLdb**: A low-level interface to MySQL databases, allowing direct SQL query execution.
2. **SQLAlchemy**: A high-level Object Relational Mapper (ORM) which abstracts database interactions via Python objects.

## Directory Structure

- **0-select_states.py**: Lists all states from a MySQL database.
- **1-filter_states.py**: Lists states starting with 'N'.
- **2-my_filter_states.py**: Filters states by user-provided name (vulnerable to SQL injection).
- **3-my_safe_filter_states.py**: Safe filtering using parameterized queries.
- **4-cities_by_state.py**: Lists all cities with corresponding state names.
- **5-filter_cities.py**: Lists all cities of a given state.
- **7-model_state_fetch_all.py**: Lists all states using SQLAlchemy ORM.
- **8-model_state_fetch_first.py**: Fetches the first state using SQLAlchemy ORM.
- **9-model_state_filter_a.py**: Lists states containing letter 'a'.
- **10-model_state_my_get.py**: Fetches state by name.
- **11-model_state_insert.py**: Adds a new state "Louisiana".
- **12-model_state_update_id_2.py**: Updates the name of a state where id=2.
- **13-model_state_delete_a.py**: Deletes states containing the letter 'a'.
- **14-model_city_fetch_by_state.py**: Lists cities with corresponding state names using SQLAlchemy.
- **model_city.py**: SQLAlchemy model definition for `City`.
- **model_state.py**: SQLAlchemy model definition for `State`.

## Two Approaches Compared

### MySQLdb (Direct SQL)

```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", 
                       passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

### SQLAlchemy (ORM)

```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    "root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
```

## Learning Objectives

- Connect to a MySQL database from a Python script.
- Perform SELECT and INSERT operations in a MySQL table from a Python script.
- Understand the principles of ORM and SQLAlchemy.
- Map a Python Class to a MySQL table using SQLAlchemy.
- Learn about SQL injection vulnerabilities and how to prevent them.

## Project Progression

### Part 1: MySQLdb (Scripts 0-5)
These scripts demonstrate direct SQL query execution:
- Basic database connection and querying
- String formatting in SQL queries (vulnerable to injection)
- Parameterized queries (safe from injection)
- JOIN operations between tables

### Part 2: SQLAlchemy ORM (Scripts 7-14)
These scripts showcase object-relational mapping:
- Model definitions (`model_state.py`, `model_city.py`)
- CRUD operations using ORM methods
- Relationships between objects
- Advanced querying with filters

## Security Note

⚠️ **Script 2** (`2-my_filter_states.py`) is intentionally vulnerable to SQL injection to demonstrate the security risks of string formatting in SQL queries.

✅ **Script 3** (`3-my_safe_filter_states.py`) shows the secure approach using parameterized queries.

## Usage

Ensure you have MySQLdb and SQLAlchemy installed. Run any script using:

```bash
./<script_name>.py <mysql_username> <mysql_password> <database_name> [additional arguments]
```

Each script file is executable and should be run directly from the terminal.

### Example:
```bash
# List all states
./0-select_states.py root password hbtn_0e_0_usa

# Filter states by name
./3-my_safe_filter_states.py root password hbtn_0e_0_usa Texas

# List all states using ORM
./7-model_state_fetch_all.py root password hbtn_0e_6_usa
```

## Requirements

- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x

## License

Distributed under the MIT License. See `LICENSE` for more information.
