"""
Provide implementation of the command line interface's public key commands.
"""
import sys
import re

import asyncio
import click
from remme import Remme

from cli.constants import (
    ADDRESS_REGEXP,
    FAILED_EXIT_FROM_COMMAND,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.public_key.help import GET_PUBLIC_KEY_ADDRESS_ARGUMENT_HELP_MESSAGE
from cli.public_key.service import PublicKey

loop = asyncio.get_event_loop()


@click.group('public-key', chain=True)
def public_key_commands():
    """
    Provide commands for working with public key.
    """
    pass


@click.option('--address', type=str, required=True, help=GET_PUBLIC_KEY_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE)
@public_key_commands.command('get-single')
def get_single(address, node_url):
    """
    Get public key by account address.
    """
    if re.match(pattern=ADDRESS_REGEXP, string=address) is None:
        click.echo('The following address `{address}` is not valid.'.format(address=address))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    if node_url is None:
        node_url = 'localhost'

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    public_key = loop.run_until_complete(PublicKey(service=remme).get(address=address))

    click.echo(public_key)
