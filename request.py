#Concept: Call APIs
#DevOps Example: Check website health
import requests

response = requests.get("https://example.com")

if response.status_code == 200:
    print("✅ Site is UP")
else:
    print("❌ Site DOWN")
#👉 Used in monitoring & integrations