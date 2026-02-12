file = open ("demo.txt")
print (file.read())
file.close()


#Concept: Read/write files
#DevOps Example: Read config file
with open("servers.txt") as f:
    servers = f.readlines()

print(servers)
#👉 Used for configs, logs, metadata