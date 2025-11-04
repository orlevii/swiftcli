# Clantic

Build testable CLI apps with `click` and `pydantic`

Clantic makes it easy to define CLI parameters with `pydantic` BaseModels, combining the power of `click` with `pydantic`'s data validation.

## Key Features

- Define CLI parameters using pydantic models
- Type validation and conversion out of the box
- Support for arguments, options, flags and switches
- Easy to test CLI applications

## Quick Example

```python
from pydantic import BaseModel
from clantic import BaseCommand, Group
from clantic.types import Argument, Option


class GreetParams(BaseModel):
    name: Argument[str]  # required argument
    color: Option[str] = ""  # Optional --color option with default value


class GreetCommand(BaseCommand[GreetParams]):
    NAME = "greet"

    def run(self) -> None:
        if self.params.color:
            print(f"Hello, {self.params.name}. You like the color {self.params.color}.")
        else:
            print(f"Hello, {self.params.name}.")


cli = Group()
cli.add_command_cls(GreetCommand)

if __name__ == "__main__":
    cli()
```

## Installation

```bash
pip install swiftcli
```
