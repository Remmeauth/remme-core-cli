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
from cli.public_key.forms import GetPublicKeysForm
from cli.public_key.help import GET_PUBLIC_KEYS_ADDRESS_ARGUMENT_HELP_MESSAGE
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


@click.option('--address', type=str, required=True, help=GET_PUBLIC_KEYS_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@public_key_commands.command('get-list')
def get_public_keys(address, node_url):
    """
    Get list of the public keys by account address.
    """
    arguments, errors = GetPublicKeysForm().load({
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

    public_key_service = PublicKey(service=remme)
    addresses = loop.run_until_complete(public_key_service.get_list(address=address))

    print_result(result=addresses)
