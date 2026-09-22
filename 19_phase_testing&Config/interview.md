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


1. Q: What is software testing?
   A: Software testing is the process of checking whether an application works as expected and whether there are bugs or defects.

2. Q: Why is testing important in Python projects?
   A: Testing helps catch bugs early, improves reliability, reduces maintenance cost, and ensures code works correctly in different scenarios.

3. Q: What is unit testing?
   A: Unit testing checks the smallest testable part of an application, usually a function or method, in isolation.

4. Q: What is pytest?
   A: pytest is a Python testing framework that is simple to use and allows writing tests with functions and assertions.

5. Q: What is unittest?
   A: unittest is Python's built-in testing framework that supports test cases, test suites, and assertions using classes.

6. Q: What is an assertion in testing?
   A: An assertion is a statement that checks whether a condition is true. If it is false, the test fails.

7. Q: How do you write a basic test in pytest?
   A: Define a function that starts with test_, then write assert statements to validate expected behavior.

8. Q: What is a test case?
   A: A test case is a single unit of testing that checks a specific behavior or function output.

9. Q: What is TDD?
   A: TDD stands for Test-Driven Development. It means writing tests before implementing the logic, then writing code to make those tests pass.

10. Q: What is the difference between testing and debugging?
    A: Testing finds failures, while debugging is the process of identifying and fixing the cause of the failure.

11. Q: What is an integration test?
    A: An integration test checks how multiple components or modules work together and whether their interactions are correct.

12. Q: What is a functional test?
    A: A functional test checks whether the software behaves correctly from the user's perspective according to requirements.

13. Q: What is mocking in Python testing?
    A: Mocking is used to replace external dependencies or functions with fake objects so tests can run in isolation.

14. Q: Why do we use mocks in tests?
    A: Mocks are useful when testing code that depends on APIs, databases, file systems, or external services that are not available or should not be used in tests.

15. Q: What is the purpose of pytest fixtures?
    A: Fixtures provide reusable setup for tests, such as test data, environment setup, or database connections.

16. Q: What is test coverage?
    A: Test coverage measures how much of the code is executed by tests. Higher coverage usually indicates fewer untested paths.

17. Q: What is the assert statement in Python testing?
    A: assert checks if a condition is true and raises an AssertionError if it fails.

18. Q: How do you test exceptions in Python?
    A: Use pytest.raises() or unittest's assertRaises() to confirm that a function raises the expected exception.

19. Q: What is the role of configuration in testing?
    A: Configuration ensures the application uses the correct environment variables, test settings, and paths during automated testing.

20. Q: What is CI/CD and how does it relate to testing?
    A: CI/CD stands for Continuous Integration and Continuous Delivery/Deployment. Automated tests are often run in CI pipelines to check code quality before deployment.

End of interview questions.
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