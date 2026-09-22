# Kubernetes Automation

# Python communicates with Kubernetes using the Kubernetes Python Client.

# Load Cluster Configuration
from kubernetes import config

config.load_kube_config()

# inside Kubernetes Pod

config.load_incluster_config()
# Create API Client
from kubernetes import client

v1 = client.CoreV1Api()

# Kubernetes Python Client
# Statement

# The Kubernetes Python Client communicates with the Kubernetes API Server.

pods = v1.list_pod_for_all_namespaces()

for pod in pods.items:

    print(pod.metadata.name)

# Create Pod
# Statement

# Python can create Pods.

from kubernetes import client

pod = client.V1Pod(
    metadata=client.V1ObjectMeta(name="nginx"),
    spec=client.V1PodSpec(
        containers=[
            client.V1Container(
                name="nginx",
                image="nginx"
            )
        ]
    )
)

v1.create_namespaced_pod(
    namespace="default",
    body=pod
)
