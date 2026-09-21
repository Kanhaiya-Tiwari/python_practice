import os
import shutil
import subprocess
from pathlib import Path


# Copy file
source = Path('demo_source.txt')
source.write_text('This is a sample file for OS automation.', encoding='utf-8')

destination = Path('demo_copy.txt')
shutil.copy2(source, destination)
print('File copied:', destination.exists())

# Rename file
renamed = Path('demo_renamed.txt')
if destination.exists():
    destination.rename(renamed)
    print('File renamed to:', renamed)

# Delete file
if renamed.exists():
    renamed.unlink()
    print('File deleted successfully')

# Environment variable
print('HOME:', os.getenv('HOME'))
print('Current directory:', os.getcwd())

# Check disk usage
usage = shutil.disk_usage('/')
print('Disk usage:')
print('Total:', usage.total)
print('Used:', usage.used)
print('Free:', usage.free)

# Execute a command
result = subprocess.run(['echo', 'Hello from subprocess'], capture_output=True, text=True)
print('Command output:', result.stdout.strip())
