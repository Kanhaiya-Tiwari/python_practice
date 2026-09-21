# Phase 11 — JSON and YAML

This phase focuses on two important data formats used in Python and real-world applications:

- JSON (JavaScript Object Notation)
- YAML (YAML Ain't Markup Language)

## Files

- interview.txt: Interview questions and answers for JSON and YAML

## Topics Covered

- JSON syntax and structure
- YAML syntax and structure
- Difference between JSON and YAML
- Reading and writing JSON in Python
- Reading and writing YAML in Python
- When to use JSON vs YAML
- Parsing and serialization concepts

## Python Libraries

- JSON: built into Python using the json module
- YAML: use PyYAML with the yaml package

## Example

```python
import json

student = {"name": "Alice", "age": 25, "skills": ["Python", "SQL"]}
json_data = json.dumps(student)
print(json_data)
```

```python
import yaml

data = {"name": "Alice", "age": 25, "skills": ["Python", "SQL"]}
print(yaml.safe_dump(data, sort_keys=False))
```

## Use Cases

- JSON: APIs, web services, data exchange
- YAML: configuration files, CI/CD pipelines, Kubernetes manifests

## Reference

- JSON: https://www.json.org/json-en.html
- YAML: https://yaml.org/
- Python json module: https://docs.python.org/3/library/json.html
- PyYAML: https://pyyaml.org/
