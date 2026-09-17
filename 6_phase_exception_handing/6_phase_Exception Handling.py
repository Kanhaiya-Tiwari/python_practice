
# Handle a ZeroDivisionError using try and except.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
# Read a file using try, except, and finally.
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("This always runs")

# Raise a ValueError if a user enters a negative age.
age = -1
if age < 0:
    raise ValueError("Age cannot be negative")

# Create a custom exception named ServerDownError and raise it when a simulated server status is "DOWN".
class ServerDownError(Exception):
    pass

server_status = "DOWN"
if server_status == "DOWN":
    raise ServerDownError("Server is currently down")