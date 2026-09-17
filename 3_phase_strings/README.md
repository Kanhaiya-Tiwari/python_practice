# Phase 3: Strings and String Manipulation

## Overview
Master Python strings including creation, manipulation, formatting, and string-specific methods. Strings are immutable and essential for data handling.

## Learning Objectives
- Understand string immutability
- Learn string indexing and slicing
- Master string methods (find, replace, split, join)
- Format strings using f-strings and .format()
- Work with Unicode and encoding

## Key Concepts

### String Basics
Strings are sequences of characters enclosed in quotes.
```python
name = "Alice"          # Single quotes
message = 'Hello'       # Double quotes
multiline = """Long
string here"""          # Triple quotes
```

### Indexing and Slicing
Access characters or substrings.
```python
text = "Python"
print(text[0])          # 'P' (first character)
print(text[-1])         # 'n' (last character)
print(text[0:4])        # 'Pyth' (slice)
print(text[::-1])       # 'nohtyP' (reverse)
```

### String Methods
Common operations on strings.
```python
text = "hello world"
print(text.upper())              # HELLO WORLD
print(text.capitalize())         # Hello world
print(text.find('o'))            # First index of 'o'
print(text.replace('o', '0'))    # hell0 w0rld
parts = text.split()             # ['hello', 'world']
```

### String Formatting
Three modern ways to format strings.
```python
name = "Bob"
age = 30

# f-strings (recommended, Python 3.6+)
print(f"{name} is {age} years old")

# .format() method
print("{} is {} years old".format(name, age))

# Simple concatenation
print(name + " is " + str(age) + " years old")
```

### Raw Strings
Treat backslashes as literal characters.
```python
path = r"C:\new\folder"         # Raw string
regex = r"\d+\.\d+"             # Regular expression pattern
```

## Common String Operations

### Check Contents
```python
text = "Python Programming"
print("Python" in text)          # True
print(text.startswith("Python")) # True
print(text.endswith("ing"))      # True
```

### Split and Join
```python
csv = "apple,banana,cherry"
fruits = csv.split(",")          # ['apple', 'banana', 'cherry']
result = "-".join(fruits)        # apple-banana-cherry
```

### Strip Whitespace
```python
text = "  Hello World  "
print(text.strip())              # "Hello World"
print(text.lstrip())             # "Hello World  "
print(text.rstrip())             # "  Hello World"
```

## How to Run
```bash
cd /Users/kanha/DevOps/python-practice/python_practice
source .venv/bin/activate
python phase3-string.py
```

## Practice Exercises
1. Extract first and last character from a string
2. Count vowels in a sentence
3. Reverse a string using slicing
4. Check if a string is a palindrome
5. Convert string to title case
6. Replace multiple characters efficiently

## Interview Questions Covered
✓ Indexing vs Slicing
✓ String Immutability
✓ find() vs index()
✓ split() vs join()
✓ Raw Strings
✓ Unicode and UTF-8
✓ f-strings vs .format()
✓ Negative Indexing
✓ String Reversal

## Performance Tips
- Use f-strings for formatting (fastest)
- Use join() for concatenating many strings
- Avoid string concatenation in loops (creates new objects)

## Next Phase
Move on to Phase 4 to learn about collections (lists, tuples, dictionaries, sets).
