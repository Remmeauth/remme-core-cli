"""
Provide utils for command line interface.
"""
import json


def dict_to_pretty_json(data):
    """
    Convert dictionary to string with indents as human readable text.
    """
    return json.dumps(data, indent=4, sort_keys=True)


def default_node_url():
    """
    Get default node URL.
    """
    return 'localhost'


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
