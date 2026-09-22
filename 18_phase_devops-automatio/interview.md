# Phase 18 - DevOps Automation Interview Questions and Answers

## Basic

### 1. What is Linux automation?
Answer: Linux automation is the process of using scripts and tools to automate repetitive system tasks such as file management, service restarts, user creation, backups, and deployments.

### 2. Why do DevOps engineers automate Linux tasks?
Answer: Automation reduces manual effort, improves consistency, saves time, reduces human errors, and makes deployments and infrastructure operations more reliable.

### 3. Which Python module is commonly used to execute Linux commands?
Answer: The subprocess module is commonly used to execute Linux commands from Python scripts.

## User Creation

### 4. How can you create a Linux user using Python?
Answer: You can use the subprocess module to run shell commands such as useradd username or call system administration tools through Python.

Example:
```python
import subprocess

subprocess.run(['sudo', 'useradd', 'devuser'], check=True)
```

### 5. Why is bulk user creation useful?
Answer: Bulk user creation is useful when setting up multiple users for a team, classroom, lab, or environment. It saves time and keeps user creation consistent.

## Backup

### 6. How do you create a backup script in Python?
Answer: You can write a Python script that copies or archives files and directories to a backup location using the shutil module or tar command.

Example:
```python
import shutil

shutil.copy2('/var/log/app.log', '/backup/app.log.bak')
```

### 7. What is the difference between copy() and copytree() in shutil?
Answer: copy() copies a single file, while copytree() copies an entire directory tree including nested files and folders.

## Log Rotation

### 8. Why is log rotation important?
Answer: Log rotation prevents log files from growing endlessly, saves disk space, and helps manage old logs in a structured way.

### 9. How would you delete log files older than 30 days?
Answer: Use Python with os, time, and datetime to check file modification times and delete files older than 30 days.

Example:
```python
import os
from datetime import datetime, timedelta

cutoff = datetime.now() - timedelta(days=30)
for filename in os.listdir('/var/log'):
    full_path = os.path.join('/var/log', filename)
    if os.path.isfile(full_path):
        mod_time = datetime.fromtimestamp(os.path.getmtime(full_path))
        if mod_time < cutoff:
            os.remove(full_path)
```

## Cron

### 10. What is cron?
Answer: Cron is a Linux utility used to schedule commands or scripts to run automatically at specified times.

### 11. How do you schedule a Python script to run daily?
Answer: Add a cron entry in the crontab file with the desired schedule and the Python interpreter path.

Example:
```bash
0 2 * * * /usr/bin/python3 /opt/scripts/daily_job.py
```

### 12. What is the purpose of crontab -e?
Answer: crontab -e opens the current user's cron table for editing scheduled jobs.

## SSH

### 13. What is Paramiko?
Answer: Paramiko is a Python library used to connect to remote systems over SSH and execute commands securely.

### 14. How do you execute a remote Linux command using Python?
Answer: Use Paramiko to create an SSH client, connect to the remote host, and run commands with exec_command().

Example:
```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.10', username='ubuntu', password='secret')
stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.read().decode())
ssh.close()
```

### 15. Why is SSH automation important in DevOps?
Answer: SSH automation helps manage remote servers, deploy applications, run health checks, configure systems, and perform patching without manual access.

## Docker

### 16. What is the Docker SDK?
Answer: The Docker SDK for Python allows Python applications to interact with the Docker Engine programmatically.

### 17. Why use Docker SDK instead of Docker CLI?
Answer: Docker SDK is useful when Python applications need to automate container operations inside code, integrate with pipelines, or build custom orchestration logic.

### 18. How do you build an image using Python?
Answer: Use the Docker SDK client to build an image from a Dockerfile or build context.

Example:
```python
import docker

client = docker.from_env()
image = client.images.build(path='.', tag='myapp:latest')
print(image)
```

### 19. How do you start or stop a container programmatically?
Answer: Use Docker SDK methods like client.containers.run(), start(), stop(), and remove().

### 20. How do you inspect a running container?
Answer: Use client.containers.get(container_id) and inspect its attributes such as status, ports, and mounts.

### 21. How would you restart unhealthy containers automatically?
Answer: Use monitoring and automation logic to check container health status and call container.restart() when the container is unhealthy.

## Kubernetes

### 22. What is the Kubernetes Python Client?
Answer: The Kubernetes Python client is a library that allows Python scripts to interact with Kubernetes clusters using the Kubernetes API.

### 23. How do you connect to a Kubernetes cluster?
Answer: You configure a Kubernetes API client using a kubeconfig file or service account token from the cluster environment.

### 24. What is the difference between a Pod and a Deployment?
Answer: A Pod is the smallest deployable unit, while a Deployment manages Pods and ensures the desired number of replicas are running.

### 25. What is a Service?
Answer: A Service provides stable network access to a set of Pods and acts as a load balancer or endpoint abstraction.

### 26. What is the difference between a ConfigMap and a Secret?
Answer: A ConfigMap stores non-sensitive configuration data, while a Secret stores sensitive data such as passwords, tokens, or keys.

### 27. Why should secrets not be hardcoded in applications?
Answer: Hardcoded secrets can be exposed in source code, logs, or version control, causing security vulnerabilities and compliance issues.

### 28. How do you list Pods using Python?
Answer: Use the Kubernetes Python client and call the CoreV1Api().list_pod_for_all_namespaces() method.

Example:
```python
from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()
for pod in v1.list_pod_for_all_namespaces().items:
    print(pod.metadata.name)
```

## AWS - boto3

### 29. What is boto3?
Answer: boto3 is the AWS SDK for Python used to interact with Amazon services such as EC2, S3, IAM, Lambda, and CloudWatch.

### 30. What is the difference between a boto3 client and a resource?
Answer: A client is a low-level service interface, while a resource is a higher-level object-oriented interface that wraps multiple service operations.

## EC2

### 31. How do you start and stop an EC2 instance using Python?
Answer: Use boto3 EC2 client methods like start_instances() and stop_instances() with the instance ID.

### 32. Why would you automate EC2 management?
Answer: Automation helps scale infrastructure, manage cost, reduce manual operations, and respond to workload changes quickly.

## S3

### 33. How do you upload a file to S3?
Answer: Use boto3.client('s3').upload_file() or boto3.resource('s3').Bucket(...).upload_file().

### 34. What are common S3 use cases in DevOps?
Answer: S3 is used for storing logs, backups, deployment artifacts, static websites, and data lakes.

## IAM

### 35. Why is IAM important?
Answer: IAM controls access to AWS resources and ensures users and services only receive the permissions they need.

### 36. How do you create an IAM user using boto3?
Answer: Use boto3.client('iam').create_user(UserName='new-user').

## Lambda

### 37. What is AWS Lambda?
Answer: Lambda is a serverless compute service that runs code in response to events without managing servers.

### 38. When would you use Lambda instead of EC2?
Answer: Use Lambda for event-driven workloads, lightweight tasks, APIs, automation scripts, and workloads that need quick scaling without server management.

## CloudWatch

### 39. What is CloudWatch used for?
Answer: CloudWatch is used for monitoring AWS resources, logs, metrics, alarms, and automated notifications.

### 40. How do you monitor EC2 CPU utilization?
Answer: Use CloudWatch metrics such as CPUUtilization on the EC2 instance and set alarms when thresholds are crossed.

## EKS

### 41. What is Amazon EKS?
Answer: Amazon EKS is a managed Kubernetes service that helps run Kubernetes clusters on AWS without managing the control plane.

### 42. How do you list EKS clusters using boto3?
Answer: Use boto3.client('eks').list_clusters().

## RDS

### 43. Why are database snapshots important?
Answer: Database snapshots help with backup, disaster recovery, restore testing, and point-in-time recovery planning.

### 44. How do you list RDS instances?
Answer: Use boto3.client('rds').describe_db_instances().

## Terraform

### 45. What is Terraform?
Answer: Terraform is an Infrastructure as Code tool used to define, provision, and manage infrastructure resources across providers.

### 46. Why do we use Infrastructure as Code?
Answer: IaC makes infrastructure repeatable, version-controlled, automated, and easier to manage across environments.

### 47. How do you execute Terraform using Python?
Answer: Use Python subprocess to run terraform init, plan, apply, and destroy commands.

Example:
```python
import subprocess

subprocess.run(['terraform', 'init'], check=True)
subprocess.run(['terraform', 'apply', '-auto-approve'], check=True)
```

### 48. What is the purpose of terraform.tfstate?
Answer: terraform.tfstate stores the current state of the infrastructure managed by Terraform and helps track resource mappings and drift.

### 49. Why would you generate a terraform.tfvars file programmatically?
Answer: It allows automation to create environment-specific configuration values dynamically and keeps secret or variable management consistent.

## Jenkins

### 50. What is the Jenkins REST API?
Answer: The Jenkins REST API allows external tools and scripts to interact with Jenkins jobs, builds, nodes, and system information over HTTP.

### 51. How do you trigger a Jenkins job using Python?
Answer: Use requests to call the Jenkins job URL with authentication and trigger the build.

### 52. How do you authenticate with Jenkins?
Answer: Use a username and API token or Jenkins credentials in the HTTP request headers.

### 53. How do you check the status of a Jenkins build?
Answer: Query the Jenkins build API and inspect the result or status fields returned in JSON.

### 54. How do you download Jenkins console logs?
Answer: Call the Jenkins build console log endpoint using requests and write the output to a file or print it.

## Git

### 55. What is GitPython?
Answer: GitPython is a Python library that allows scripts to interact with Git repositories programmatically.

### 56. Why use GitPython instead of Git CLI?
Answer: GitPython is useful when Python applications need to automate Git operations without shelling out to the CLI.

### 57. How do you clone a repository using Python?
Answer: Use GitPython Repo.clone_from() to clone a remote repository.

### 58. How do you commit and push changes?
Answer: Use GitPython to stage files, create a commit, and then push to the configured remote.

### 59. How do you pull the latest changes?
Answer: Use Repo.remotes.origin.pull() or a similar GitPython method.

## Ansible

### 60. What is an Ansible inventory?
Answer: An Ansible inventory is a file or dynamic source that defines the hosts and groups managed by Ansible.

### 61. How do you generate an inventory file using Python?
Answer: Write a Python script that creates a file with host and group definitions in INI or YAML format.

### 62. How do you execute an Ansible playbook from Python?
Answer: Use subprocess to run ansible-playbook with the playbook file and inventory path.

### 63. Why is dynamic inventory useful?
Answer: Dynamic inventory automatically discovers hosts from cloud or infrastructure systems, keeping inventory up to date without manual maintenance.

### 64. What is the difference between a playbook and an inventory?
Answer: A playbook defines the tasks to run on hosts, while an inventory defines which hosts or groups the playbook should target.

## Summary

DevOps automation with Python combines system administration, cloud operations, containers, and deployment automation. By mastering Python scripting with tools like Linux shell commands, Paramiko, Docker SDK, boto3, Kubernetes client, Terraform, Jenkins, GitPython, and Ansible, engineers can automate large parts of modern infrastructure workflows.
