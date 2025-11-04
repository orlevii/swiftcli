# Parameter Types

Clantic supports several parameter types through the `clantic.types` module.

## Arguments

Arguments are required positional parameters:

```python
from pydantic import BaseModel
from clantic.types import Argument

class MyParams(BaseModel):
    filename: Argument[str]  # Required positional argument
```

## Options

Options are named parameters that can have default values:

```python
from swiftcli.types import Option

class MyParams(BaseModel):
    output: Option[str] = "output.txt"  # --output option with default
    count: Option[int] = 1  # --count option with default
```

## Flags

Flags are boolean options that can be enabled:

```python
from swiftcli.types import Flag

class MyParams(BaseModel):
    verbose: Flag  # --verbose flag, defaults to False
```

## Switches

Switches create multiple mutually exclusive flags from an Enum:

```python
from enum import Enum
from swiftcli.types import Switch

class LogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info" 
    ERROR = "error"

class MyParams(BaseModel):
    log_level: Switch[LogLevel] = LogLevel.INFO  # Creates --debug, --info, --error flags
```

## Advanced Argument Settings

Options and Arguments can be customized using `OptionSettings`/`ArgumentsSettings`:

```python
from typing import Annotated
from swiftcli.types import OptionSettings

class MyParams(BaseModel):
    verbose: Annotated[
        int,
        OptionSettings(
            count=True,  # Allow multiple flags (-vvv)
            aliases=["-v"],  # Add short alias
            help="Sets the verbosity level"
        )
    ] = 0
``` 