# Phase 17 — Database Interview Questions

1. Q: What is a database in Python applications?
   A: A database is a structured storage system used to save and manage data. In Python, we commonly connect to databases like SQLite, MySQL, and PostgreSQL using modules such as sqlite3 or ORM libraries like SQLAlchemy.

2. Q: Why is Python used with databases?
   A: Python is easy to learn, supports database drivers, and can automate data storage, retrieval, and processing. It is widely used for backend logic, APIs, and data-driven applications.

3. Q: What is SQLite?
   A: SQLite is a lightweight database engine built into Python through the sqlite3 module. It is ideal for small applications, testing, and local storage.

4. Q: How do you connect Python to SQLite?
   A: Use the sqlite3.connect() function and create a cursor object to execute SQL statements.

5. Q: What is CRUD?
   A: CRUD stands for Create, Read, Update, and Delete. These are the four basic database operations used in most applications.

6. Q: What is a cursor in Python database programming?
   A: A cursor is an object used to execute SQL queries and fetch results from the database.

7. Q: What is the purpose of execute() in sqlite3?
   A: execute() runs a single SQL statement such as SELECT, INSERT, UPDATE, or DELETE.

8. Q: What is executemany()?
   A: executemany() executes the same SQL statement multiple times with different values, which is useful for bulk inserts.

9. Q: What is a primary key?
   A: A primary key is a unique identifier for each row in a table. It ensures each record is unique and helps in indexing.

10. Q: What is a foreign key?
    A: A foreign key is a field in one table that refers to the primary key in another table. It is used to maintain relationships between tables.

11. Q: What is a join in SQL?
    A: A join combines rows from two or more tables based on a related column. Common joins are INNER JOIN, LEFT JOIN, and RIGHT JOIN.

12. Q: How do you insert data into a database using Python?
    A: Use a connection object, create a cursor, write an INSERT SQL query, and then call commit() to save the changes.

13. Q: What is the commit() method used for?
    A: commit() saves all pending changes to the database permanently.

14. Q: What is rollback() in database operations?
    A: rollback() reverts the last transaction if an error occurs. It helps maintain data integrity.

15. Q: What is SQL injection?
    A: SQL injection is an attack where malicious SQL is inserted into queries. It can be prevented by using parameterized queries instead of direct string concatenation.

16. Q: Why should Python database queries use parameters?
    A: Parameterized queries protect against SQL injection, improve readability, and reduce syntax errors.

17. Q: What is the difference between fetchone() and fetchall()?
    A: fetchone() returns one row from a query result, while fetchall() returns all rows.

18. Q: What is a transaction in database programming?
    A: A transaction is a sequence of operations performed as a single unit. It must either fully succeed or fully fail.

19. Q: What is SQLAlchemy?
    A: SQLAlchemy is a Python SQL toolkit and Object Relational Mapper (ORM) that makes database interaction easier and more Pythonic.

20. Q: How do you handle database errors in Python?
    A: Use try/except blocks around database operations and log the exception. It is also good to use rollback() when an error occurs to avoid partial updates.

End of interview questions.
