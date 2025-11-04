from typing import Annotated

from clantic import BaseCommand
from clantic.types import Option, OptionSettings
from tests.dummy_cli.logger import logger

from .common_params import CommonParams


class GreetCommandParams(CommonParams):
    name: Option[str]
    birth_place: Annotated[str, OptionSettings(aliases=["-b"])] = "USA"


class GreetCommand(BaseCommand[GreetCommandParams]):
    NAME = "greet"

    def run(self) -> None:
        print(self.params)
        print("Hello,", self.params.name, "from", self.params.birth_place)
        logger.warning("WARN")
        logger.info("INFO")
        logger.debug("DEBUG")
