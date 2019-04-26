"""
Provide implementation of the command line interface's public key commands.
"""
import sys

import click
from remme import Remme

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.public_key.forms import (
    GetPublicKeyInformationForm,
    GetPublicKeysForm,
)
from cli.public_key.help import (
    ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE,
    PUBLIC_KEY_ADDRESS_ARGUMENT_HELP_MESSAGE,
)
from cli.public_key.service import PublicKey
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('public-key', chain=True)
def public_key_commands():
    """
    Provide commands for working with public key.
    """
    pass


@click.option('--address', type=str, required=True, help=PUBLIC_KEY_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@public_key_commands.command('get-info')
def get_public_key_info(address, node_url):
    """
    Get information about public key by its address.
    """
    arguments, errors = GetPublicKeyInformationForm().load({
        'address': address,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    public_key_address = arguments.get('address')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = PublicKey(service=remme).get(address=public_key_address)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)


@click.option('--address', type=str, required=True, help=ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@public_key_commands.command('get-list')
def get_public_keys(address, node_url):
    """
    Get a list of the addresses of the public keys by account address.
    """
    arguments, errors = GetPublicKeysForm().load({
        'address': address,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    account_address = arguments.get('address')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = PublicKey(service=remme).get_list(address=account_address)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
