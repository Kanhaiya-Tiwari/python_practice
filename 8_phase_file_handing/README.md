# Phase 8: File Handling and I/O Operations

## Overview
Master reading, writing, and manipulating files. Learn to handle different file types safely using best practices and exception handling.

## Learning Objectives
- Understand file modes (r, w, a, x, b, t)
- Read files safely using context managers
- Write and append data to files
- Work with text and binary files
- Handle file-related exceptions
- Implement efficient file operations
- Create file processing pipelines

## Key Concepts

### File Modes

| Mode | Purpose | Behavior |
|------|---------|----------|
| `r` | Read | File must exist |
| `w` | Write | Creates/overwrites file |
| `a` | Append | Creates/adds to end |
| `x` | Exclusive | Fails if file exists |
| `b` | Binary | Use with other modes |
| `t` | Text | Default, use with others |
| `+` | Read/Write | Use with r/w/a |

Examples:
```python
open('file.txt', 'r')      # Read text (default)
open('file.txt', 'w')      # Write text
open('file.txt', 'a')      # Append text
open('image.jpg', 'rb')    # Read binary
open('output.bin', 'wb')   # Write binary
open('file.txt', 'r+')     # Read and write
```

### The with Statement (Context Manager)
Automatically handles file closing, even if errors occur.
```python
# GOOD: Automatic file closing
with open('file.txt', 'r') as f:
    content = f.read()

# BAD: Manual closing, easy to forget
f = open('file.txt', 'r')
content = f.read()
f.close()
```
### Reading Files

**read() - Entire file as string:**
```python
with open('story.txt', 'r') as f:
    content = f.read()  # Entire content
print(content)
```

**readline() - One line at a time:**
```python
with open('story.txt', 'r') as f:
    line1 = f.readline()  # First line
    line2 = f.readline()  # Second line
```

**readlines() - All lines as list:**
```python
with open('story.txt', 'r') as f:
    lines = f.readlines()  # List of strings
    for line in lines:
        print(line.strip())
```

**Iterate line by line (memory efficient):**
```python
with open('large_file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Process one line at a time
```

### Writing Files

**write() - Text mode:**
```python
with open('output.txt', 'w') as f:
    f.write('First line\n')
    f.write('Second line\n')
```

**writelines() - Multiple lines at once:**
```python
lines = ['Hello\n', 'World\n', 'Python\n']
with open('output.txt', 'w') as f:
    f.writelines(lines)
```

**Append mode - Add without overwriting:**
```python
with open('log.txt', 'a') as f:
    f.write('New log entry\n')
```

### Text vs Binary Files

**Text files (ASCII/UTF-8):**
```python
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

**Binary files (images, PDFs, executables):**
```python
with open('image.jpg', 'rb') as f:
    image_data = f.read()
```

### File Existence and Properties

```python
import os
from pathlib import Path

# Using os module
if os.path.exists('file.txt'):
    print(os.path.getsize('file.txt'))  # File size
    print(os.path.isfile('file.txt'))   # Is file?

# Using pathlib (modern)
p = Path('file.txt')
if p.exists():
    print(p.stat().st_size)  # File size
    print(p.is_file())       # Is file?
```

## File Operations

### Copy a File
```python
import shutil

# Simple file copy
shutil.copy('source.txt', 'destination.txt')

# Binary file copy (any file type)
with open('source.bin', 'rb') as src:
    with open('destination.bin', 'wb') as dst:
        dst.write(src.read())
```

### Reading Large Files Efficiently
```python
def read_large_file(filename, chunk_size=4096):
    """Read large file in chunks"""
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            process(chunk)

# Or iterate line by line
def read_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()
```

### Search in File
```python
def find_in_file(filename, search_term):
    """Find search term in file"""
    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            if search_term in line:
                print(f"Found at line {line_num}: {line.strip()}")
```

### Modify File
```python
def replace_in_file(filename, old_text, new_text):
    """Replace text in file"""
    with open(filename, 'r') as f:
        content = f.read()
    
    new_content = content.replace(old_text, new_text)
    
    with open(filename, 'w') as f:
        f.write(new_content)
```

## Error Handling

### Handle FileNotFoundError
```python
try:
    with open('missing.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist")
except IOError:
    print("Cannot read file")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Validate Before Opening
```python
import os

if not os.path.exists('file.txt'):
    print("File not found")
else:
    with open('file.txt', 'r') as f:
        content = f.read()
```

### Handle Encoding Issues
```python
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    print("Encoding error - try different encoding")
    with open('file.txt', 'r', encoding='latin-1') as f:
        content = f.read()
```

## Practical Examples

### Log File Processor
```python
def process_logs(log_file):
    """Process log file and extract errors"""
    errors = []
    with open(log_file, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                errors.append(line.strip())
    return errors
```

### Backup Generator
```python
import shutil
from datetime import datetime

def create_backup(source_dir, backup_dir):
    """Create timestamped backup"""
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_path = f'{backup_dir}/backup_{timestamp}'
    
    try:
        shutil.copytree(source_dir, backup_path)
        return f"Backup created: {backup_path}"
    except Exception as e:
        return f"Backup failed: {e}"
```

### CSV File Reader
```python
def read_csv(filename):
    """Read CSV without external library"""
    data = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.strip().split(',')
            data.append(fields)
    return data
```

## How to Run
```bash
cd /Users/kanha/DevOps/python-practice/python_practice/8_phase_file_handing
source ../../.venv/bin/activate
python 8_phase_filehandling.py
```

## Practice Exercises
1. Create a program to count lines in a file
2. Read a CSV file and display as formatted table
3. Search for a word in multiple files
4. Create a log file rotator (archive old logs)
5. Implement a file backup utility
6. Build a text file merger
7. Create duplicate file finder
8. Implement file encryption/decryption basics

## Interview Questions Covered
✓ What is file handling
✓ Why use file handling
✓ Text vs binary files
✓ read() vs readline() vs readlines()
✓ write() vs append()
✓ with statement importance
✓ "w" vs "a" modes
✓ "r" vs "rb" modes
✓ FileNotFoundError handling
✓ File overwrite behavior
✓ Binary file copying
✓ Large file reading
✓ Backup report generation

## Best Practices

### DO's ✓
- Always use `with` statement
- Specify encoding explicitly (UTF-8)
- Check file existence before reading
- Use `append` mode instead of `r+`
- Read large files in chunks
- Use context managers
- Validate file paths
- Use pathlib for modern Python

### DON'Ts ✗
- Don't forget to close files (use `with`)
- Don't assume file exists
- Don't read entire large files into memory
- Don't ignore encoding issues
- Don't use string concatenation for paths
- Don't write binary and text in same open

### Encoding Tips
```python
# Always specify encoding
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Handle encoding errors
with open('file.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
```

## Performance Comparison

| Method | Use Case | Speed |
|--------|----------|-------|
| read() | Small files | Fast |
| readline() | One line processing | Medium |
| readlines() | All lines at once | Medium |
| for loop | Large files | Best |
| chunk reading | Very large files | Best |

## Common Patterns

### File Counter
```python
def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for line in f)
```

### File Size
```python
import os
size = os.path.getsize('file.txt')  # Bytes
size_mb = size / (1024 * 1024)      # Convert to MB
```

### Working with Directories
```python
import os
files = [f for f in os.listdir('.') if f.endswith('.txt')]
```

## Next Steps
- Explore file compression (zip, tar)
- Learn CSV/JSON libraries
- Study database file operations
- Experiment with file permissions

## Related Modules
- `csv` - Read/write CSV files
- `json` - Handle JSON files
- `pickle` - Serialize Python objects
- `shutil` - High-level file operations
- `pathlib` - Object-oriented path handling

---

**Congratulations!** You've completed the core Python learning phases. Now explore projects that combine all these concepts!
