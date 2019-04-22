"""
Provide implementation of the command line interface's atomic swap commands.
"""
import asyncio
import sys

import click
from remme import Remme

from cli.atomic_swap.forms import GetAtomicSwapInfoForm
from cli.atomic_swap.help import (
    GET_SWAP_INFO_IDENTIFIER_ARGUMENT_HELP_MESSAGE,
    PRIVATE_KEY_FROM_ARGUMENT_HELP_MESSAGE,
)
from cli.atomic_swap.service import AtomicSwap
from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)

loop = asyncio.get_event_loop()


@click.group('atomic-swap', chain=True)
def atomic_swap_commands():
    """
    Provide commands for working with atomic swap.
    """
    pass


@click.option('--private-key-from', type=str, required=True, help=PRIVATE_KEY_FROM_ARGUMENT_HELP_MESSAGE)
@click.option('--id', type=str, required=True, help=GET_SWAP_INFO_IDENTIFIER_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@atomic_swap_commands.command('get-info')
def get_swap_info(private_key_from, id, node_url):
    """
    Get information about atomic swap by swap identifier.
    """
    arguments, errors = GetAtomicSwapInfoForm().load({
        'private_key_from': private_key_from,
        'id': id,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    private_key_from = arguments.get('private_key_from')
    swap_id = arguments.get('id')
    node_url = arguments.get('node_url')

    remme = Remme(private_key_hex=private_key_from, network_config={
        'node_address': str(node_url) + ':8080',
    })

    atomic_swap_service = AtomicSwap(service=remme)
    swap_info = loop.run_until_complete(atomic_swap_service.get_info(swap_id=swap_id))

    print_result(result=swap_info)
