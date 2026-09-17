# Phase 1: Introduction to Python

## Overview
This phase covers the fundamental concepts of Python programming, including variables, data types, basic operations, and getting started with Python.

## Learning Objectives
- Understand variables and how to declare them
- Learn basic data types (int, float, str, bool)
- Perform basic arithmetic operations
- Use print() and input() functions
- Understand type casting

## Key Concepts

### Variables
Variables are containers for storing data values in Python.
```python
name = "Alice"
age = 25
height = 5.8
```

### Data Types
- **int**: integers (5, -10, 100)
- **float**: decimal numbers (3.14, -2.5)
- **str**: text strings ("Hello", 'World')
- **bool**: Boolean values (True, False)

### Type Casting
Converting one data type to another.
```python
x = int("50")           # String to integer
y = float("3.14")       # String to float
z = str(100)            # Integer to string
```

### Input and Output
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

## How to Run
```bash
cd /Users/kanha/DevOps/python-practice/python_practice
source .venv/bin/activate
python 1_phase_introduction.py
```

## Practice Exercises
1. Create variables for your name, age, and city
2. Print them using f-strings
3. Take input from user and display it
4. Perform arithmetic operations and display results
5. Practice type casting with different data types

## Resources
- Official Python Documentation: https://docs.python.org/3/
- Python for Beginners: https://www.python.org/about/gettingstarted/

## Next Phase
Move on to Phase 2 to learn about loops and control flow.
