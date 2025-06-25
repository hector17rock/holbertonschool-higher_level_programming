# SQL - Introduction

Welcome to the **SQL Introduction** project! This project covers the foundational concepts of relational databases and SQL operations using MySQL 8.0. You'll learn how to manage databases and perform queries through structured tasks designed to teach key concepts like DDL, DML, subqueries, and SQL functions.

---

## 📚 Resources

Recommended readings and references:

- [What is Database & SQL?](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
- [Install MySQL](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)
- [Basic SQL statements: DDL and DML](https://www3.ntu.edu.sg/home/ehchua/programming/sql/Relational_Database_Design.html)
- [Basic Queries: SQL and Relational Algebra](https://www.geeksforgeeks.org/sql-query-questions-and-answers/)
- [SQL Techniques: Functions](https://dev.mysql.com/doc/refman/8.0/en/functions.html)
- [SQL Techniques: Subqueries](https://dev.mysql.com/doc/refman/8.0/en/subqueries.html)
- [Backtick vs Apostrophe](https://stackoverflow.com/questions/11321491/when-to-use-single-quotes-double-quotes-and-backticks-in-mysql)
- [MySQL Cheat Sheet](https://data-flair.training/blogs/mysql-cheat-sheet/)
- [MySQL 8.0 SQL Syntax Reference](https://dev.mysql.com/doc/refman/8.0/en/sql-syntax.html)

---

## 🎯 Learning Objectives

At the end of this project, you should be able to explain:

- What’s a database and a relational database
- What SQL stands for and what MySQL is
- How to create databases and tables
- The meaning of DDL and DML
- How to use `CREATE`, `ALTER`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- How to use SQL functions and subqueries

---

## ✅ Requirements

- OS: Ubuntu 20.04 LTS
- MySQL Version: 8.0
- Editors allowed: `vi`, `vim`, `emacs`
- All SQL files should:
  - End with a new line
  - Begin with a comment describing the task
  - Include a comment before each query
  - Use **UPPERCASE** for SQL keywords
- A `README.md` file is mandatory
- SQL files are tested using `wc` for length

---

## ⚙️ MySQL Installation & Setup

### On Ubuntu 22.04+

```bash
$ apt update
$ apt install -y mysql-server
$ service mysql start
$ mysql --version
$ mysql -uroot


On Ubuntu 20.04 (old image or sandbox)
$ service mysql start
$ mysql -uroot
# OR
$ cat <script.sql> | mysql -uroot -p

