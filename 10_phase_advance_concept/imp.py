# Practice Projects
# Read a large log file using a generator.
def log_generator(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()
# Create a list of running servers using a list comprehension.
running_servers = [server for server in servers if server.status == "running"]
# Combine server names and IP addresses with zip().
server_names = ["server1", "server2", "server3"]
ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
combined = list(zip(server_names, ip_addresses))
# Number backup files with enumerate().
backup_files = ["backup1.txt", "backup2.txt", "backup3.txt"]
numbered_backups = [(i, filename) for i, filename in enumerate(backup_files)]
# Filter only failed deployments using filter().
failed_deployments = list(filter(lambda x: x.status == "failed", deployments))
# Convert CPU values to percentage strings using map().
cpu_values = [80, 90, 75]
percentages = list(map(lambda x: f"{x}%", cpu_values))
# Write a simple logging decorator that prints when a function starts and finishes.
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper
# Use a context manager (with) to safely read and write configuration files.
with open("config.txt", "r") as f:
    config = f.read()
with open("config.txt", "w") as f:
    f.write(config)