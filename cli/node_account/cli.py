"""
Provide implementation of the command line interface's node account commands.
"""
import sys

import click
from remme import Remme

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.node_account.forms import GetNodeAccountInformationForm
from cli.node_account.help import NODE_ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE
from cli.node_account.service import NodeAccount
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('node-account', chain=True)
def node_account_commands():
    """
    Provide commands for working with node account.
    """
    pass


@click.option('--address', type=str, required=True, help=NODE_ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@node_account_commands.command('get')
def get(address, node_url):
    """
    Get information about the node account by its address.
    """
    arguments, errors = GetNodeAccountInformationForm().load({
        'address': address,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    node_account_address = arguments.get('address')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080'},
    )

    result, errors = NodeAccount(service=remme).get(address=node_account_address)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
