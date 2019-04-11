import click

from cli.account.cli import account_commands
from cli.blockchain_info.cli import transaction_command


@click.group()
@click.version_option()
@click.help_option()
def cli():
    """
    Command-line interface to interact with Remme-core.
    """
    pass


cli.add_command(account_commands)
cli.add_command(transaction_command)
