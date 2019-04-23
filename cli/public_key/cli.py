"""
Provide implementation of the command line interface's public key commands.
"""
import asyncio
import sys

import click
from remme import Remme

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.public_key.forms import GetPublicKeyInfoForm
from cli.public_key.help import GET_PUBLIC_KEY_INFO_ADDRESS_ARGUMENT_HELP_MESSAGE
from cli.public_key.service import PublicKey
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)

loop = asyncio.get_event_loop()


@click.group('public-key', chain=True)
def public_key_commands():
    """
    Provide commands for working with public key.
    """
    pass


@click.option('--address', type=str, required=True, help=GET_PUBLIC_KEY_INFO_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@public_key_commands.command('get-info')
def get_public_key_info(address, node_url):
    """
    Get information about public key by public key address.
    """
    arguments, errors = GetPublicKeyInfoForm().load({
        'address': address,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    address = arguments.get('address')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = PublicKey(service=remme).get_info(address=address)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
