"""
Provide implementation of the command line interface's receipt commands.
"""
import sys

import click
from remme import Remme

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.receipt.forms import GetReceiptsForm
from cli.receipt.help import RECEIPT_TRANSACTION_IDENTIFIERS_ARGUMENT_HELP_MESSAGE
from cli.receipt.service import Receipt
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('receipt', chain=True)
def receipt_commands():
    """
    Provide commands for working with receipt.
    """
    pass


@click.option('--ids', type=str, required=True, help=RECEIPT_TRANSACTION_IDENTIFIERS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@receipt_commands.command('get')
def get_receipt(ids, node_url):
    """
    Get a list of the transaction's receipts by identifiers.
    """
    arguments, errors = GetReceiptsForm().load({
        'ids': ids,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    identifiers = arguments.get('ids')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = Receipt(service=remme).get(identifiers=identifiers)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
