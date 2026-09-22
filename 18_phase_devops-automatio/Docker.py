import docker

client = docker.from_env()

containers = client.containers.list()

for container in containers:
    print(container.name)

# Connet to docker 

import docker

client = docker.from_env()

print(client.version())

# Build Docker Images
import docker

client = docker.from_env()

client.images.build(
    path=".",
    tag="myapp:v1"
)

print("Image Built Successfully")

# Run Containers
import docker

client = docker.from_env()

container = client.containers.run(
    "nginx",
    detach=True,
    ports={"80/tcp":8080},
    name="webserver"
)

print(container.id)

# Stop Container
container.stop()
# Restart Container
container.restart()
# Remove Container
container.remove()

# Inspect Containers
container = client.containers.get("webserver")

print(container.status)

# DevOps Example

# Health Monitoring

for container in client.containers.list():

    print(container.name)

    print(container.status)

# Restart Unhealthy Containers
for container in client.containers.list():

    if container.status != "running":

        container.restart()

# Pull Image
client.images.pull("nginx")
# List Images
for image in client.images.list():

    print(image.tags)