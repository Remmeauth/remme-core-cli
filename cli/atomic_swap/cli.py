"""
Provide implementation of the command line interface's atomic swap commands.
"""
import asyncio
import click
from remme import Remme

from cli.atomic_swap.service import AtomicSwap
from cli.constants import NODE_URL_ARGUMENT_HELP_MESSAGE

loop = asyncio.get_event_loop()


@click.group('atomic-swap', chain=True)
def atomic_swap_commands():
    """
    Provide commands for working with atomic swap.
    """
    pass


@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE)
@atomic_swap_commands.command('get-public-key')
def get_public_key(node_url):
    """
    Get public key of atomic swap.
    """
    if node_url is None:
        node_url = 'localhost'

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    public_key = loop.run_until_complete(AtomicSwap(service=remme).get())

    click.echo(public_key)
