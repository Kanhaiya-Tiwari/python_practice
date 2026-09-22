# 1. Linux Automation
# User Creation
import subprocess

subprocess.run(["sudo","useradd","kanha"])

# Backup Script

import shutil

source = "/home/project"
destination = "/backup/project"

shutil.copytree(source, destination)

import shutil

shutil.make_archive(
    "backup",
    "zip",
    "/home/project"
)

# Log Rotation

from pathlib import Path

logs = Path("/var/log")

for file in logs.glob("*.log"):
    print(file)

# Delete Old Logs
from pathlib import Path
import time

log_dir = Path("/var/log")

days = 30

for file in log_dir.glob("*.log"):

    age = time.time() - file.stat().st_mtime

    if age > days * 86400:
        file.unlink()

# SSH Automation
import paramiko

client = paramiko.SSHClient()

client.load_system_host_keys()

client.connect(
    hostname="192.168.1.10",
    username="ubuntu",
    password="password"
)

print("Connected")

# Suppose HR provides a CSV file containing 100 new employee names.
import csv
import subprocess

with open("users.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        username = row[0]
        subprocess.run(["sudo", "useradd", username])