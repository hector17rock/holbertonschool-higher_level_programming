# Holberton School - Higher Level Programming

This repository contains projects and exercises for the Higher Level Programming track at Holberton School. The curriculum covers advanced programming concepts in Python, SQL, and API development, progressing from basic syntax to complex software engineering principles.

## Repository Overview

**Repository Name:** `holbertonschool-higher_level_programming`  
**School:** Holberton School  
**Track:** Higher Level Programming  
**Languages:** Python, SQL, HTML, CSS, JavaScript  
**Total Projects:** 18 modules  
**Total Files:** 200+ scripts and programs

## Learning Objectives

By completing this curriculum, students will master:
- **Python Programming**: From basics to advanced OOP concepts
- **Database Management**: SQL queries, database design, and optimization
- **API Development**: RESTful services and HTTP protocols
- **Software Engineering**: Testing, documentation, and best practices
- **Data Structures & Algorithms**: Implementation and optimization
- **Web Technologies**: Backend development fundamentals

## Project Structure

### 🐍 Python Fundamentals

#### [`python-hello_world`](./python-hello_world/)
**Files:** 9 | **Focus:** Python basics and syntax
- Introduction to Python programming
- Variables, strings, and basic operations
- Print statements and string formatting
- Basic debugging and error handling

#### [`python-if_else_loops_functions`](./python-if_else_loops_functions/)
**Files:** 16 | **Focus:** Control structures and functions
- Conditional statements (if, elif, else)
- Loops (for, while) and iteration
- Function definition and calling
- Scope and parameter passing

#### [`python-import_modules`](./python-import_modules/)
**Files:** 9 | **Focus:** Code organization and modularity
- Importing modules and packages
- Creating custom modules
- Understanding Python path and namespaces
- Command-line arguments handling

### 🏗️ Data Structures & Algorithms

#### [`python-data_structures`](./python-data_structures/)
**Files:** 14 | **Focus:** Lists, tuples, and basic algorithms
- List manipulation and comprehensions
- Tuple operations and immutability
- String methods and character manipulation
- Basic sorting and searching algorithms

#### [`python-more_data_structures`](./python-more_data_structures/)
**Files:** 16 | **Focus:** Advanced data structures
- Dictionaries and hash tables
- Sets and set operations
- Lambda functions and functional programming
- Map, filter, and reduce operations

### 🛡️ Error Handling & Testing

#### [`python-exceptions`](./python-exceptions/)
**Files:** 9 | **Focus:** Exception handling and debugging
- Try-except blocks and error catching
- Raising custom exceptions
- Finally blocks and cleanup
- Debugging techniques and best practices

#### [`python-test_driven_development`](./python-test_driven_development/)
**Files:** 9 | **Focus:** Testing methodologies
- Unit testing with doctest and unittest
- Test-driven development (TDD) principles
- Writing comprehensive test cases
- Code documentation and examples

### 🎯 Object-Oriented Programming

#### [`python-classes`](./python-classes/)
**Files:** 8 | **Focus:** Basic OOP concepts
- Class definition and instantiation
- Attributes and methods
- Constructors and destructors
- Instance vs class variables

#### [`python-more_classes`](./python-more_classes/)
**Files:** 11 | **Focus:** Advanced OOP features
- Static methods and class methods
- Properties and getters/setters
- String representation methods
- Class documentation and introspection

#### [`python-inheritance`](./python-inheritance/)
**Files:** 15 | **Focus:** Inheritance and polymorphism
- Single and multiple inheritance
- Method overriding and super()
- Abstract classes and interfaces
- Method resolution order (MRO)

#### [`python-abc`](./python-abc/)
**Files:** 7 | **Focus:** Abstract base classes
- ABC module and abstract methods
- Interface design patterns
- Enforcing method implementation
- Advanced inheritance patterns

### 💾 File Operations & Serialization

#### [`python-input_output`](./python-input_output/)
**Files:** 17 | **Focus:** File handling and I/O operations
- Reading and writing files
- File modes and context managers
- JSON serialization and deserialization
- CSV and data format handling

#### [`python-serialization`](./python-serialization/)
**Files:** 5 | **Focus:** Data persistence
- Pickle for Python object serialization
- XML and JSON data formats
- Custom serialization methods
- Data validation and conversion

### 🗄️ Database Management

#### [`SQL_introduction`](./SQL_introduction/)
**Files:** 22 | **Focus:** SQL fundamentals
- Database creation and management
- Basic queries (SELECT, INSERT, UPDATE, DELETE)
- Data types and table design
- Filtering and sorting data

#### [`SQL_more_queries`](./SQL_more_queries/)
**Files:** 19 | **Focus:** Advanced SQL operations
- Complex joins and subqueries
- User management and privileges
- Foreign keys and relationships
- Database optimization techniques

### 🌐 Web Development & APIs

#### [`restful-api`](./restful-api/)
**Files:** 8 | **Focus:** API development
- RESTful service design
- HTTP methods and status codes
- JSON data handling
- API testing and documentation

## Technical Requirements

### General Requirements
- **Editors:** vi, vim, emacs
- **Operating System:** Ubuntu 20.04 LTS
- **Python Version:** 3.8.x
- **MySQL Version:** 8.0.x
- **Code Style:** PEP 8 compliant
- **Documentation:** All functions, classes, and modules must be documented

### Python Specifications
- All files must be executable
- First line: `#!/usr/bin/python3`
- All files must end with a new line
- Code must be PEP 8 compliant (pycodestyle)
- All modules, classes, and functions must have documentation
- Documentation must be meaningful sentences explaining the purpose

### SQL Specifications
- All files executed on Ubuntu 20.04 LTS using MySQL 8.0
- All SQL keywords must be in uppercase
- All files must start with a comment describing the task
- All files must end with a new line

## Key Learning Outcomes

### Programming Fundamentals
- **Syntax Mastery**: Complete understanding of Python syntax and idioms
- **Problem Solving**: Algorithmic thinking and solution design
- **Code Quality**: Writing clean, readable, and maintainable code
- **Debugging**: Systematic approach to finding and fixing bugs

### Software Engineering
- **Modular Design**: Breaking complex problems into smaller components
- **Testing**: Comprehensive testing strategies and methodologies
- **Documentation**: Clear and comprehensive code documentation
- **Version Control**: Git workflow and collaboration practices

### Database Management
- **Database Design**: Normalized database schemas and relationships
- **Query Optimization**: Efficient SQL queries and performance tuning
- **Data Integrity**: Constraints, transactions, and data validation
- **Security**: User management and access control

### Web Development
- **API Design**: RESTful service architecture and best practices
- **HTTP Protocol**: Understanding web communication protocols
- **Data Formats**: JSON, XML, and data serialization
- **Backend Development**: Server-side programming fundamentals

## Project Highlights

### 🏆 Notable Implementations

1. **Advanced Calculator** (python-classes): Object-oriented calculator with multiple operations
2. **File Manager** (python-input_output): Comprehensive file handling system
3. **Database Schema** (SQL_more_queries): Complex relational database design
4. **RESTful API** (restful-api): Complete API implementation with authentication
5. **Testing Framework** (python-test_driven_development): Custom testing utilities

### 📈 Skill Progression

**Beginner → Intermediate → Advanced**
- Basic syntax → Complex algorithms → System design
- Simple scripts → Object-oriented programs → Full applications
- Single files → Modular projects → Distributed systems
- Manual testing → Automated testing → CI/CD integration

## Usage Examples

### Running Python Scripts
```bash
# Make script executable
chmod +x script.py

# Run with Python interpreter
./script.py
# or
python3 script.py
```

### Executing SQL Scripts
```bash
# Execute SQL script on database
cat script.sql | mysql -hlocalhost -uroot -p database_name

# Import database dump
mysql -hlocalhost -uroot -p < database_dump.sql
```

### Testing Code
```bash
# Run Python doctests
python3 -m doctest -v file.py

# Run unittest
python3 -m unittest test_file.py

# Check code style
pycodestyle file.py
```

## Best Practices Demonstrated

### Code Quality
- **PEP 8 Compliance**: Consistent code formatting and style
- **Meaningful Names**: Descriptive variable and function names
- **Documentation**: Comprehensive docstrings and comments
- **Error Handling**: Robust exception handling and validation

### Software Engineering
- **Modular Design**: Separation of concerns and single responsibility
- **DRY Principle**: Don't Repeat Yourself - code reusability
- **SOLID Principles**: Object-oriented design principles
- **Testing**: Unit tests and integration tests

### Database Design
- **Normalization**: Eliminating data redundancy
- **Indexing**: Optimizing query performance
- **Constraints**: Ensuring data integrity
- **Security**: Access control and user management

## Resources and References

### Documentation
- [Python Official Documentation](https://docs.python.org/3/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [SQL Standards](https://www.iso.org/standard/63555.html)

### Tools and Testing
- **pycodestyle**: Python code style checker
- **doctest**: Documentation testing framework
- **unittest**: Unit testing framework
- **MySQL Workbench**: Database design and management

### Learning Path
1. **Foundations**: Basic syntax and programming concepts
2. **Data Structures**: Understanding data organization
3. **OOP**: Object-oriented programming principles
4. **Databases**: SQL and database management
5. **APIs**: Web services and backend development
6. **Testing**: Quality assurance and debugging

## Contributing

This repository represents academic work completed as part of the Holberton School curriculum. Each project follows specific requirements and learning objectives designed to build comprehensive programming skills.

### Project Structure
- Each directory contains a specific module with related exercises
- Files are numbered to indicate progression and difficulty
- README files in each directory provide detailed project information
- All code follows school coding standards and style guides

## Author

**Holberton School Student**  
**Track:** Higher Level Programming  
**Cohort:** [Year/Cohort Information]  
**Focus:** Full-Stack Software Development

---

*This repository demonstrates the comprehensive curriculum of Holberton School's Higher Level Programming track, showcasing progression from basic programming concepts to advanced software engineering principles.*
