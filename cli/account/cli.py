"""
Provide implementation of the command line interface's account commands.
"""
import sys

import click
from remme import Remme

from cli.account.forms import GetAccountBalanceForm
from cli.account.help import ADDRESS_ARGUMENT_HELP_MESSAGE
from cli.account.service import Account
from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('account', chain=True)
def account_commands():
    """
    Provide commands for working with account.
    """
    pass


@click.option('--address', type=str, required=True, help=ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@account_commands.command('get-balance')
def get_balance(address, node_url):
    """
    Get balance of the account by its address.
    """
    arguments, errors = GetAccountBalanceForm().load({
        'address': address,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    address = arguments.get('address')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = Account(service=remme).get_balance(address=address)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
