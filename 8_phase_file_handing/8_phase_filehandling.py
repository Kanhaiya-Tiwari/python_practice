# File Handling Example with proper path handlin
file = open("/Users/kanha/DevOps/python-practice/python_practice/8_phase_file_handing/Interview.txt", "r")
content = file.readline()
print(content)
file.close()