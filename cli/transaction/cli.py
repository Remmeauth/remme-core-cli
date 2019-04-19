"""
Provide implementation of the command line interface's transaction info commands.
"""
import asyncio
import sys

import click
from aiohttp_json_rpc import RpcGenericServerDefinedError
from cli.constants import (
    FAILED_EXIT_FROM_COMMAND,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.forms import ValidationForm
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
)
from marshmallow import ValidationError

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
    try:
        arguments = ValidationForm().load({
            'ids': ids,
            'start': start,
            'limit': limit,
            'head': head,
            'family_name': family_name,
        })
    except ValidationError as err:
        click.echo(err.messages)
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    remme = get_network(node_url=node_url)

    transaction = Transaction(service=remme)
    try:
        transactions = loop.run_until_complete(
            transaction.get_list(arguments),
        )

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
    transaction_id, errors = ValidationForm().load({
        'ids': id,
    })

    if errors:
        click.echo(errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND)

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
