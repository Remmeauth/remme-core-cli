"""
Provide implementation of the command line interface's account commands.
"""
import click
from remme import Remme

from cli.services.account import Account

GET_ACCOUNT_BALANCE_ADDRESS_ARGUMENT_HELP_MESSAGE = 'Get balance of the account by its address.'
NODE_URL_ARGUMENT_HELP_MESSAGE = 'Apply the command to the specified node by its URL.'


@click.group('account', chain=True)
def account_commands():
    """
    Provide commands for working with account.
    """
    pass


@click.option('--address', type=str, required=True, help=GET_ACCOUNT_BALANCE_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE)
@account_commands.command('get-balance')
def get_balance(address, node_url):
    """
    Get balance of the account by its address.
    """
    if node_url is None:
        node_url = 'localhost'

    remme = Remme(private_key_hex=None, network_config={
        'node_address': str(node_url) + ':8080',
        'ssl_mode': False,
    })

    balance = Account(service=remme).get_balance(address=address)
    click.echo(balance)
