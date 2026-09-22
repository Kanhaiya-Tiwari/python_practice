# Jenkins Automation
# trigger a Jenkins Job
# Python can trigger Jenkins jobs through the REST API.

import requests

url = "http://jenkins.example.com/job/myapp/build"

response = requests.post(
    url,
    auth=("username","api_token")
)

print(response.status_code)

# Check Build Status
import requests

url = "http://jenkins.example.com/job/myapp/lastBuild/api/json"

response = requests.get(
    url,
    auth=("username","api_token")
)

print(response.json()["result"])

# Download Console Logs
# Python can retrieve Jenkins console output for troubleshooting.
import requests

url = "http://jenkins.example.com/job/myapp/lastBuild/consoleText"

response = requests.get(
    url,
    auth=("username","api_token")
)
print(response.text)

# Trigger Build with Parameters
import requests

requests.post(
    "http://jenkins.example.com/job/deploy/buildWithParameters",
    auth=("username","api_token"),
    data={
        "Environment":"Production",
        "Version":"v2.1"
    }
)
