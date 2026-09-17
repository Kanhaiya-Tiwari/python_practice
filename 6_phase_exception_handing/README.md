# Phase 6: Exception Handling and Error Management

## Overview
Learn to handle errors gracefully in your programs. Master try-except blocks, custom exceptions, and best practices for robust error handling that prevents program crashes.

## Learning Objectives
- Understand exception hierarchy
- Master try-except-else-finally blocks
- Handle specific exceptions
- Create custom exceptions
- Use raise to trigger exceptions
- Implement assertions for validation
- Write defensive, error-resistant code

## Key Concepts

### Basic Try-Except
Catch and handle errors without crashing.
```python
try:
    value = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Multiple Except Blocks
Handle different exception types.
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That's not a valid integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
```

### Else Block
Runs if no exception occurs in try block.
```python
try:
    value = int("42")
except ValueError:
    print("Invalid input")
else:
    print(f"Successfully converted: {value}")
```

### Finally Block
Always executes, whether exception occurs or not.
```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    if 'file' in locals():
        file.close()  # Always close the file
print("Program ends")
```

### Raise Statement
Manually trigger an exception.
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Invalid input: {e}")
```

### Assert Statement
Validate conditions; assert False raises AssertionError.
```python
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

divide(10, 0)  # Raises AssertionError: Divisor cannot be zero
```

### Custom Exceptions
Create application-specific exception classes.
```python
class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Age {age} is invalid")

try:
    age = -5
    if age < 0:
        raise InvalidAgeError(age)
except InvalidAgeError as e:
    print(f"Error: {e}")
```

## Exception Hierarchy
Python's built-in exceptions form a hierarchy:
```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ValueError        # Wrong value
    ├── TypeError         # Wrong type
    ├── IndexError        # Out of range index
    ├── KeyError          # Missing dictionary key
    ├── FileNotFoundError # File doesn't exist
    ├── ZeroDivisionError # Division by zero
    ├── AttributeError    # Missing attribute
    └── ... (many more)
```

## Common Exception Types

| Exception | When Raised | Example |
|-----------|------------|---------|
| ValueError | Invalid value | int("abc") |
| TypeError | Wrong type | "string" + 5 |
| IndexError | List index out of range | list[10] on 5-item list |
| KeyError | Dictionary key missing | dict["missing"] |
| FileNotFoundError | File not found | open("xyz.txt") |
| ZeroDivisionError | Division by zero | 10 / 0 |
| AttributeError | Missing attribute | obj.missing_attr |

## Practical Examples

### File Reading with Error Handling
```python
def read_file_safe(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except IOError:
        print("Error reading file")
        return None
    finally:
        print("Read operation completed")
```

### Type Validation
```python
def process_age(age):
    try:
        age = int(age)
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150")
        return f"Valid age: {age}"
    except ValueError as e:
        return f"Invalid: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
```

### Logging Exceptions
```python
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"Math error occurred: {e}")
```

## How to Run
```bash
cd /Users/kanha/DevOps/python-practice/python_practice
source .venv/bin/activate
python "6_phase_Exception Handling.py"
```

## Practice Exercises
1. Create a function that reads a file and handles FileNotFoundError
2. Write age validation using try-except and raise
3. Create a custom exception for invalid credentials
4. Build a calculator that handles all division errors
5. Implement retry logic with exception handling
6. Create logging for all exceptions in a program

## Interview Questions Covered
✓ Why use exception handling
✓ except vs finally
✓ else block execution
✓ raise statement
✓ assert purpose
✓ Custom exceptions

## Best Practices

### DO's ✓
- Catch specific exceptions
- Use finally for cleanup
- Create custom exceptions for your domain
- Log exceptions for debugging
- Provide meaningful error messages
- Validate input early

### DON'Ts ✗
- Don't use bare except: (catches everything)
- Don't ignore exceptions silently
- Don't use exception handling for normal flow
- Don't catch too broad (Exception catches everything)
- Don't raise generic exceptions inappropriately

## Anti-Patterns to Avoid

### Bad: Too Broad
```python
try:
    # Many lines of code
except Exception:
    pass  # Silently ignore all errors!
```

### Good: Specific Handling
```python
try:
    value = int(user_input)
except ValueError:
    print("Please enter a valid number")
else:
    process(value)
```

## Chaining Exceptions (Advanced)
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    raise ValueError("Cannot process division") from e
```

## Testing Exceptions
```python
import unittest

def test_division_by_zero():
    with self.assertRaises(ZeroDivisionError):
        result = 10 / 0
```

## Next Phase
Move on to Phase 7 to learn about modules, packages, and importing code.
