# unittest
# unittest is Python's built-in testing framework.

import unittest

def add(a,b):
    return a+b

class TestMath(unittest.TestCase):

    def test_add(self):

        self.assertEqual(add(2,3),5)

unittest.main()

# pytest 
# pytest is a modern and more user-friendly testing framework.
import pytest

def test_add():
    assert add(2,3) == 5

""""
configparser

Reads .ini configuration files.

Example

config.ini

[database]
host=localhost
port=5432
"""

import configparser

config = configparser.ConfigParser()

config.read("config.ini")

print(config["database"]["host"])

# dotenv

from dotenv import load_dotenv

import os

load_dotenv()

print(os.getenv("DB_HOST"))

# YAML Configuration

import yaml

with open("config.yaml") as file:

    config = yaml.safe_load(file)

print(config)

# JSON Configuration

import json

with open("config.json") as file:

    config = json.load(file)

print(config)