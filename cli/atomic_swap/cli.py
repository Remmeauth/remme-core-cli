"""
Provide implementation of the command line interface's atomic swap commands.
"""
import sys

import click
from remme import Remme

from cli.atomic_swap.forms import GetAtomicSwapPublicKeyForm
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


@click.group('atomic-swap', chain=True)
def atomic_swap_commands():
    """
    Provide commands for working with atomic swap.
    """
    pass


@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@atomic_swap_commands.command('get-public-key')
def get_public_key(node_url):
    """
    Get public key of atomic swap.
    """
    arguments, errors = GetAtomicSwapPublicKeyForm().load({
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = AtomicSwap(service=remme).get_public_key()

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
