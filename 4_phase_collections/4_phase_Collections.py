
# Practice Tasks
# Create a list of 5 programming languages and print the third language.
languages = ["Python", "Jave", "C++", "C#", "C"]
print (languages[2])
# Add two new languages using append() and extend().
languages.append("JavaScript")
languages.extend(["Go", "Rust"])
print(languages)
# Remove one language using remove().
languages.remove("C")
print(languages)
# Sort the list in ascending and descending order.
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)

# Create a tuple containing your name, age, and city, then unpack it into variables.
person = ("Kanha, 22, Delhi")
name, age, city = person.split(", ")
print(age)
print(name)
print(city)
# Create a dictionary for a server with hostname, ip, and status, then update its status.
server = {"hostname": "server1", "ip": "192.168.1.1", "status": "running"}
print(server)
server["status"] = "maintenance"
print (server)
# Create two sets of server names and find their union, intersection, difference, and symmetric_difference.
servers1 = {"server1", "server2", "server3"}
servers2 = {"server2", "server3", "server4"}
print(servers1.union(servers2))
print(servers1.intersection(servers2))
print(servers1.difference(servers2))
print(servers1.symmetric_difference(servers2))