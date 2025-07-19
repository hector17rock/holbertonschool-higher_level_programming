# Python Server-Side Rendering

A comprehensive collection of Flask applications demonstrating server-side rendering techniques using Jinja2 templating, data integration from multiple sources (JSON, CSV, SQLite), and dynamic web page generation.

## 📚 Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Tasks Description](#tasks-description)
4. [Installation & Setup](#installation--setup)
5. [Usage](#usage)
6. [Data Sources](#data-sources)
7. [Templates](#templates)
8. [API Endpoints](#api-endpoints)
9. [Testing](#testing)
10. [Features](#features)
11. [Author](#author)

## 🎯 Overview

This repository contains a progressive series of Python Flask applications that demonstrate:
- Basic templating with Jinja2
- Dynamic content rendering
- Multiple data source integration (JSON, CSV, SQLite)
- RESTful API design
- Error handling and validation
- Reusable template components

## 📁 Project Structure

```
python-server_side_rendering/
├── README.md
├── task_00_intro.py        # Simple templating system
├── task_01_jinja.py        # Basic Flask app with Jinja templates
├── task_02_logic.py        # Flask app with JSON data integration
├── task_03_files.py        # Flask app with JSON/CSV data sources
├── task_04_db.py          # Flask app with SQLite database
├── main.py                # Example usage demonstrations
├── create_db.py           # Database initialization script
├── test_error_handling.py # Error handling tests
├── items.json             # Sample items data
├── products.json          # Sample products data (JSON format)
├── products.csv           # Sample products data (CSV format)
├── template.txt           # Template file for task_00
└── templates/
    ├── index.html         # Home page template
    ├── about.html         # About page template
    ├── contact.html       # Contact page template
    ├── header.html        # Reusable header component
    ├── footer.html        # Reusable footer component
    ├── items.html         # Items display template
    └── product_display.html # Products display template
```

## 📋 Tasks Description

### Task 0: Simple Templating System (`task_00_intro.py`)
- **Purpose**: Basic template processing with placeholder replacement
- **Features**:
  - Template processing with `{name}`, `{event_title}`, `{event_date}`, `{event_location}` placeholders
  - Error handling for invalid inputs
  - Missing data handling (replaces with "N/A")
  - Sequential output file generation
- **Usage**:
  ```python
  from task_00_intro import generate_invitations
  generate_invitations(template_content, attendees)
  ```

### Task 1: Basic Flask with Jinja (`task_01_jinja.py`)
- **Purpose**: Introduction to Flask and Jinja2 templating
- **Features**:
  - Three routes: `/` (home), `/about`, `/contact`
  - Reusable header and footer components
  - Navigation between pages
  - Static content rendering
- **Routes**:
  - `GET /` → Home page
  - `GET /about` → About page
  - `GET /contact` → Contact page

### Task 2: Logic and Data Integration (`task_02_logic.py`)
- **Purpose**: Dynamic content from JSON data
- **Features**:
  - JSON file reading and parsing
  - Conditional rendering
  - Loop iteration in templates
  - Error handling for missing files
- **Routes**:
  - `GET /items` → Display items from `items.json`

### Task 3: Multiple File Sources (`task_03_files.py`)
- **Purpose**: Data integration from multiple sources
- **Features**:
  - JSON and CSV data source support
  - Query parameter-based source selection
  - Product filtering by ID
  - Comprehensive error handling
- **Routes**:
  - `GET /products?source=json` → Products from JSON
  - `GET /products?source=csv` → Products from CSV
  - `GET /products?source=json&id=1` → Specific product

### Task 4: Database Integration (`task_04_db.py`)
- **Purpose**: SQLite database integration
- **Features**:
  - SQLite database connectivity
  - Support for JSON, CSV, and SQL data sources
  - Database error handling
  - Product filtering and querying
- **Routes**:
  - `GET /products?source=sql` → Products from database
  - `GET /products?source=sql&id=1` → Specific product from DB

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd python-server_side_rendering
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install Flask
   ```

4. **Initialize database (for task_04)**
   ```bash
   python3 create_db.py
   ```

## 📖 Usage

### Running Individual Tasks

```bash
# Task 0: Template generation
python3 main.py

# Task 1: Basic Flask app
python3 task_01_jinja.py
# Visit: http://127.0.0.1:5000

# Task 2: Items from JSON
python3 task_02_logic.py
# Visit: http://127.0.0.1:5000/items

# Task 3: Multiple file sources
python3 task_03_files.py
# Visit: http://127.0.0.1:5000/products?source=json

# Task 4: Database integration
python3 task_04_db.py
# Visit: http://127.0.0.1:5000/products?source=sql
```

### Example URLs

**Task 1 Navigation:**
- `http://127.0.0.1:5000/` - Home page
- `http://127.0.0.1:5000/about` - About page
- `http://127.0.0.1:5000/contact` - Contact page

**Task 2 Items:**
- `http://127.0.0.1:5000/items` - Display all items

**Task 3 & 4 Products:**
- `http://127.0.0.1:5000/products?source=json` - All products from JSON
- `http://127.0.0.1:5000/products?source=csv` - All products from CSV
- `http://127.0.0.1:5000/products?source=sql` - All products from database
- `http://127.0.0.1:5000/products?source=json&id=1` - Product ID 1 from JSON
- `http://127.0.0.1:5000/products?source=sql&id=2` - Product ID 2 from database

## 💾 Data Sources

### items.json
```json
{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
```

### products.json
```json
[
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]
```

### products.csv
```csv
id,name,category,price
1,Laptop,Electronics,799.99
2,Coffee Mug,Home Goods,15.99
```

### SQLite Database
- **Table**: `Products`
- **Schema**: `id INTEGER, name TEXT, category TEXT, price REAL`

## 🎨 Templates

### Reusable Components
- **header.html**: Navigation bar with links to all pages
- **footer.html**: Copyright information and site footer

### Page Templates
- **index.html**: Welcome page with site introduction
- **about.html**: About us page with company information
- **contact.html**: Contact information page
- **items.html**: Dynamic list display with conditional rendering
- **product_display.html**: Table-based product display with error handling

### Template Features
- Jinja2 template inheritance
- Conditional rendering (`{% if %}`, `{% else %}`)
- Loop iteration (`{% for %}`)
- Template inclusion (`{% include %}`)
- Variable substitution (`{{ variable }}`)

## 🌐 API Endpoints

| Endpoint | Method | Parameters | Description |
|----------|--------|------------|-------------|
| `/` | GET | - | Home page |
| `/about` | GET | - | About page |
| `/contact` | GET | - | Contact page |
| `/items` | GET | - | Display items from JSON |
| `/products` | GET | `source` (json\|csv\|sql) | Display products from specified source |
| `/products` | GET | `source`, `id` | Display specific product by ID |

### Query Parameters
- **source**: Data source selection (`json`, `csv`, `sql`)
- **id**: Product ID for filtering (integer)

### Error Responses
- "Wrong source" - Invalid source parameter
- "Invalid ID format" - Non-numeric ID parameter
- "Product not found" - ID not found in data source
- "Database error occurred" - SQLite connection/query error

## 🧪 Testing

### Manual Testing
```bash
# Test error handling
python3 test_error_handling.py

# Test template generation
python3 main.py
```

### Testing Scenarios
1. **Valid inputs**: Normal operation with correct data
2. **Invalid source**: Test with wrong source parameters
3. **Missing data**: Test with non-existent product IDs
4. **Database errors**: Test with missing database file
5. **File errors**: Test with missing JSON/CSV files

## ✨ Features

### Core Functionality
- ✅ Server-side rendering with Jinja2
- ✅ Multiple data source support (JSON, CSV, SQLite)
- ✅ RESTful API design
- ✅ Dynamic content generation
- ✅ Template inheritance and reusability

### Error Handling
- ✅ Input validation
- ✅ File not found handling
- ✅ Database connection error handling
- ✅ Invalid parameter handling
- ✅ Graceful error messages

### Code Quality
- ✅ PEP 8 compliant code style
- ✅ Comprehensive documentation
- ✅ Modular design
- ✅ Separation of concerns

## 📚 Learning Objectives

This project demonstrates:
1. **Flask Framework**: Web application development
2. **Jinja2 Templating**: Dynamic HTML generation
3. **Data Integration**: Working with multiple data formats
4. **Database Operations**: SQLite integration
5. **Error Handling**: Robust application design
6. **RESTful APIs**: HTTP request handling
7. **Template Design**: Reusable component architecture

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:
1. Follow PEP 8 style conventions
2. Add comprehensive docstrings
3. Include error handling
4. Test your changes thoroughly

## 📄 License

This project is part of educational coursework and is intended for learning purposes.

## 👨‍💻 Author

**Hector**  
Maintainer and Primary Developer

---

*This project is part of the Holberton School Higher Level Programming curriculum, focusing on server-side rendering techniques with Python and Flask.*
