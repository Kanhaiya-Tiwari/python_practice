# Phase 4: Collections (Lists, Tuples, Dictionaries, Sets)

## Overview
Learn to work with Python collections: data structures for storing multiple values. Master lists, tuples, dictionaries, and sets—each with different characteristics and use cases.

## Learning Objectives
- Understand mutable vs immutable data structures
- Master list operations (append, extend, remove, pop)
- Work with tuples for immutable sequences
- Create and manipulate dictionaries
- Use sets for unique values
- Know when to use each collection type

## Key Concepts

### Lists (Mutable)
Ordered, changeable sequences.
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")           # Add single element
fruits.extend(["fig", "grape"]) # Add multiple elements
fruits.remove("banana")         # Remove by value
popped = fruits.pop()           # Remove and return last
fruits.sort()                   # Sort in place
```

### Tuples (Immutable)
Ordered, unchangeable sequences. Use when data shouldn't change.
```python
coordinates = (10, 20)
location = ("New York", "NY", "USA")
# Can be used as dictionary keys
data = {}
data[coordinates] = "Point A"
```

### Dictionaries
Key-value pairs; unordered (in Python 3.7+, ordered by insertion).
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}
print(person["name"])           # Access by key
person["email"] = "alice@email.com"  # Add new key
value = person.get("age", "Unknown") # Safe access
keys = person.keys()            # Get all keys
values = person.values()        # Get all values
```

### Sets
Unordered, unique values. No duplicates allowed.
```python
colors = {"red", "blue", "green"}
colors.add("yellow")            # Add element
colors.remove("blue")           # Remove element
common = {"red", "blue"} & {"red", "green"}  # Intersection
all_colors = {"red"} | {"blue"}             # Union
```

## Collection Comparison

| Feature | List | Tuple | Dict | Set |
|---------|------|-------|------|-----|
| Mutable | ✓ | ✗ | ✓ | ✓ |
| Indexed | ✓ | ✓ | ✗ | ✗ |
| Ordered | ✓ | ✓ | ✓ | ✗ |
| Duplicates | ✓ | ✓ | Keys: ✗ | ✗ |
| Use Case | Any data | Fixed data | Key-value | Unique values |

## Common Operations

### List Methods
```python
numbers = [3, 1, 4, 1, 5]
print(len(numbers))             # 5
print(numbers.count(1))         # 2
print(numbers.index(4))         # 2
numbers.reverse()               # Reverse in place
sorted_nums = sorted(numbers)   # Return sorted copy
```

### Dictionary Methods
```python
student = {"name": "Bob", "gpa": 3.8}
print(student.get("age", 0))    # Default value if key missing
del student["gpa"]              # Delete key
student.update({"age": 20})     # Merge dictionaries
for key, value in student.items():
    print(f"{key}: {value}")
```

### Set Operations
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)              # Intersection: {3}
print(set1 | set2)              # Union: {1, 2, 3, 4, 5}
print(set1 - set2)              # Difference: {1, 2}
print(set1 ^ set2)              # Symmetric difference: {1, 2, 4, 5}
```

## How to Run
```bash
cd /Users/kanha/DevOps/python-practice/python_practice
source .venv/bin/activate
python 4_phase_Collections.py
```

## Practice Exercises
1. Create a list of 5 students and their scores
2. Sort a list of numbers without using sort()
3. Create a dictionary of countries and capitals
4. Find duplicates in a list using sets
5. Merge two dictionaries
6. Remove duplicates from a list using set

## Interview Questions Covered
✓ List vs Tuple
✓ List Mutability
✓ append() vs extend()
✓ remove() vs pop()
✓ sort() vs sorted()
✓ Dictionary vs Set
✓ Dictionary Key Uniqueness
✓ get() vs []
✓ union() vs intersection()
✓ When to Use Sets vs Lists

## Performance Tips
- Use lists for ordered data that changes
- Use tuples for fixed data or dictionary keys
- Use dictionaries for fast key-value lookups
- Use sets to remove duplicates (fast O(1) lookup)

## Common Patterns
```python
# Count occurrences
from collections import Counter
items = [1, 2, 2, 3, 3, 3]
counts = Counter(items)         # {3: 3, 2: 2, 1: 1}

# Find common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))  # [3, 4]
```

## Next Phase
Move on to Phase 5 to learn about functions and code reusability.
