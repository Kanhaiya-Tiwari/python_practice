# Phase 16 — REST API with Python

This phase focuses on building and consuming APIs using Python. The goal is to understand HTTP methods, request/response handling, authentication, and how to connect backend services with client applications.

## Topics

- REST fundamentals
- HTTP methods: GET, POST, PUT, DELETE
- JSON payloads
- Request and response handling
- Status codes and error handling
- API authentication and tokens
- Flask and FastAPI basics
- Testing REST endpoints

## Key Concepts

- A REST API exposes resources through predictable endpoints.
- Clients send HTTP requests and receive JSON responses.
- Proper validation and error handling are essential for production APIs.
- Authentication, rate limiting, and logging protect services.

## Common Questions

- What is REST?
- What is the difference between PUT and PATCH?
- How do you send JSON in Python requests?
- How do you handle API errors and retries?
- What is authentication token-based security?

## Example

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
response.raise_for_status()
print(response.json())
```

## Best Practices

- Use meaningful endpoint names
- Validate request and response data
- Return proper status codes
- Keep APIs secure and documented
- Log important API events

## Resources

- Python `requests` documentation
- FastAPI documentation
- REST API design best practices
