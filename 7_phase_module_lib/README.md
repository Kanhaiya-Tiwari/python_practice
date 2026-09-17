# Phase 7: Modules and Packages

## Overview
Learn to organize and reuse code using modules and packages. Master imports, built-in modules, and third-party libraries essential for real-world Python development.

## Learning Objectives
- Understand modules and packages
- Master import statements
- Use built-in modules (os, sys, json, logging, subprocess, argparse)
- Compare os and pathlib
- Read command-line arguments with sys.argv
- Handle JSON data
- Implement logging
- Execute system commands

## Key Concepts

### What is a Module?
A Python file containing reusable code.
```python
# math_functions.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### What is a Package?
A directory containing modules and `__init__.py`.
```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

### Import Statements

**Full import:**
```python
import os
print(os.getcwd())
```

**Import specific item:**
```python
from os import getcwd
print(getcwd())
```

**Import with alias:**
```python
import numpy as np
arr = np.array([1, 2, 3])
```

**Import multiple items:**
```python
from os import getcwd, listdir, path
```

### __init__.py
Makes a directory a package; can contain initialization code.
```python
# mypackage/__init__.py
print("Initializing mypackage")
VERSION = "1.0"
```

## Built-in Modules

### OS Module (Operating System)
Interact with the operating system.
```python
import os

print(os.getcwd())                 # Current directory
print(os.listdir('.'))             # List files
print(os.path.exists('file.txt'))  # Check file existence
os.chdir('/path/to/dir')          # Change directory
os.mkdir('new_folder')            # Create directory
```

### pathlib Module (Modern Path Handling)
Object-oriented approach to file paths.
```python
from pathlib import Path

p = Path('.')
print(p.cwd())                     # Current directory
files = list(p.glob('*.txt'))     # Find files
p_file = Path('data.txt')
print(p_file.exists())
print(p_file.suffix)               # File extension
```

### os vs pathlib Comparison
| Task | os | pathlib |
|------|-----|---------|
| Current dir | os.getcwd() | Path.cwd() |
| Check exists | os.path.exists(p) | Path(p).exists() |
| List files | os.listdir(d) | list(Path(d).iterdir()) |
| Join paths | os.path.join(a, b) | Path(a) / b |
| File ext | os.path.splitext(f) | Path(f).suffix |
| Create dir | os.mkdir(d) | Path(d).mkdir() |

### sys Module (System-Specific)
Access system-specific parameters and functions.
```python
import sys

print(sys.argv)        # Command-line arguments
print(sys.version)     # Python version
print(sys.platform)    # Operating system
sys.exit(0)           # Exit program
```

**Using sys.argv:**
```python
# script.py
import sys
print(sys.argv)  # ['script.py', arg1, arg2, ...]
```
```bash
python script.py hello world
# Output: ['script.py', 'hello', 'world']
```

### json Module (JSON Data)
Parse and create JSON.
```python
import json

# Dictionary to JSON string
data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)

# JSON string to dictionary
parsed = json.loads(json_str)

# File operations
with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)
```

**loads() vs dumps():**
- `json.loads(string)` - Parse JSON string → Python object
- `json.dumps(object)` - Convert Python object → JSON string
- `json.load(file)` - Parse JSON from file
- `json.dump(object, file)` - Write JSON to file

### logging Module (Logging)
Record program events and errors.
```python
import logging

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log messages
logging.debug('Debug message')      # Lowest priority
logging.info('Info message')
logging.warning('Warning message')  # Default level
logging.error('Error message')
logging.critical('Critical message') # Highest priority
```

**Why logging over print():**
- Logs go to file, not just console
- Severity levels for filtering
- Timestamps and formatters
- Can be rotated by size or time
- Essential for production code

### subprocess Module (System Commands)
Execute system commands from Python.
```python
import subprocess

# Simple command
result = subprocess.run(['ls', '-la'], capture_output=True)
print(result.stdout.decode())

# With shell
subprocess.run('ls -la', shell=True)

# Get output
result = subprocess.run(['echo', 'Hello'], capture_output=True, text=True)
print(result.stdout)  # 'Hello\n'
```

### argparse Module (Command-Line Arguments)
Parse command-line arguments professionally.
```python
import argparse

parser = argparse.ArgumentParser(description='Process some data')
parser.add_argument('name', help='Your name')
parser.add_argument('--age', type=int, help='Your age')
parser.add_argument('--city', default='NYC', help='Your city')

args = parser.parse_args()
print(f"{args.name} is {args.age} from {args.city}")
```
```bash
python script.py Alice --age 25 --city Boston
```

## Creating Your Own Module

Create `calculator.py`:
```python
def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b
```

Use it:
```python
import calculator
result = calculator.add(5, 3)
print(result)  # 8
```

## Module Search Path
Python looks for modules in:
1. Current directory
2. PYTHONPATH environment variable
3. Installation-dependent default path

```python
import sys
print(sys.path)  # Shows all search paths
```

## How to Run
```bash
cd /Users/kanha/DevOps/python-practice/python_practice
source .venv/bin/activate
python 7_phase_Modules\ \&\ Packages.py
```

## Practice Exercises
1. Create a simple module with math functions
2. Read current directory and list all Python files
3. Create a JSON file with user data
4. Build a command-line tool using argparse
5. Implement logging in a multi-function program
6. Execute system commands using subprocess
7. Compare os vs pathlib for file operations

## Interview Questions Covered
✓ What is a module
✓ What is a package
✓ Module vs Package
✓ import vs from...import
✓ Why use aliases
✓ __init__.py purpose
✓ os vs pathlib
✓ File existence check
✓ Listing files
✓ sys.argv
✓ loads() vs dumps()
✓ Logging over print()
✓ Executing Linux commands
✓ argparse purpose

## Best Practices

### Imports
- Put all imports at the top of the file
- Use absolute imports (avoid circular imports)
- Import modules, not * (except for special cases)
- Organize: standard library → third-party → local

### Module Organization
```python
"""
Module documentation (docstring)
"""
import standard_lib
import third_party
from . import local_module

# Constants
DEBUG = True

# Functions
def main():
    pass

# Main execution
if __name__ == "__main__":
    main()
```

### Virtual Environments
```bash
# Create
python -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Deactivate
deactivate

# Install packages
pip install requests
```

## Common Pitfalls
- Circular imports (module A imports B, B imports A)
- Naming conflicts with standard library
- Not using virtual environments
- Installing packages globally instead of in venv

## pip (Package Manager)
```bash
pip install package_name           # Install
pip uninstall package_name         # Uninstall
pip list                          # List installed
pip freeze > requirements.txt     # Export dependencies
pip install -r requirements.txt   # Install from file
```

## Next Phase
Move on to Phase 8 to learn about file handling and I/O operations.
