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

loop = asyncio.get_event_loop()


@click.group('account', chain=True)
def account_commands():
    """
    Provide commands for working with account.
    """
    pass


@click.option('--address', type=str, required=True, help=GET_ACCOUNT_BALANCE_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE)
@account_commands.command('get-balance')
def get_balance(address, node_url):
    """
    Get balance of the account by its address.
    """
    if re.match(pattern=ADDRESS_REGEXP, string=address) is None:
        click.echo(f'The following address `{address}` is not valid.')
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    if node_url is None:
        node_url = 'localhost'

    remme = Remme(private_key_hex=None, network_config={
        'node_address': str(node_url) + ':8080',
    })

    account_service = Account(service=remme)
    balance = loop.run_until_complete(account_service.get_balance(address=address))

    click.echo(balance)
