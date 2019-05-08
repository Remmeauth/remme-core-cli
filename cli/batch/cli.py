"""
Provide implementation of the command line interface's batch commands.
"""
import sys

import click
from remme import Remme

from cli.batch.forms import GetBatchesListForm
from cli.batch.help import (
    BATCH_HEAD_ARGUMENT_HELP_MESSAGE,
    BATCH_IDS_ARGUMENT_HELP_MESSAGE,
    BATCH_LIMIT_ARGUMENT_HELP_MESSAGE,
    BATCH_REVERSE_ARGUMENT_HELP_MESSAGE,
    BATCH_START_ARGUMENT_HELP_MESSAGE,
)
from cli.batch.service import Batch
from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('batch', chain=True)
def batch_commands():
    """
    Provide commands for working with batch.
    """
    pass


@click.option('--ids', required=False, type=str, help=BATCH_IDS_ARGUMENT_HELP_MESSAGE)
@click.option('--start', required=False, type=str, help=BATCH_START_ARGUMENT_HELP_MESSAGE)
@click.option('--limit', required=False, type=int, help=BATCH_LIMIT_ARGUMENT_HELP_MESSAGE)
@click.option('--head', required=False, type=str, help=BATCH_HEAD_ARGUMENT_HELP_MESSAGE)
@click.option('--reverse', required=False, is_flag=True, help=BATCH_REVERSE_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@batch_commands.command('get-list')
def get_batches(ids, start, limit, head, reverse, node_url):
    """
    Get a list of batches.
    """
    arguments, errors = GetBatchesListForm().load({
        'ids': ids,
        'start': start,
        'limit': limit,
        'head': head,
        'reverse': reverse,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    batch_ids = arguments.get('ids')
    start = arguments.get('start')
    limit = arguments.get('limit')
    head = arguments.get('head')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    batches, errors = Batch(service=remme).get_list(
        batch_ids=batch_ids,
        start=start,
        limit=limit,
        head=head,
        reverse=reverse,
    )

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=batches)
