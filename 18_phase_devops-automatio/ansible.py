# Ansible Automation
# Generate Inventory
servers = [
    "web01",
    "web02",
    "web03"
]

with open("inventory.ini","w") as file:

    file.write("[web]\n")

    for server in servers:

        file.write(server+"\n")

# Execute Playbooks

import subprocess

subprocess.run(
    [
        "ansible-playbook",
        "-i",
        "inventory.ini",
        "deploy.yml"
    ],
    check=True
)