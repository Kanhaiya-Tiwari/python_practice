#Concept: Run shell commands
#DevOps Example: Get disk usage
import subprocess

result = subprocess.run(["df", "-h"], capture_output=True, text=True)
print(result.stdout)
#👉 Used for:
#Running kubectl
#Running docker
#Running terraform */
result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
print(result.stdout)
result = subprocess.run(["terraform", "plan"], capture_output=True, text=True)
print(result.stdout)