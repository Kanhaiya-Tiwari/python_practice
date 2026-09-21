"

import json
import logging
import os
import shutil
import subprocess
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


# -------------------------
# Phase 14: JSON & YAML
# -------------------------

def json_parsing_example():
    """Convert a JSON string into a Python dictionary."""
    json_text = '{"name": "Alice", "age": 25, "skills": ["Python", "SQL"]}'
    data = json.loads(json_text)
    print("JSON parsing:", data)
    print("Name:", data["name"])


def json_dump_example():
    """Convert a Python dictionary into a JSON string."""
    data = {"name": "Bob", "age": 30, "skills": ["Java", "AWS"]}
    json_text = json.dumps(data, indent=2)
    print("JSON dump:")
    print(json_text)


def json_load_example(file_path):
    """Read JSON data from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        loaded = json.load(file)
    print("JSON load:", loaded)


def yaml_read_example(file_path):
    """Read YAML content from a file."""
    if yaml is None:
        print("PyYAML is not installed. Install it with: pip install pyyaml")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    print("YAML read:", data)


def yaml_write_example(file_path):
    """Write Python data into YAML format."""
    if yaml is None:
        print("PyYAML is not installed. Install it with: pip install pyyaml")
        return

    data = {"name": "Charlie", "age": 35, "project": "Python Practice"}
    with open(file_path, "w", encoding="utf-8") as file:
        yaml.safe_dump(data, file, sort_keys=False)
    print(f"YAML written to {file_path}")
