# 1. GET
# GET retrieves data from the server.÷
import requests

response = requests.get(
    "https://api.github.com"
)

print(response.status_code)
print(response.json())

# 2. POST

# POST creates a new resource on the server.

# Example
import requests

data = {
    "title":"Python",
    "body":"REST API"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.status_code)

# 3. PUT

# PUT replaces an existing resource completely.

import requests

data = {
    "title":"Updated Title",
    "body":"Updated Content"
}

requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=data
)

# 4. PATCH
#PATCH updates only specific fields.

import requests
data = {
    "title":"Only Title Changed"
}

requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=data
)

# 5. DELETE

# DELETE removes a resource.

import requests

response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print(response.status_code)

# Headers
# Statement

# Headers provide additional information about the request.

# Example 
headers = {
    "Content-Type":"application/json"
}
requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    headers=headers
)

# Authentication
# Authentication verifies the identity of the client.

import requests

requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    auth=("username","password")
)


# with help of Exception handling

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    print(response.json())

except requests.exceptions.RequestException as e:
    print("API Error:", e)


# Real DevOps Examples
# Check Website Health
import requests

response = requests.get(
    "https://example.com"
)

if response.status_code == 200:
    print("Website is Healthy")


# Get GitHub Repository Information
import requests

response = requests.get(
    "https://api.github.com/repos/octocat/Hello-World"
)

print(response.json()["name"])