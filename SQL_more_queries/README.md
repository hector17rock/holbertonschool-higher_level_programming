# SQL - More queries

This directory contains SQL scripts that demonstrate advanced MySQL database operations including user management, database creation, table creation with constraints, and relational database design.

## Repository Information
- **GitHub repository:** holbertonschool-higher_level_programming
- **Directory:** SQL_more_queries

## Learning Objectives

By completing these exercises, you will learn:
- How to create a new MySQL user
- How to manage privileges for a user or role
- What's a PRIMARY KEY and FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before (i.e. syntax above)
- All files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE...)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## Files Description

### 0. My privileges!
**File:** `0-privileges.sql`
- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server

### 1. Root user
**File:** `1-create_user.sql`
- Script that creates the MySQL server user user_0d_1
- user_0d_1 should have all privileges on your MySQL server
- The user_0d_1 password should be set to user_0d_1_pwd
- If the user user_0d_1 already exists, your script should not fail

### 2. Read user
**File:** `2-create_read_user.sql`
- Script that creates the database hbtn_0d_2 and the user user_0d_2
- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
- The user_0d_2 password should be set to user_0d_2_pwd
- If the database hbtn_0d_2 already exists, your script should not fail
- If the user user_0d_2 already exists, your script should not fail

### 3. Always a name
**File:** `3-force_name.sql`
- Script that creates the table force_name on your MySQL server
- **Table description:**
  - id INT
  - name VARCHAR(256) can't be null
- The database name will be passed as an argument of the mysql command
- If the table force_name already exists, your script should not fail

### 4. ID can't be null
**File:** `4-never_empty.sql`
- Script that creates the table id_not_null on your MySQL server
- **Table description:**
  - id INT with the default value 1
  - name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table id_not_null already exists, your script should not fail

### 5. Unique ID
**File:** `5-unique_id.sql`
- Script that creates the table unique_id on your MySQL server
- **Table description:**
  - id INT with the default value 1 and must be unique
  - name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table unique_id already exists, your script should not fail

### 6. States table
**File:** `6-states.sql`
- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server
- **States table description:**
  - id INT unique, auto generated, can't be null and is a primary key
  - name VARCHAR(256) can't be null
- If the database hbtn_0d_usa already exists, your script should not fail
- If the table states already exists, your script should not fail

### 7. Cities table
**File:** `7-cities.sql`
- Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
- **Cities table description:**
  - id INT unique, auto generated, can't be null and is a primary key
  - state_id INT, can't be null and must be a FOREIGN KEY that references to id of the states table
  - name VARCHAR(256) can't be null
- If the database hbtn_0d_usa already exists, your script should not fail
- If the table cities already exists, your script should not fail

## Usage Examples

### Running the scripts
```bash
# Execute a script on a specific database
cat script_name.sql | mysql -hlocalhost -uroot -p database_name

# Execute a script (when database is created within the script)
cat script_name.sql | mysql -hlocalhost -uroot -p

# Example for creating a user
cat 1-create_user.sql | mysql -hlocalhost -uroot -p

# Example for creating a table in a specific database
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```

### Testing the results
```bash
# Check user privileges
cat 0-privileges.sql | mysql -hlocalhost -uroot -p

# Insert test data
echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa

# Query data
echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
```

## Key Concepts Demonstrated

### 1. User Management
- Creating MySQL users with specific privileges
- Using `IF NOT EXISTS` to prevent script failures
- Setting user passwords securely

### 2. Database Design
- Creating databases and tables
- Implementing various constraints (NOT NULL, UNIQUE, DEFAULT)
- Setting up primary keys and foreign keys

### 3. Data Integrity
- Using AUTO_INCREMENT for unique identifiers
- Implementing foreign key constraints for referential integrity
- Preventing null values where required

### 4. Best Practices
- Using conditional creation statements (`IF NOT EXISTS`)
- Proper commenting in SQL scripts
- Consistent naming conventions
- Error handling in database operations

## Author
Holberton School Project - SQL More Queries Module
