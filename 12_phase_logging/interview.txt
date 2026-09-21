Phase 12 — Logging Interview Questions and Answers

Basic

Q: What is logging in Python?
A: Logging is a built-in module used to record events, messages, errors, and application behavior while a program runs.

Q: Why do we use logging instead of print()?
A: Logging is more flexible, supports severity levels, can write to files, and is easier to manage in production applications.

Q: What are the common log levels?
A: DEBUG, INFO, WARNING, ERROR, and CRITICAL. They indicate the severity of a message.

Q: What is the default logging level?
A: The default level is WARNING, which means only warnings and above are shown unless configured differently.

Q: What is a logger?
A: A logger is the main object used in Python logging to emit messages.

Intermediate

Q: What is a formatter?
A: A formatter controls the final structure of a log message, such as time, log level, and message content.

Q: What is a file handler?
A: A file handler writes log messages to a file instead of the console.

Q: What is a stream handler?
A: A stream handler sends logs to an output stream such as stdout or stderr.

Q: What is a rotating log file?
A: A rotating log file automatically creates new log files once a file reaches a specified size or age.

Q: What is the purpose of `logging.basicConfig()`?
A: It configures the root logger with a basic format and output destination.

Advanced

Q: Why is logging important in enterprise applications?
A: It helps in debugging, auditing, monitoring, troubleshooting, and tracking system health over time.

Q: What is the difference between logging and exception handling?
A: Exception handling reacts to errors in code; logging records events, including errors, for debugging and monitoring.

Q: How do you log to a file?
A: Use `logging.FileHandler()` with a logger or `basicConfig(filename='app.log')`.

Q: How do you rotate logs in Python?
A: Use `RotatingFileHandler` or `TimedRotatingFileHandler` from the logging module.

Q: What is a logger hierarchy?
A: Loggers have a parent-child structure. Child loggers inherit configuration from parent loggers unless overridden.

End of Phase 12 interview notes.
