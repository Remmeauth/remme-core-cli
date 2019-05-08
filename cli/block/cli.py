"""
Provide implementation of the command line interface's block commands.
"""
import sys

import click
from remme import Remme

from cli.block.forms import GetBlockByIdentifierForm
from cli.block.help import BLOCK_IDENTIFIER_ARGUMENT_HELP_MESSAGE
from cli.block.service import Block
from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('block', chain=True)
def block_commands():
    """
    Provide commands for working with block.
    """
    pass


@click.option('--id', type=str, required=True, help=BLOCK_IDENTIFIER_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@block_commands.command('get')
def get_block(id, node_url):
    """
    Get a block by its identifier.
    """
    arguments, errors = GetBlockByIdentifierForm().load({
        'id': id,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    identifier = arguments.get('id')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = Block(service=remme).get(identifier=identifier)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
