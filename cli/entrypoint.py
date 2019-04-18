"""
Provide implementation of the command line interface to interact with Remme-core.
"""
import click

from cli.account.cli import account_commands
from cli.atomic_swap.cli import atomic_swap_commands


@click.group()
@click.version_option()
@click.help_option()
def cli():
    """
    Command-line interface to interact with Remme-core.
    """
    pass


cli.add_command(account_commands)
cli.add_command(atomic_swap_commands)
