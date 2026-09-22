# Phase 17 — Database Concepts

This phase introduces database fundamentals, SQL operations, and how Python interacts with databases. It covers relational databases, CRUD operations, joins, and transaction handling.

## Topics

- Relational databases
- SQL basics
- CRUD operations
- Primary and foreign keys
- Joins and normalization
- Indexing and performance
- Python database connectivity
- Transactions and error handling

## Key Concepts

- Databases store structured data efficiently.
- SQL provides a standard way to query and manipulate data.
- Joins combine related data across tables.
- Transactions keep data consistent and reliable.

## Useful Tools

- SQLite
- MySQL
- PostgreSQL
- SQLAlchemy
- psycopg2 / mysql-connector

## Example

```python
import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
conn.commit()
conn.close()
```

## Best Practices

- Normalize your schema
- Use indexes on frequently queried columns
- Handle transactions carefully
- Validate input before inserting data
- Close database connections properly

## Resources

- SQLite documentation
- SQL tutorial
- Python DB API
