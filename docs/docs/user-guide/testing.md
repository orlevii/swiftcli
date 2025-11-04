# Testing

Clantic makes it easy to test your CLI applications by allowing direct instantiation and execution of commands.

## Basic Testing

Test a command by creating an instance and calling `run()`:

## Testing with pytest

Example using pytest for testing a CLI command:

```python
import pytest
from my_cli.commands import GreetCommand


def test_greet_command():
    # Create and run command
    cmd = GreetCommand(name="Alice")
    cmd.run()
```
