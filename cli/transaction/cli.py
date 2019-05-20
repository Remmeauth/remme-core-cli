"""
Provide implementation of the command line interface's transaction commands.
"""
import sys

import click
from remme import Remme

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.transaction.forms import (
    GetTransactionForm,
    GetTransactionsListForm,
)
from cli.transaction.help import (
    TRANSACTION_ID_ARGUMENT_HELP_MESSAGE,
    TRANSACTIONS_FAMILY_NAME_ARGUMENT_HELP_MESSAGE,
    TRANSACTIONS_HEAD_ARGUMENT_HELP_MESSAGE,
    TRANSACTIONS_IDENTIFIERS_ARGUMENT_HELP_MESSAGE,
    TRANSACTIONS_IDENTIFIERS_ONLY_ARGUMENT_HELP_MESSAGE,
    TRANSACTIONS_LIMIT_ARGUMENT_HELP_MESSAGE,
    TRANSACTIONS_REVERSE_ARGUMENT_HELP_MESSAGE,
    TRANSACTIONS_START_ARGUMENT_HELP_MESSAGE,
)
from cli.transaction.service import Transaction
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('transaction', chain=True)
def transaction_command():
    """
    Provide commands for working with transaction.
    """
    pass


@click.option('--ids', required=False, type=str, help=TRANSACTIONS_IDENTIFIERS_ARGUMENT_HELP_MESSAGE)
@click.option('--start', required=False, type=str, help=TRANSACTIONS_START_ARGUMENT_HELP_MESSAGE)
@click.option('--limit', required=False, type=int, help=TRANSACTIONS_LIMIT_ARGUMENT_HELP_MESSAGE)
@click.option('--head', required=False, type=str, help=TRANSACTIONS_HEAD_ARGUMENT_HELP_MESSAGE)
@click.option('--reverse', required=False, is_flag=True, help=TRANSACTIONS_REVERSE_ARGUMENT_HELP_MESSAGE)
@click.option('--family-name', required=False, type=str, help=TRANSACTIONS_FAMILY_NAME_ARGUMENT_HELP_MESSAGE)
@click.option('--ids-only', required=False, is_flag=True, help=TRANSACTIONS_IDENTIFIERS_ONLY_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@transaction_command.command('get-list')
def get_transactions(ids, start, limit, head, reverse, family_name, ids_only, node_url):
    """
    Get a list of transactions.
    """
    arguments, errors = GetTransactionsListForm().load({
        'ids': ids,
        'start': start,
        'limit': limit,
        'head': head,
        'family_name': family_name,
        'reverse': reverse,
        'ids_only': ids_only,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    transaction_ids = arguments.get('ids')
    start = arguments.get('start')
    limit = arguments.get('limit')
    head = arguments.get('head')
    reverse = arguments.get('reverse')
    family_name = arguments.get('family_name')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    if ids_only:
        result, errors = Transaction(service=remme).get_list_ids(
            ids=transaction_ids, start=start, limit=limit, head=head, family_name=family_name, reverse=reverse,
        )

    else:
        result, errors = Transaction(service=remme).get_list(
            ids=transaction_ids, start=start, limit=limit, head=head, family_name=family_name, reverse=reverse,
        )

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)


@click.option('--id', required=True, type=str, help=TRANSACTION_ID_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@transaction_command.command('get')
def get_transaction(id, node_url):
    """
    Fetch transaction by its identifier.
    """
    arguments, errors = GetTransactionForm().load({
        'id': id,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    transaction_id = arguments.get('id')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    transaction, errors = Transaction(service=remme).get(transaction_id=transaction_id)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=transaction)
