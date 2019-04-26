"""
Provide implementation of the command line interface's transaction commands.
"""
import asyncio
import sys

import click
from remme import Remme

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.transaction.forms import (
    GetListTransactionForm,
    GetSingleTransaction,
)
from cli.transaction.help import (
    TRANSACTION_FAMILY_NAME_ARGUMENT_HELP_MESSAGE,
    TRANSACTION_HEAD_ARGUMENT_HELP_MESSAGE,
    TRANSACTION_ID_ARGUMENT_HELP_MESSAGE,
    TRANSACTION_IDS_ARGUMENT_HELP_MESSAGE,
    TRANSACTION_LIMIT_ARGUMENT_HELP_MESSAGE,
    TRANSACTION_REVERSE_ARGUMENT_HELP_MESSAGE,
    TRANSACTION_START_ARGUMENT_HELP_MESSAGE,
)
from cli.transaction.service import Transaction
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)

loop = asyncio.get_event_loop()


@click.group('transaction', chain=True)
def transaction_command():
    """
    Provide commands for working with transaction.
    """
    pass


@click.option('--ids', required=False, type=str, help=TRANSACTION_IDS_ARGUMENT_HELP_MESSAGE)
@click.option('--start', required=False, type=str, help=TRANSACTION_START_ARGUMENT_HELP_MESSAGE)
@click.option('--limit', required=False, type=int, help=TRANSACTION_LIMIT_ARGUMENT_HELP_MESSAGE)
@click.option('--head', required=False, type=str, help=TRANSACTION_HEAD_ARGUMENT_HELP_MESSAGE)
@click.option('--reverse', is_flag=True, help=TRANSACTION_REVERSE_ARGUMENT_HELP_MESSAGE)
@click.option('--family-name', required=False, type=str, help=TRANSACTION_FAMILY_NAME_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@transaction_command.command('get-list')
def get_transactions(ids, start, limit, head, reverse, family_name, node_url):
    """
    Get a list of transactions.
    """
    arguments, errors = GetListTransactionForm().load({
        'ids': ids,
        'start': start,
        'limit': limit,
        'head': head,
        'family_name': family_name,
        'reverse': reverse,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    transactions, errors = Transaction(service=remme).get_list(
        query=arguments,
    )

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=transactions)


@click.option('--id', required=True, type=str, help=TRANSACTION_ID_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@transaction_command.command('get')
def get_transaction(id, node_url):
    """
    Fetch transaction by its id.
    """
    arguments, errors = GetSingleTransaction().load({
        'id': id,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    transaction, errors = Transaction(service=remme).get(
        transaction_id=arguments.get('id'),
    )

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=transaction)
