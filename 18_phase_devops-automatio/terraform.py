# Execute Terraform
import subprocess

subprocess.run(["terraform", "init"], check=True)

subprocess.run(["terraform", "plan"], check=True)

subprocess.run(["terraform", "apply", "-auto-approve"], check=True)

# Destroy Infrastructure
import subprocess

subprocess.run([
    "terraform",
    "destroy",
    "-auto-approve"
])

# Parse Terraform State
import json

with open("terraform.tfstate") as file:
    state = json.load(file)

print(state["resources"])

# Generate Variables
variables = """
instance_type = "t3.micro"
region = "ap-south-1"
"""

with open("terraform.tfvars","w") as file:

    file.write(variables)