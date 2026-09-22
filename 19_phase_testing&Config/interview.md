Configuration Management

Applications should not store configuration directly in the source code.

configparser

Reads .ini configuration files.

Example

config.ini

[database]
host=localhost
port=5432

Python

import configparser

config = configparser.ConfigParser()

config.read("config.ini")

print(config["database"]["host"])
dotenv ⭐⭐⭐⭐⭐

Used for environment variables.

Install

pip install python-dotenv

.env

DB_HOST=localhost
DB_PASSWORD=secret123

Python

from dotenv import load_dotenv

import os

load_dotenv()

print(os.getenv("DB_HOST"))

Reason

Never hardcode passwords or API keys.

YAML Configuration

config.yaml

database:
  host: localhost
  port: 5432

Python

import yaml

with open("config.yaml") as file:

    config = yaml.safe_load(file)

print(config)
JSON Configuration

config.json

{
  "database":{
      "host":"localhost"
  }
}

Python

import json

with open("config.json") as file:

    config = json.load(file)

print(config)
Configuration File Comparison
Format	Best For
.env	Secrets, passwords, API keys
.ini	Small applications
.json	API responses and structured configuration
.yaml	Kubernetes, Ansible, Docker Compose, CI/CD