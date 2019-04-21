"""
Provide utils for command line interface.
"""
import json

import click
import marshmallow
from remme import Remme


def dict_to_pretty_json(data):
    """
    Convert dictionary to string with indents as human readable text.
    """
    return json.dumps(data, indent=4, sort_keys=True)


async def return_async_value(value):
    """
    Asynchronous function return value impostor.

    Using for mock particular asynchronous function with specified return value.

    Example of usage in code:
        mock_account_get_balance = mock.patch('cli.account.service.Account.get_balance')
        mock_account_get_balance.return_value = return_async_value(13500)

    References:
        - https://github.com/pytest-dev/pytest-mock/issues/60
    """
    return value


def get_network(node_url):
    """
    Create object for sending requests to chain.
    """
    if node_url is None:
        node_url = 'localhost'

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })
    return remme


def pprint_walker(printer):
    """
    Change print behavior by error type.

    Arguments:
        printer (function): function that print message.
        error (Exception): particular error object.

    Returns:
        Redefined print function.
    """
    def pprint_inner(error):

        if isinstance(error, marshmallow.exceptions.ValidationError):
            for err in error.messages:
                printer(error.messages.get(err)[0])

        else:
            printer(error)

    return pprint_inner


@pprint_walker
def pprint(error):
    """
    Print to a console error message.

    Using for a print exception error message to the console.

    Arguments:
        error (Exception): particular error object.

    References:
        https://click.palletsprojects.com/en/7.x/utils/#ansi-colors
    """
    click.secho(f'{error}', blink=True, bold=True, fg='red')
