#Working with JSON
#Concept: Parse structured data
#DevOps Example: API response
import json

data = '{"cpu": 72, "memory": 65}'
parsed = json.loads(data)

print(parsed["cpu"])
#👉 Used in cloud/API automation