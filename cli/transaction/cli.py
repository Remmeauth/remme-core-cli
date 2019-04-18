"""
Provide implementation of the command line interface's transaction info commands.
"""
import asyncio

import click
from aiohttp_json_rpc import RpcGenericServerDefinedError

from cli.constants import (
    HEADER_SIGNATURE_REGEXP,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.transaction.help import (
    GET_TRANSACTION_ID_HELP_MESSAGE,
    GET_TRANSACTIONS_FAMILY_NAME_ARGUMENT_HELP_MESSAGE,
    GET_TRANSACTIONS_HEAD_ARGUMENT_HELP_MESSAGE,
    GET_TRANSACTIONS_IDS_ARGUMENT_HELP_MESSAGE,
    GET_TRANSACTIONS_LIMIT_ARGUMENT_HELP_MESSAGE,
    GET_TRANSACTIONS_REVERSE_ARGUMENT_HELP_MESSAGE,
    GET_TRANSACTIONS_START_ARGUMENT_HELP_MESSAGE,
)
from cli.transaction.service import Transaction
from cli.utils import (
    dict_to_pretty_json,
    get_network,
    validate_family_name,
    validate_ids,
    validate_limit,
    validate_sign,
)

loop = asyncio.get_event_loop()


@click.group('transaction', chain=True)
def transaction_command():
    """
    Provide commands for working with transaction.
    """
    pass


@click.option('--ids', required=False, type=str, help=GET_TRANSACTIONS_IDS_ARGUMENT_HELP_MESSAGE)
@click.option('--start', required=False, type=str, help=GET_TRANSACTIONS_START_ARGUMENT_HELP_MESSAGE)
@click.option('--limit', required=False, type=int, help=GET_TRANSACTIONS_LIMIT_ARGUMENT_HELP_MESSAGE)
@click.option('--head', required=False, type=str, help=GET_TRANSACTIONS_HEAD_ARGUMENT_HELP_MESSAGE)
@click.option('--reverse', required=False, type=str, help=GET_TRANSACTIONS_REVERSE_ARGUMENT_HELP_MESSAGE)
@click.option('--family-name', required=False, type=str, help=GET_TRANSACTIONS_FAMILY_NAME_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE)
@transaction_command.command('get-list')
def get_transactions(ids, start, limit, head, reverse, family_name, node_url):
    """
    Get a list of transaction.
    """
    transaction_ids = validate_ids(ids=ids, regexp_pattern=HEADER_SIGNATURE_REGEXP)
    limit = validate_limit(limit=limit)
    start = validate_sign(sign=start, regexp_pattern=HEADER_SIGNATURE_REGEXP, type_sign='start')
    head = validate_sign(sign=head, regexp_pattern=HEADER_SIGNATURE_REGEXP, type_sign='header signature')
    family_name = validate_family_name(family_name=family_name)

    remme = get_network(node_url=node_url)

    transaction = Transaction(service=remme)
    try:
        transactions = loop.run_until_complete(
            transaction.get_list(
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


@click.option('--id', required=True, type=str, help=GET_TRANSACTION_ID_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE)
@transaction_command.command('get-single')
def get_transaction(id, node_url):
    """
    Fetch transaction by its id.
    """
    transaction_id = validate_sign(sign=id, regexp_pattern=HEADER_SIGNATURE_REGEXP, type_sign='id')
    remme = get_network(node_url=node_url)

    transaction = Transaction(service=remme)
    try:
        transactions = loop.run_until_complete(
            transaction.get(
                transaction_id=transaction_id,
            ))

        click.echo(dict_to_pretty_json(data=transactions))

    except RpcGenericServerDefinedError:
        click.echo("Generic server defined Error (Transaction not found).")

    except Exception:
        click.echo("Generic server defined Error (Connection error).")
