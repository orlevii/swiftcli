# Command Configuration

## Basic Configuration

Commands can be configured using the `CONFIG` class variable:

```python
class MyCommand(BaseCommand[MyParams]):
    NAME = "mycommand"
    CONFIG = {
        "help": "My command help text",
        "short_help": "Short help",
        "epilog": "Additional help text at the bottom",
        "hidden": False,
        "deprecated": False,
    }
```

## Configuration Options

| Option | Type | Description |
|--------|------|-------------|
| `help` | `str` | Detailed help text for the command |
| `short_help` | `str` | Short help shown in command listings |
| `epilog` | `str` | Text shown after the help message |
| `hidden` | `bool` | Hide command from help listings |
| `deprecated` | `bool` | Mark command as deprecated |
| `context_settings` | `dict` | Click context settings |

## Command Groups

Group multiple commands together:

```python
from clantic import Group

cli = Group()
cli.add_command_cls(CommandOne)
cli.add_command_cls(CommandTwo)

if __name__ == "__main__":
    cli()
``` 