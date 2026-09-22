# Phase 19 — Testing and Configuration

This phase focuses on writing reliable code, validating behavior, and managing configuration safely. It covers unit tests, automation, environment variables, and production-ready deployment configuration.

## Topics

- Unit testing
- Test frameworks such as `pytest` and `unittest`
- Test-driven development (TDD)
- Mocking and assertions
- Environment variables
- YAML, JSON, and config files
- CI/CD basics
- Deployment readiness

## Key Concepts

- Tests help catch issues before production.
- Configuration should be externalized and environment based.
- Automation reduces manual errors and improves reliability.
- Good test coverage supports maintainable software.

## Example

```python
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
```

## Best Practices

- Write small, focused tests
- Keep configuration outside source code
- Avoid hard-coded secrets
- Use CI pipelines for validation
- Test both success and failure paths

## Resources

- Pytest documentation
- Python unittest module
- 12-factor app principles
