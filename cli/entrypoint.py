"""
Provide implementation of the command line interface to interact with Remme-core.
"""
import click

from cli.account.cli import account_commands
from cli.atomic_swap.cli import atomic_swap_commands
from cli.node.cli import node_commands
from cli.public_key.cli import public_key_commands
from cli.state.cli import state_command
from cli.transaction.cli import transaction_command


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
cli.add_command(node_commands)
cli.add_command(public_key_commands)
cli.add_command(state_command)
cli.add_command(transaction_command)
