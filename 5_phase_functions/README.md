# Phase 5: Functions and Code Reusability

## Overview
Learn to write functions—reusable blocks of code that perform specific tasks. Master parameters, return values, scope, and advanced function concepts.

## Learning Objectives
- Define and call functions
- Understand parameters and arguments
- Master return values
- Learn variable scope (local vs global)
- Use *args and **kwargs for flexible functions
- Understand recursion and lambda functions
- Create nested functions

## Key Concepts

### Function Basics
Define a reusable block of code.
```python
def greet(name):
    message = f"Hello, {name}!"
    return message

result = greet("Alice")
print(result)  # Hello, Alice!
```

### Parameters vs Arguments
- **Parameters**: Variable names in function definition
- **Arguments**: Actual values passed when calling function

```python
def add(a, b):          # a, b are parameters
    return a + b

result = add(5, 3)      # 5, 3 are arguments
```

### Return Statement
Return values from a function.
```python
def calculate(x, y):
    sum_val = x + y
    diff = x - y
    return sum_val, diff  # Return multiple values as tuple

total, difference = calculate(10, 3)
print(total, difference)  # 13, 7
```

### Default Parameters
Provide default values for parameters.
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))       # 9 (uses default)
print(power(3, 3))    # 27 (uses provided value)
```

### Variable Scope
Where a variable can be accessed.
```python
global_var = 10  # Global scope

def outer():
    local_var = 5  # Local scope
    print(global_var)  # Can access global
    return local_var

outer()
# print(local_var)  # Error: local_var not accessible here
```

### *args (Variable Positional Arguments)
Accept any number of positional arguments.
```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))      # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
```

### **kwargs (Variable Keyword Arguments)
Accept any number of keyword arguments.
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# name: Alice
# age: 25
# city: NYC
```

### Lambda Functions
Anonymous, single-line functions.
```python
square = lambda x: x ** 2
print(square(5))  # 25

# Commonly used with sorted() or map()
numbers = [3, 1, 4, 1, 5]
sorted_nums = sorted(numbers, key=lambda x: -x)  # Descending
```

### Recursion
A function that calls itself.
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### Nested Functions
Functions defined inside other functions.
```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))  # 8
```

## How to Run
```bash
cd /Users/kanha/DevOps/python-practice/python_practice
source .venv/bin/activate
python 5_phase_functions.py
```

## Practice Exercises
1. Create a function to check if a number is prime
2. Write a function to calculate factorial using recursion
3. Create a function that accepts *args and returns the average
4. Write a function with **kwargs to create a user profile
5. Use lambda to sort a list of dictionaries by a specific key
6. Create a nested function for calculating compound interest

## Function Patterns

### Decorator Pattern (Preview)
```python
def uppercase_decorator(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"hello, {name}"

print(greet("bob"))  # HELLO, BOB
```

### Closure
```python
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

triple = multiplier(3)
print(triple(5))  # 15
```

## Interview Questions Covered
✓ Parameters vs Arguments
✓ return vs print()
✓ *args vs **kwargs
✓ Recursion
✓ Lambda Functions
✓ Variable Scope
✓ Nested Functions

## Best Practices
- Keep functions small and focused (single responsibility)
- Use clear, descriptive function names
- Document with docstrings
- Avoid excessive use of global variables
- Use type hints for clarity (Python 3.5+)
- Return early to avoid deep nesting

## Docstring Example
```python
def calculate_age(birth_year):
    """
    Calculate age based on birth year.
    
    Args:
        birth_year (int): Year of birth
    
    Returns:
        int: Current age
    """
    current_year = 2024
    return current_year - birth_year
```

## Common Function Mistakes
- Forgetting to return a value
- Modifying mutable parameters unintentionally
- Using mutable default arguments (use None instead)
- Shadowing built-in functions

## Performance Considerations
- Avoid redundant function calls in loops
- Use generators for large datasets
- Cache results of expensive functions
- Profile your code to find bottlenecks

## Next Phase
Move on to Phase 6 to learn about exception handling and error management.
