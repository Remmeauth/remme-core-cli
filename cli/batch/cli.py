"""
Provide implementation of the command line interface's batch commands.
"""
import sys

import click
from remme import Remme

from cli.batch.forms import (
    GetBatchesListForm,
    GetBatchForm,
    GetBatchStatusForm,
)
from cli.batch.help import (
    BATCH_IDENTIFIER_ARGUMENT_HELP_MESSAGE,
    BATCH_STATUS_IDENTIFIER_ARGUMENT_HELP_MESSAGE,
    BATCHES_HEAD_ARGUMENT_HELP_MESSAGE,
    BATCHES_IDENTIFIERS_ARGUMENT_HELP_MESSAGE,
    BATCHES_IDENTIFIERS_ONLY_ARGUMENT_HELP_MESSAGE,
    BATCHES_LIMIT_ARGUMENT_HELP_MESSAGE,
    BATCHES_REVERSE_ARGUMENT_HELP_MESSAGE,
    BATCHES_START_ARGUMENT_HELP_MESSAGE,
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


@click.option('--id', required=True, type=str, help=BATCH_IDENTIFIER_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@batch_commands.command('get')
def get_batch(id, node_url):
    """
    Get a batch by its identifier.
    """
    arguments, errors = GetBatchForm().load({
        'id': id,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    batch_id = arguments.get('id')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    batch, errors = Batch(service=remme).get(id=batch_id)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=batch)


@click.option('--id', required=True, type=str, help=BATCH_STATUS_IDENTIFIER_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@batch_commands.command('get-status')
def get_batch_status(id, node_url):
    """
    Get a batch status by its identifier.
    """
    arguments, errors = GetBatchStatusForm().load({
        'id': id,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    batch_id = arguments.get('id')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = Batch(service=remme).get_status(id=batch_id)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)


@click.option('--ids', required=False, type=str, help=BATCHES_IDENTIFIERS_ARGUMENT_HELP_MESSAGE)
@click.option('--start', required=False, type=str, help=BATCHES_START_ARGUMENT_HELP_MESSAGE)
@click.option('--limit', required=False, type=int, help=BATCHES_LIMIT_ARGUMENT_HELP_MESSAGE)
@click.option('--head', required=False, type=str, help=BATCHES_HEAD_ARGUMENT_HELP_MESSAGE)
@click.option('--reverse', required=False, is_flag=True, help=BATCHES_REVERSE_ARGUMENT_HELP_MESSAGE)
@click.option('--ids-only', required=False, is_flag=True, help=BATCHES_IDENTIFIERS_ONLY_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@batch_commands.command('get-list')
def get_batches(ids, start, limit, head, reverse, ids_only, node_url):
    """
    Get a list of batches.
    """
    arguments, errors = GetBatchesListForm().load({
        'ids': ids,
        'start': start,
        'limit': limit,
        'head': head,
        'reverse': reverse,
        'ids_only': ids_only,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    batch_ids = arguments.get('ids')
    start = arguments.get('start')
    limit = arguments.get('limit')
    head = arguments.get('head')
    reverse = arguments.get('reverse')
    ids_only = arguments.get('ids_only')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    if ids_only:
        result, errors = Batch(service=remme).get_list_ids(
            ids=batch_ids, start=start, limit=limit, head=head, reverse=reverse,
        )
    else:
        result, errors = Batch(service=remme).get_list(
            ids=batch_ids, start=start, limit=limit, head=head, reverse=reverse,
        )

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
