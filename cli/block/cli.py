"""
Provide implementation of the command line interface's block commands.
"""
import sys

import click
from remme import Remme

from cli.block.forms import (
    GetBlockByIdentifierForm,
    GetBlocksListForm,
)
from cli.block.help import (
    BLOCK_IDENTIFIER_ARGUMENT_HELP_MESSAGE,
    BLOCKS_HEAD_ARGUMENT_HELP_MESSAGE,
    BLOCKS_IDENTIFIERS_ARGUMENT_HELP_MESSAGE,
    BLOCKS_IDENTIFIERS_ONLY_ARGUMENT_HELP_MESSAGE,
    BLOCKS_LIMIT_ARGUMENT_HELP_MESSAGE,
    BLOCKS_REVERSE_ARGUMENT_HELP_MESSAGE,
)
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


@click.option('--ids', required=False, type=str, help=BLOCKS_IDENTIFIERS_ARGUMENT_HELP_MESSAGE)
@click.option('--limit', required=False, type=int, help=BLOCKS_LIMIT_ARGUMENT_HELP_MESSAGE)
@click.option('--head', required=False, type=str, help=BLOCKS_HEAD_ARGUMENT_HELP_MESSAGE)
@click.option('--reverse', required=False, is_flag=True, help=BLOCKS_REVERSE_ARGUMENT_HELP_MESSAGE)
@click.option('--ids-only', required=False, is_flag=True, help=BLOCKS_IDENTIFIERS_ONLY_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@block_commands.command('get-list')
def get_blocks(ids, head, limit, reverse, ids_only, node_url):
    """
    Get a list of blocks.
    """
    arguments, errors = GetBlocksListForm().load({
        'ids': ids,
        'limit': limit,
        'head': head,
        'reverse': reverse,
        'ids_only': ids_only,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    block_ids = arguments.get('ids')
    limit = arguments.get('limit')
    head = arguments.get('head')
    reverse = arguments.get('reverse')
    ids_only = arguments.get('ids_only')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    if ids_only:
        result, errors = Block(service=remme).get_list_ids(ids=block_ids, head=head, limit=limit, reverse=reverse)
    else:
        result, errors = Block(service=remme).get_list(ids=block_ids, head=head, limit=limit, reverse=reverse)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)


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
