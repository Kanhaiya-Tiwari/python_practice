#Environment Variables
#Concept: Store secrets/configs safely
#DevOps Example: API token
import os

token = os.getenv("API_TOKEN")
print(token)
#👉 Used for credentials