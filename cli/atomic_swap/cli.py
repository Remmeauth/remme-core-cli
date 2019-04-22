"""
Provide implementation of the command line interface's atomic swap commands.
"""
import asyncio
import click
from remme import Remme

from cli.atomic_swap.help import GET_SWAP_INFO_IDENTIFIER_ARGUMENT_HELP_MESSAGE
from cli.atomic_swap.service import AtomicSwap
from cli.constants import NODE_URL_ARGUMENT_HELP_MESSAGE
from cli.utils import dict_to_pretty_json

loop = asyncio.get_event_loop()


@click.group('atomic-swap', chain=True)
def atomic_swap_commands():
    """
    Provide commands for working with atomic swap.
    """
    pass


@click.option('--id', type=str, required=True, help=GET_SWAP_INFO_IDENTIFIER_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default='localhost')
@atomic_swap_commands.command('get-public-key')
def get_swap_info(id, node_url):
    """
    Get information about atomic swap by swap identifier.
    """
    remme = Remme(network_config={'node_address': str(node_url) + ':8080'})

    atomic_swap_service = AtomicSwap(service=remme)

    swap_info = loop.run_until_complete(atomic_swap_service.get_list(swap_id=id))

    click.echo(dict_to_pretty_json(swap_info))
