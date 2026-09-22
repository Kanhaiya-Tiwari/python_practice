# Phase 18 - DevOps Automation with Python

This phase focuses on automating Linux system administration, cloud operations, container management, CI/CD, infrastructure provisioning, and DevOps workflows using Python.

## Topics Covered

- Linux automation with Python
- User and file management
- Backup and log rotation
- Cron jobs and scheduling
- SSH automation with Paramiko
- Docker automation using Docker SDK
- Kubernetes orchestration using Python client
- AWS automation with boto3
- Terraform automation
- Jenkins automation
- Git automation with GitPython
- Ansible automation and inventory management

## Key Skills

- Executing shell commands from Python
- Creating users and managing system files
- Automating backups and log cleanup
- Managing remote servers securely with SSH
- Building and controlling containers programmatically
- Interacting with Kubernetes clusters and resources
- Provisioning and monitoring AWS services
- Using Infrastructure as Code with Terraform
- Triggering Jenkins jobs and fetching build status
- Handling repositories using GitPython
- Running Ansible playbooks through Python scripts

## Common Tools

- Python standard libraries: os, shutil, subprocess, logging, pathlib
- Paramiko
- Docker SDK for Python
- Kubernetes Python client
- boto3
- Terraform
- Jenkins REST API
- GitPython
- Ansible

## Best Practices

- Use secure authentication and avoid hardcoded secrets
- Validate command output before proceeding
- Handle errors and logging properly
- Use automation for repeatable and scalable workflows
- Keep infrastructure declarative when possible

## Example

```python
import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```

## Learning Goals

By the end of this phase, you should be able to:

- Automate Linux tasks using Python
- Integrate with cloud and container platforms
- Manage DevOps workflows programmatically
- Build scripts for deployment and infrastructure automation
- Work efficiently with CI/CD, Git, and automation tools
