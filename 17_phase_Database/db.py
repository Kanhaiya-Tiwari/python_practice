# SQLite
# SQLite is a lightweight, file-based database.
# No separate database server is required.

import sqlite3

conn = sqlite3.connect("company.db")

print("Connected Successfully")

# PostgreSQL psycopg2 is a popular PostgreSQL database adapter for Python. It allows you to connect to a PostgreSQL database and perform various operations such as querying, inserting, updating, and deleting data.
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="company",
    user="postgres",
    password="password"
)

print("Connected")

cursor = conn.cursor()

# CRUD Operations

# Create
cursor.execute(
    "INSERT INTO employee(name) VALUES (%s)",
    ("Kanha",)
)
conn.commit()

# Read
cursor.execute("SELECT * FROM employee")

rows = cursor.fetchall()

print(rows)

# Update
cursor.execute(
    "UPDATE employee SET name=%s WHERE id=%s",
    ("Rahul",1)
)
conn.commit()

# Delete
cursor.execute(
    "DELETE FROM employee WHERE id=%s",
    (1,)
)
conn.commit()