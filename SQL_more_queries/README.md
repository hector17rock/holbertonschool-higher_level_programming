# SQL - More queries

This directory contains SQL scripts that demonstrate advanced MySQL database operations including user management, database creation, table creation with constraints, relational database design, and complex queries with JOINs and subqueries.

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
- How to use LEFT JOIN, RIGHT JOIN, and INNER JOIN
- How to use aggregate functions like COUNT
- How to use GROUP BY and ORDER BY clauses

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

### 8. Cities of California
**File:** `8-cities_of_california_subquery.sql`
- Script that lists all the cities of California that can be found in the database hbtn_0d_usa
- The states table contains only one record where name = California (but the id can be different)
- Results must be sorted in ascending order by cities.id
- You are not allowed to use the JOIN keyword (must use subquery)
- The database name will be passed as an argument of the mysql command

### 9. Cities by States
**File:** `9-cities_by_state_join.sql`
- Script that lists all cities contained in the database hbtn_0d_usa
- Each record should display: cities.id - cities.name - states.name
- Results must be sorted in ascending order by cities.id
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 10. Genre ID by show
**File:** `10-genre_id_by_show.sql`
- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
- Each record should display: tv_shows.title - tv_show_genres.genre_id
- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 11. Genre ID for all shows
**File:** `11-genre_id_all_shows.sql`
- Script that lists all shows contained in the database hbtn_0d_tvshows
- Each record should display: tv_shows.title - tv_show_genres.genre_id
- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
- If a show doesn't have a genre, display NULL
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 12. No genre
**File:** `12-no_genre.sql`
- Script that lists all shows contained in hbtn_0d_tvshows without a genre linked
- Each record should display: tv_shows.title - tv_show_genres.genre_id
- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 13. Number of shows by genre
**File:** `13-count_shows_by_genre.sql`
- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
- First column must be called genre
- Second column must be called number_of_shows
- Don't display a genre that doesn't have any shows linked
- Results must be sorted in descending order by the number of shows linked
- You can use only one SELECT statement

### 14. My genres
**File:** `14-my_genres.sql`
- Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
- The tv_shows table contains only one record where title = Dexter (but the id can be different)
- Each record should display: tv_genres.name
- Results must be sorted in ascending order by the genre name
- You can use only one SELECT statement

### 15. Only Comedy
**File:** `15-comedy_only.sql`
- Script that lists all Comedy shows in the database hbtn_0d_tvshows
- The tv_genres table contains only one record where name = Comedy (but the id can be different)
- Each record should display: tv_shows.title
- Results must be sorted in ascending order by the show title
- You can use only one SELECT statement

### 16. List shows and genres
**File:** `16-shows_by_genre.sql`
- Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
- If a show doesn't have a genre, display NULL in the genre column
- Each record should display: tv_shows.title - tv_genres.name
- Results must be sorted in ascending order by the show title and genre name
- You can use only one SELECT statement

## Database Structure

### hbtn_0d_usa Database
- **states table**: Contains US states with id (primary key) and name
- **cities table**: Contains cities with id (primary key), state_id (foreign key), and name

### hbtn_0d_tvshows Database
- **tv_shows table**: Contains TV shows with id (primary key) and title
- **tv_genres table**: Contains genres with id (primary key) and name
- **tv_show_genres table**: Junction table linking shows to genres with show_id and genre_id

## Usage Examples

### Basic Script Execution
```bash
# Execute a script on a specific database
cat script_name.sql | mysql -hlocalhost -uroot -p database_name

# Execute a script (when database is created within the script)
cat script_name.sql | mysql -hlocalhost -uroot -p

# Example for creating a user
cat 1-create_user.sql | mysql -hlocalhost -uroot -p

# Example for creating a table in a specific database
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2

# Example for querying the TV shows database
cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

### Testing the Results
```bash
# Check user privileges
cat 0-privileges.sql | mysql -hlocalhost -uroot -p

# Insert test data for states
echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa

# Insert test data for cities
echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose");' | mysql -hlocalhost -uroot -p hbtn_0d_usa

# Query data
echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
```

## Key SQL Concepts Demonstrated

### 1. User Management
- Creating MySQL users with specific privileges
- Using `IF NOT EXISTS` to prevent script failures
- Setting user passwords securely
- Granting different levels of access (ALL PRIVILEGES vs SELECT only)

### 2. Database Design
- Creating databases and tables
- Implementing various constraints (NOT NULL, UNIQUE, DEFAULT)
- Setting up primary keys and foreign keys
- Using AUTO_INCREMENT for unique identifiers

### 3. Data Integrity
- Implementing foreign key constraints for referential integrity
- Preventing null values where required
- Ensuring unique values with UNIQUE constraints
- Setting default values for columns

### 4. Query Techniques
- **Subqueries**: Using nested SELECT statements
- **INNER JOIN**: Linking tables with matching records only
- **LEFT JOIN**: Including all records from left table, even without matches
- **Multiple JOINs**: Connecting three or more tables
- **Aggregate functions**: Using COUNT() to summarize data
- **GROUP BY**: Grouping results for aggregation
- **ORDER BY**: Sorting results by multiple criteria

### 5. Advanced Querying
- Filtering with WHERE clauses
- Handling NULL values in results
- Using column aliases for cleaner output
- Combining multiple conditions in queries

### 6. Best Practices
- Using conditional creation statements (`IF NOT EXISTS`)
- Proper commenting in SQL scripts
- Consistent naming conventions
- Error handling in database operations
- Single SELECT statement optimization

## Common Query Patterns

### Finding Related Data
```sql
-- Using subquery (when JOIN is not allowed)
SELECT column FROM table1 WHERE id = (SELECT id FROM table2 WHERE condition);

-- Using INNER JOIN (only matching records)
SELECT t1.column, t2.column FROM table1 t1
JOIN table2 t2 ON t1.id = t2.foreign_id;

-- Using LEFT JOIN (include all from left table)
SELECT t1.column, t2.column FROM table1 t1
LEFT JOIN table2 t2 ON t1.id = t2.foreign_id;
```

### Aggregating Data
```sql
-- Count with grouping
SELECT category, COUNT(*) as count FROM table
GROUP BY category ORDER BY count DESC;
```

### Filtering Results
```sql
-- Include only records with relationships
WHERE foreign_key IS NOT NULL

-- Include only records without relationships
WHERE foreign_key IS NULL
```

## Author
Holberton School Project - SQL More Queries Module
