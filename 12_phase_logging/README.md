# Phase 12 — Logging

This phase covers the Python `logging` module and how it is used for application monitoring and debugging.

## Topics

- Log levels
- Logger objects
- Formatter configuration
- File and console handlers
- Rotating logs
- Real-world application logging

## Files

- `interview.txt` — interview Q&A
- `logging_example.py` — practical logging example

## Example

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

logging.info('Application started')
logging.warning('Something needs attention')
logging.error('An error occurred')
```

## Common Log Levels

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

## Best Practices

- Log meaningful messages
- Do not log secrets or passwords
- Use proper log levels
- Rotate log files in production
- Keep messages clear and useful

## References

- Python logging docs: https://docs.python.org/3/library/logging.html
