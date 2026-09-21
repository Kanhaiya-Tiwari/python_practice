# Phase 13 — OS Automation

This phase covers Python modules used to automate operating system tasks.

## Modules

- os
- pathlib
- shutil
- subprocess

## Tasks Covered

- Copy files
- Rename files
- Delete files
- Execute commands
- Check disk usage
- Work with environment variables

## Files

- `interview.txt` — Q&A notes
- `os_automation_example.py` — example code

## Example

```python
import os
from pathlib import Path
import shutil

source = Path('sample.txt')
source.write_text('Hello from Python', encoding='utf-8')

copy_path = Path('sample_copy.txt')
shutil.copy2(source, copy_path)

print(os.path.exists(copy_path))
print(os.getenv('HOME'))
```

## Use Cases

- File maintenance
- Deployment scripts
- Configuration and environment setup
- Automation of admin tasks

## References

- Python os module: https://docs.python.org/3/library/os.html
- Python pathlib: https://docs.python.org/3/library/pathlib.html
- Python shutil: https://docs.python.org/3/library/shutil.html
- Python subprocess: https://docs.python.org/3/library/subprocess.html
