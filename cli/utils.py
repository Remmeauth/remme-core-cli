"""
Provide utils for command line interface.
"""
import json

import click

from cli.config import ConfigFile


def dict_to_pretty_json(data):
    r"""
    Convert dictionary to json with indents (human readable string).

    From the following code:
        {
            "address": [
                "The following address `1120076ecf036e857f42129b5830` is invalid."
            ]
        }

    It creates:
        "{\n    \"address\": [\n        \"The following address `1120076ecf036e857f42129b5830` is invalid.\"    ]\n}\n"

    Notes:
        - `r` symbol at the start of the documentation is presented because of PEP257.

    References:
        - https://www.python.org/dev/peps/pep-0257/#id15
        - https://stackoverflow.com/a/33734332/9632462
    """
    return json.dumps(data, indent=4, sort_keys=True)


def print_result(result):
    """
    Print successful result to the terminal.
    """
    return click.echo(dict_to_pretty_json({'result': result}))


def print_errors(errors):
    """
    Print error messages to the terminal.

    Arguments:
        errors (dict): dictionary with error messages.

    References:
        - https://click.palletsprojects.com/en/7.x/utils/#ansi-colors
    """
    click.secho(dict_to_pretty_json({'errors': errors}), blink=True, bold=True, fg='red')


def default_node_url():
    """
    Get default node URL.
    """
    config_parameters = ConfigFile().parse()

    if config_parameters.node_url is None:
        return 'localhost'

    return config_parameters.node_url


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
