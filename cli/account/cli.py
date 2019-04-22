"""
Provide implementation of the command line interface's account commands.
"""
import sys
import re

import asyncio
import click
from remme import Remme

from cli.account.help import GET_ACCOUNT_BALANCE_ADDRESS_ARGUMENT_HELP_MESSAGE
from cli.account.service import Account
from cli.constants import (
    ADDRESS_REGEXP,
    FAILED_EXIT_FROM_COMMAND,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.utils import default_node_url

loop = asyncio.get_event_loop()


@click.group('account', chain=True)
def account_commands():
    """
    Provide commands for working with account.
    """
    pass


@click.option('--address', type=str, required=True, help=GET_ACCOUNT_BALANCE_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@account_commands.command('get-balance')
def get_balance(address, node_url):
    """
    Get balance of the account by its address.
    """
    if re.match(pattern=ADDRESS_REGEXP, string=address) is None:
        click.echo('The following address `{address}` is not valid.'.format(address=address))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    remme = Remme(network_config={'node_address': str(node_url) + ':8080'})

    account_service = Account(service=remme)
    balance = loop.run_until_complete(account_service.get_balance(address=address))

    click.echo(balance)
