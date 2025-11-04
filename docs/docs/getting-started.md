# Getting Started

## Installation

Install Clantic using pip:

```bash
pip install clantic
```

## Basic Usage

### 1. Define Parameters

First, define your command parameters using a Pydantic model:

```python
from pydantic import BaseModel
from clantic.types import Argument, Option

class GreetParams(BaseModel):
    name: Argument[str]  # required argument
    greeting: Option[str] = "Hello"  # optional with default
```

### 2. Create Command

Create a command by inheriting from `BaseCommand`:

```python
from clantic import BaseCommand

class GreetCommand(BaseCommand[GreetParams]):
    NAME = "greet"
    
    def run(self) -> None:
        print(f"{self.params.greeting}, {self.params.name}!")
```

### 3. Create CLI Group

Group your commands and create the CLI:

```python
from clantic import Group

cli = Group()
cli.add_command_cls(GreetCommand)

if __name__ == "__main__":
    cli()
```

### 4. Run the CLI

Your CLI is now ready to use:

```bash
$ python my_cli.py greet --name Alice --greeting Hi
Hi, Alice!
```

## Next Steps

- Learn about different [Parameter Types](user-guide/parameter-types.md)
- Explore [Command Configuration](user-guide/command-configuration.md)
- See how to [Test Your CLI](user-guide/testing.md) 