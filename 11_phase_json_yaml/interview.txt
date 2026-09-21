Phase 11 — JSON and YAML Interview Questions and Answers

Basic

Q: What is JSON?
A: JSON (JavaScript Object Notation) is a lightweight data interchange format that stores data as key-value pairs and arrays. It is easy to read, write, and parse in Python and many other languages.

Q: What is YAML?
A: YAML (YAML Ain't Markup Language) is a human-readable data serialization format commonly used for configuration files. It uses indentation instead of braces and brackets, which makes it cleaner for configuration.

Q: What is the difference between JSON and YAML?
A: JSON is stricter and uses double quotes around keys and string values. YAML is more readable and flexible, supports comments, and uses indentation to define structure. JSON is commonly used in APIs; YAML is commonly used in configuration files.

Q: Is JSON valid Python syntax?
A: Not exactly. JSON is similar to Python dictionaries and lists, but there are key differences such as JSON requiring double quotes around strings and using null, true, false instead of Python's None, True, False.

Q: Why is YAML popular for configuration?
A: YAML is easy for humans to read and write, supports comments, nested data structures, and often reduces boilerplate compared to JSON.

Q: What is parsing?
A: Parsing is the process of converting a text format like JSON or YAML into a native Python object such as a dictionary, list, string, or number.

Q: What is serialization?
A: Serialization is the process of converting a Python object into a string or file format like JSON or YAML so it can be stored or transferred.

Intermediate

Q: What is a JSON object?
A: A JSON object is a collection of key-value pairs enclosed in curly braces. Example: {"name": "Alice", "age": 25}.

Q: What is a JSON array?
A: A JSON array is a list of values enclosed in square brackets. Example: ["apple", "banana", "mango"].

Q: What is a YAML list?
A: A YAML list is represented as a sequence with hyphen markers. Example:
  - apple
  - banana
  - mango

Q: What is a YAML dictionary?
A: A YAML dictionary is a key-value mapping written using a colon. Example:
  name: Alice
  age: 25

Q: How do you read JSON in Python?
A: Use the json module. Example: json.loads() to parse a string, or json.load() to read from a file.

Q: How do you write JSON in Python?
A: Use json.dumps() to convert Python objects to a JSON string or json.dump() to write to a file.

Q: How do you read YAML in Python?
A: Use a library such as PyYAML. Example: yaml.safe_load() reads YAML content and converts it to Python data structures.

Q: How do you write YAML in Python?
A: Use yaml.safe_dump() from the PyYAML library to convert Python objects into YAML format.

Q: Why is indentation important in YAML?
A: YAML uses indentation to define nesting. Incorrect indentation can change the structure or cause parsing errors.

Q: What is a JSON schema?
A: A JSON schema defines the expected structure of JSON data, including field names, types, and validation rules.

Advanced

Q: What are the advantages of JSON?
A: JSON is lightweight, language-independent, easy to parse, widely supported, and commonly used in APIs and web services.

Q: What are the advantages of YAML?
A: YAML is more readable for humans, easier to maintain for configuration files, and supports comments and nested structures with cleaner formatting.

Q: When should you use JSON instead of YAML?
A: Use JSON when you need strict, machine-friendly data exchange, especially in APIs, database payloads, and frontend-backend communication.

Q: When should you use YAML instead of JSON?
A: Use YAML for configuration files, deployment manifests, and developer-friendly settings where readability matters more than strict formatting.

Q: What is a nested JSON structure?
A: A nested JSON structure contains objects or arrays inside other objects or arrays, such as a user with address and hobbies.

Q: Can YAML represent the same data as JSON?
A: Yes. YAML is a superset of JSON in many cases. JSON is a subset of YAML in terms of data representation, but YAML has more human-friendly syntax.

Q: What happens if YAML indentation is wrong?
A: YAML may raise a parsing error or create a completely different data structure, because indentation defines hierarchy.

Q: What is safe_load() in PyYAML?
A: safe_load() reads YAML content safely and converts it into Python objects without executing arbitrary code. It is recommended for normal use.

Q: Why do APIs prefer JSON?
A: JSON is standardized, compact, easy to parse, and supported across all major programming languages and frameworks.

Q: What is the difference between a JSON string and a Python string?
A: Both are text, but JSON strings must be stored in double quotes and are used as a data format. Python strings are native runtime objects in Python code.

Q: How do you convert a Python dict to JSON?
A: Use json.dumps(my_dict). This returns a JSON string.

Q: How do you convert JSON to Python dict?
A: Use json.loads(json_string). This returns a Python dictionary.

Q: Which is better for configuration: JSON or YAML?
A: YAML is often easier for people to manage manually, while JSON is stricter and better for machine-to-machine data exchange. The best choice depends on the use case.

End of Phase 11 interview notes.
