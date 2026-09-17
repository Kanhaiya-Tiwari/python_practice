"""
Modules & Packages Interview Questions and Answers

=== BASIC ===

1. What is a module?
A module is a Python file containing reusable code like functions, variables, and classes.
Example: math.py is a module.
You can use it in other files by importing it.

2. What is a package?
A package is a directory containing Python modules and an __init__.py file.
It is a way to organize related modules into a directory structure.
Example: requests/ is a package containing many modules.

3. Difference between module and package?
A module is a single Python file (.py).
A package is a directory with an __init__.py file containing multiple modules.
Example: os.py is a module; os/ is a package.

4. Difference between import and from ... import?
import brings the entire module into the namespace.
Example: import os; os.getcwd()

from ... import brings specific items from a module.
Example: from os import getcwd; getcwd()

5. Why do we use aliases?
Aliases (using 'as') make long module names shorter and easier to use.
Example: import numpy as np; np.array([1, 2, 3])
They avoid name conflicts and improve code readability.

6. What is __init__.py?
__init__.py is a file that tells Python a directory is a package.
It can be empty or contain initialization code for the package.
It is executed when the package is imported.
Example: When you import mypackage, Python runs __init__.py first.

=== OS MODULE ===

7. Difference between os and pathlib?
os is an older module for file and directory operations using strings.
Example: os.path.join('folder', 'file.txt')

pathlib is a newer module with object-oriented paths.
Example: Path('folder') / 'file.txt'

pathlib is more modern and easier to use.

8. How do you check if a file exists?
import os
if os.path.exists('file.txt'):
    print('File exists')

Or with pathlib:
from pathlib import Path
if Path('file.txt').exists():
    print('File exists')

9. How do you list files?
import os
files = os.listdir('.')
print(files)

Or with pathlib:
from pathlib import Path
files = list(Path('.').iterdir())
print(files)

=== SYS MODULE ===

10. What is sys.argv?
sys.argv is a list of command-line arguments passed to a Python script.
The first element (sys.argv[0]) is the script name.
Other elements are the arguments provided by the user.
Example: python script.py name age
print(sys.argv)  # ['script.py', 'name', 'age']

=== JSON MODULE ===

11. Difference between loads() and dumps()?
json.loads() converts a JSON string into a Python object (dictionary).
Example: data = json.loads('{"name": "Alice"}')

json.dumps() converts a Python object into a JSON string.
Example: json_str = json.dumps({'name': 'Alice'})

=== LOGGING MODULE ===

12. Why use logging instead of print()?
print() output is only visible in the console.
logging allows you to save messages to files, set severity levels, and format messages.
Example:
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)
logging.info('This message is saved to app.log')

=== SUBPROCESS MODULE ===

13. How do you execute Linux commands in Python?
import subprocess
result = subprocess.run(['ls', '-l'], capture_output=True)
print(result.stdout.decode())

Or use shell=True for complex commands:
subprocess.run('ls -la', shell=True)

=== ARGPARSE MODULE ===

14. Why use argparse?
argparse is used to parse command-line arguments easily.
It automatically creates help messages and validates input.
Example:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name', help='Your name')
parser.add_argument('--age', type=int, help='Your age')
args = parser.parse_args()
print(args.name, args.age)

=== ADDITIONAL CONCEPTS ===

15. What is the difference between absolute and relative imports?
Absolute import: from mypackage.module import function
Relative import: from ..module import function (from parent package)

Absolute imports are recommended as they are clearer and work from anywhere.

16. How do you create a module?
Just create a Python file with functions and classes.
Example: mymodule.py
Then import it: import mymodule or from mymodule import function

17. What is pip?
pip is the package management tool for Python.
It installs and manages third-party packages.
Example: pip install requests

18. What is a virtual environment?
A virtual environment is an isolated Python environment for a project.
It keeps dependencies separate from the system Python.
Create: python -m venv venv
Activate: source venv/bin/activate (on macOS/Linux)

"""