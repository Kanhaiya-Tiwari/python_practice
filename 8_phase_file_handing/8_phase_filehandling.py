# File Handling Example with proper path handlin
file = open("/Users/kanha/DevOps/python-practice/python_practice/8_phase_file_handing/Interview.txt", "r")
content = file.readline()
print(content)
file.close()
# Practice Programs
# Create a file named student.txt and write your name and age.
open("student.txt", "w").write("Kanhaiya Tiwari, 25")
# Read the contents of student.txt.
with open("student.txt", "r") as f:
    print(f.read()) 
# Append your city to the file.
with open("student.txt", "a") as f:
    f.write(",\n New York")
# Count the number of lines in a file.
with open("student.txt", "r") as f:
    lines = f.readlines()
    print(f"Number of lines: {len(lines)}")
# Copy a text file into another file.
with open("student.txt", "r") as source:
    with open("student_copy.txt", "w") as dest:
        dest.write(source.read())
# Copy an image using binary mode.
with open("image.jpg", "rb") as source:
    with open("image_copy.jpg", "wb") as dest:
        dest.write(source.read())
# Read a server list from servers.txt and print each server.
with open("servers.txt", "r") as f:
    for line in f:
        print(line.strip())
# Generate a timestamped backup log.


with open("backup.log", "a") as f:
    f.write(f"{datetime.datetime.now()}: Backup completed\n")

# Handle the case where a file does not exist using try and except.
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
# Read a large log file line by line using a for loop.
with open("large_log.txt", "r") as f:
    for line in f:
        print(line.strip())