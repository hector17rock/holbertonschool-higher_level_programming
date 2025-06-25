# SQL Introduction

This project introduces the fundamentals of SQL and MySQL. You'll learn how to manipulate databases and tables, perform queries, and manage data using SQL commands. The project is designed to run on Ubuntu 20.04 with MySQL 8.0 and all scripts must follow specified formatting and syntax guidelines.

---

## 📚 Resources

**Read or Watch:**
- [What is Database & SQL?](https://www.digitalocean.com/community/tutorials/what-is-database-sql)
- [Install MySQL (MySQL Server)](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)
- [A Basic MySQL Tutorial](https://www.w3schools.com/sql/)
- [Basic SQL statements: DDL and DML](https://www.sqltutorial.org/sql-ddl/)
- [Basic queries: SQL and RA](https://en.wikipedia.org/wiki/Relational_algebra)
- [SQL technique: functions](https://dev.mysql.com/doc/refman/8.0/en/functions.html)
- [SQL technique: subqueries](https://dev.mysql.com/doc/refman/8.0/en/subqueries.html)
- [Backtick vs Apostrophe](https://stackoverflow.com/questions/11321491/when-to-use-single-quotes-double-quotes-and-backticks-in-mysql)
- [MySQL Cheat Sheet](https://devhints.io/mysql)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain:
- What a database is
- What a relational database is
- What SQL stands for
- What MySQL is
- How to create a database in MySQL
- The meaning of DDL and DML
- How to use `CREATE`, `ALTER`, `SELECT`, `INSERT`, `UPDATE`, and `DELETE`
- How to write subqueries
- How to use MySQL functions

---

## ✅ Requirements

### General
- All scripts must be executed on **Ubuntu 20.04 LTS** using **MySQL 8.0 (version 8.0.25)**
- Allowed editors: `vi`, `vim`, `emacs`
- All SQL files must end with a new line and begin with a comment describing the task
- SQL keywords must be written in **UPPERCASE**
- SQL queries must include a comment before them
- File length will be tested using `wc`

---

## ⚙️ Setup Instructions

### On Ubuntu 22.04:
```bash
apt update
apt install -y mysql-server
mysql --version  # Verify version
service mysql start
mysql -uroot     # Connect



