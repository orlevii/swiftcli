from typing import Annotated

from swiftcli import BaseCommand
from swiftcli.types import Argument, Option, OptionSettings
from tests.dummy_cli.logger import logger

from .common_params import CommonParams


class CopyCommandParams(CommonParams):
    from_: Argument[str]
    to_: Argument[str]


class CopyCommand(BaseCommand[CopyCommandParams]):
    NAME = "copy"

    def run(self) -> None:
        print(self.params)
        print("Copying", self.params.from_, "->", self.params.to_)
