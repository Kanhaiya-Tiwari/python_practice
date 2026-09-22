Phase 13 — OS Automation Interview Questions and Answers

Basic

Q: What is OS automation?
A: OS automation means using Python to automate system-level tasks such as file operations, environment checks, command execution, and process management.

Q: What is the os module?
A: The os module provides a way to interact with the operating system, including file and directory operations, environment variables, and command execution support.

Q: What is the pathlib module?
A: pathlib is an object-oriented way to work with file paths in Python. It makes file and folder operations easier to read and use.

Q: What is shutil used for?
A: shutil provides high-level file operations such as copying, moving, renaming, and removing files or directories.

Q: What is subprocess used for?
A: subprocess allows Python to run shell commands, launch external programs, and capture their output.

Intermediate

Q: How do you copy a file in Python?
A: Use shutil.copy() or shutil.copy2() from the shutil module.

Q: How do you rename a file?
A: Use os.rename() or pathlib.Path.rename().

Q: How do you delete a file?
A: Use os.remove() to delete a file or shutil.rmtree() for directories.

Q: How do you execute a shell command from Python?
A: Use subprocess.run() or subprocess.Popen() and pass the command as a list or string.

Q: How do you check environment variables?
A: Use os.environ or os.getenv("VARIABLE_NAME").

Q: How do you check disk usage?
A: Use shutil.disk_usage(path) to get total, used, and free space information.

Advanced

Q: Why is OS automation useful in DevOps?
A: It helps automate repeated system tasks, reduces manual effort, improves reliability, and supports deployment, monitoring, and maintenance workflows.

Q: What is the difference between os and pathlib?
A: os works with strings and is traditional; pathlib uses cleaner object-oriented path handling and is often easier to read.

Q: Why should we use subprocess carefully?
A: External commands can be security-sensitive and can behave differently across operating systems. Input should be validated and commands should be well controlled.

Q: What is the benefit of using shutil for file operations?
A: It abstracts common file tasks like copy, move, and removal and is easier to use than manually handling lower-level file APIs.

Q: What are common OS automation tasks?
A: Copying files, renaming logs, deleting temporary files, running scripts, checking disk capacity, and reading environment configuration.

End of Phase 13 interview notes.
