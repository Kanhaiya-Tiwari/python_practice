"""
Exception Handling Interview Questions and Answers

1. Why do we use exception handling?
We use exception handling to handle runtime errors gracefully without crashing the program.
It helps us manage invalid input, missing files, division by zero, and other unexpected situations.
Example:
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

2. What is the difference between except and finally?
except is used to catch and handle specific errors that occur in the try block.
finally always executes whether an exception occurs or not.
It is usually used for cleanup tasks like closing files or database connections.
Example:
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("This always runs")

3. When does the else block execute?
The else block executes only if no exception occurs in the try block.
It runs after successful code execution and before finally.
Example:
try:
    value = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Division successful")

4. Why do we use raise?
raise is used to manually trigger an exception when a certain condition is not met.
It helps enforce business rules and validate input.
Example:
age = -1
if age < 0:
    raise ValueError("Age cannot be negative")

5. What is the purpose of assert?
assert is used for debugging and validation.
It checks whether a condition is true and raises an AssertionError if it is false.
Example:
num = 5
assert num > 0, "Number must be positive"

6. How do you create a custom exception?
You create a custom exception by defining a new class that inherits from Exception.
This is useful when you want to raise application-specific errors.
Example:
class InvalidAgeError(Exception):
    pass

age = -1
if age < 0:
    raise InvalidAgeError("Age cannot be negative")

7. What is the difference between try, except, else, and finally?
try contains the code that may raise an exception.
except handles the exception.
else runs when no exception occurs.
finally runs always, whether there is an error or not.

8. What is a typical exception hierarchy in Python?
Python has built-in exception classes like ValueError, TypeError, ZeroDivisionError, and FileNotFoundError.
All of them inherit from the base Exception class.

9. Why is exception handling important in real applications?
It prevents the whole program from crashing and allows users to see meaningful error messages.
It also helps developers debug and maintain code more effectively.

10. Can we catch multiple exceptions in one block?
Yes, multiple exceptions can be handled using a tuple in one except block.
Example:
try:
    value = int("abc")
except (ValueError, TypeError):
    print("Invalid value")

"""
