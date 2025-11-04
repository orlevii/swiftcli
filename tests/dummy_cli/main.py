from typing import Any

import click

from clantic import Group
from tests.dummy_cli.commands.copy import CopyCommand
from tests.dummy_cli.commands.greet import GreetCommand


def print_version(ctx: click.Context, _: Any, value: bool) -> None:
    if not value:
        return
    msg = "DummyCLI {}".format(click.style("0.1.0", fg="yellow"))
    click.echo(msg)
    ctx.exit()


cli = Group(
    params=[
        click.Option(
            ["--version", "-V"],
            is_flag=True,
            callback=print_version,
            help="Display cli version",
        )
    ]
)
cli.add_command_cls(GreetCommand)
cli.add_command_cls(CopyCommand)

if __name__ == "__main__":
    cli()
