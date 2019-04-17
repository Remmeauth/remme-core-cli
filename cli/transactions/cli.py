"""
Provide implementation of the command line interface's transaction info commands.
"""
import asyncio
import click
from aiohttp_json_rpc import RpcGenericServerDefinedError

from cli.utils import (
    validate_ids,
    validate_limit,
    validate_head_sign,
    validate_id,
    get_network,
    dict_to_pretty_json,
)

from cli.transactions.service import Transactions
from cli.transactions.help import (
    LIST_TRANSACTIONS_HEAD_HELP_MESSAGE,
    LIST_TRANSACTIONS_START_HELP_MESSAGE,
    LIST_TRANSACTIONS_LIMIT_HELP_MESSAGE,
    LIST_TRANSACTIONS_REVERSE_HELP_MESSAGE,
    LIST_TRANSACTIONS_FAMILY_NAME_HELP_MESSAGE,
    LIST_TRANSACTIONS_IDS_HELP_MESSAGE,
    TRANSACTION_ID_HELP_MESSAGE,
)
from cli.constants import (
    HEADER_SIGNATURE_REGEXP,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)

loop = asyncio.get_event_loop()


@click.group('transactions', chain=True)
def transaction_command():
    """
    Provide commands for working with transactions.
    """
    pass


@click.option('--ids', type=str, help=LIST_TRANSACTIONS_IDS_HELP_MESSAGE)
@click.option('--start', type=str, help=LIST_TRANSACTIONS_START_HELP_MESSAGE)
@click.option('--limit', type=int, help=LIST_TRANSACTIONS_LIMIT_HELP_MESSAGE)
@click.option('--head', type=str, help=LIST_TRANSACTIONS_HEAD_HELP_MESSAGE)
@click.option('--reverse', type=str, help=LIST_TRANSACTIONS_REVERSE_HELP_MESSAGE)
@click.option('--family_name', type=str, help=LIST_TRANSACTIONS_FAMILY_NAME_HELP_MESSAGE)
@click.option('--node-url', type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE)
@transaction_command.command('get-list')
def get_list_transaction(ids, start, limit, head, reverse, family_name, node_url):
    """
    Get a list of transactions.
    """
    transaction_ids = validate_ids(ids=ids, regexp_pattern=HEADER_SIGNATURE_REGEXP)
    limit = validate_limit(limit=limit)
    start = validate_head_sign(sign=start, regexp_pattern=HEADER_SIGNATURE_REGEXP)
    head = validate_head_sign(sign=head, regexp_pattern=HEADER_SIGNATURE_REGEXP)

    remme = get_network(node_url=node_url)

    transaction = Transactions(service=remme)
    try:
        transactions = loop.run_until_complete(
            transaction.list_transactions(
                query={
                    'ids': transaction_ids,
                    'start': start,
                    'limit': limit,
                    'head': head,
                    'reverse': reverse,
                    'family_name': family_name,
                }))

        click.echo(dict_to_pretty_json(data=transactions))

    except RpcGenericServerDefinedError:
        click.echo("Generic server defined Error (Transactions not found).")

    except Exception:
        click.echo("Generic server defined Error (Connection error).")


@click.option('--identifier', required=True, type=str, help=TRANSACTION_ID_HELP_MESSAGE)
@click.option('--node-url', type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE)
@transaction_command.command('get-single')
def get_single_transaction(identifier, node_url):
    """
    Fetch transaction by its id.
    """
    transaction_id = validate_id(id_=identifier, regexp_pattern=HEADER_SIGNATURE_REGEXP)
    remme = get_network(node_url=node_url)

    transaction = Transactions(service=remme)
    try:
        transactions = loop.run_until_complete(
            transaction.single_transaction(
                transaction_id=transaction_id,
            ))

        click.echo(dict_to_pretty_json(data=transactions))

    except RpcGenericServerDefinedError:
        click.echo("Generic server defined Error (Transaction not found).")

    except Exception:
        click.echo("Generic server defined Error (Connection error).")
