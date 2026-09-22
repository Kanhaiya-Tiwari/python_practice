PHASE 16: REST / HTTP — INTERVIEW QUESTIONS (BASIC → ADVANCED)
===============================================================

BASIC

Q: What is a REST API?
A: REST (Representational State Transfer) is an architectural style for designing networked applications. A REST API exposes resources (URLs) that clients can interact with using standard HTTP methods (GET, POST, PUT, DELETE, etc.) and representations (commonly JSON).

Q: What is the difference between REST and HTTP?
A: HTTP is a protocol (transport) that defines methods, status codes, and headers. REST is an architectural style that uses HTTP (or other protocols) and prescribes constraints (statelessness, resource-based URLs, uniform interface) for designing APIs.

Q: Why is JSON commonly used with REST APIs?
A: JSON is lightweight, human-readable, language-agnostic, and easily parsed in clients and servers. It maps well to native data structures (objects, arrays) in most languages.

Q: What does the `requests` module do?
A: `requests` is a popular Python library for making HTTP requests simply (GET/POST/etc.), handling headers, sessions, timeouts, redirects, and responses (text/json/binary).

HTTP METHODS

Q: Difference between GET and POST?
A: GET retrieves data and should be idempotent and safe (no side effects). Parameters are usually in the URL/query. POST sends data to create resources or trigger operations and can have side effects.

Q: Difference between PUT and PATCH?
A: PUT replaces a resource entirely (idempotent). PATCH applies partial modifications to a resource (not necessarily idempotent, though it can be designed to be).

Q: When should you use DELETE?
A: Use DELETE to remove a resource. It should be idempotent: calling DELETE multiple times yields the same outcome (resource absent).

AUTHENTICATION

Q: What is a Bearer Token?
A: A Bearer Token is an access token (often a JWT) sent in the `Authorization: Bearer <token>` header. Possession of the token grants access (hence the need to store/transmit securely).

Q: Difference between API Key and Basic Authentication?
A: API Key: a single token (usually sent in header or query) used to identify/authorize a client. Basic Auth: sends base64-encoded `username:password` in `Authorization: Basic ...`. Basic is credentials-based; API keys are tokens and are usually easier to rotate and scope.

STATUS CODES

Q: What does 200 OK mean?
A: The request succeeded; response contains the requested data or confirmation.

Q: What is the difference between 401 and 403?
A: 401 Unauthorized: client is unauthenticated or invalid credentials (needs to authenticate). 403 Forbidden: client is authenticated but not authorized to access the resource.

Q: What does 404 indicate?
A: 404 Not Found: the requested resource/URL does not exist on the server.

Q: What is 500 Internal Server Error?
A: 500 indicates an unhandled error or server-side failure while processing the request.

ADVANCED

Q: What are REST principles?
A: Key REST constraints include: statelessness, client-server separation, uniform interface (resource-based URIs, standard methods), cacheability, layered system, and optionally HATEOAS (hypermedia links).

Q: Why is REST stateless?
A: Statelessness means each request contains all information needed to process it (no server-side session state). This improves scalability, reliability, and simplifies load balancing.

Q: How do you handle API timeouts and exceptions in Python?
A: - Use timeouts on network calls (e.g., `requests.get(url, timeout=(connect, read))`).
- Wrap calls in try/except to catch `requests.Timeout`, `requests.ConnectionError`, or generic exceptions.
- Use retries with backoff (e.g., `urllib3.util.retry` or `tenacity`) for transient errors.
- Fail gracefully and return meaningful error messages/status codes to callers.

Example (requests):
```
import requests
from requests.exceptions import Timeout, RequestException

try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    data = r.json()
except Timeout:
    # handle timeout
except RequestException as e:
    # handle other errors
```

Q: How would you secure an API request?
A: Practical measures:
- Use HTTPS/TLS to encrypt transport.
- Authenticate requests (Bearer tokens, API keys, OAuth2).
- Use short-lived tokens (rotate and revoke when needed).
- Validate and sanitize inputs; enforce minimal privileges (least privilege).
- Verify server certificates; avoid ignoring TLS verification.
- Use HMAC or signatures for high-security integrations (e.g., AWS-style signed requests).
- Rate-limit clients and add logging/monitoring and anomaly detection.
- Store credentials/tokens in environment variables or secure vaults (never in code).


---

File created: concise Phase 16 interview Q&A.

Status Codes
Statement

A status code tells whether the request succeeded or failed.

     2   xx Success
     Code	Meaning
200	OK
201	Created
204	No Content
         3xx Redirection
Code	Meaning
301	Permanent Redirect
302	Temporary Redirect
4xx Client Errors
            Code	Meaning
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
429	Too Many Requests
      5xx Server Errors
Code	Meaning
500	Internal Server Error
502	Bad Gateway
503	Service Unavailable