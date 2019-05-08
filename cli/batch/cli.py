"""
Provide implementation of the command line interface's batch commands.
"""
import sys

import click
from remme import Remme

from cli.batch.forms import GetBatchForm
from cli.batch.help import BATCH_ID_ARGUMENT_HELP_MESSAGE
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


@click.option('--id', required=True, type=str, help=BATCH_ID_ARGUMENT_HELP_MESSAGE)
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
