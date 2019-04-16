"""
Provide implementation of the command line interface to interact with Remme-core.
"""
import click

from cli.account.cli import account_commands
from cli.public_key.cli import public_key_commands


@click.group()
@click.version_option()
@click.help_option()
def cli():
    """
    Command-line interface to interact with Remme-core.
    """
    pass


cli.add_command(public_key_commands)
