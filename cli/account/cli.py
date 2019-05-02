"""
Provide implementation of the command line interface's account commands.
"""
import sys

import click
from remme import Remme

from cli.account.forms import (
    GetAccountBalanceForm,
    TransferTokensForm,
)
from cli.account.help import (
    ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE,
    ACCOUNT_ADDRESS_TO_ARGUMENT_HELP_MESSAGE,
    AMOUNT_ARGUMENT_HELP_MESSAGE,
    PRIVATE_KEY_ARGUMENT_HELP_MESSAGE,
)
from cli.account.service import Account
from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('account', chain=True)
def account_commands():
    """
    Provide commands for working with account.
    """
    pass


@click.option('--address', type=str, required=True, help=ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@account_commands.command('get-balance')
def get_balance(address, node_url):
    """
    Get balance of the account by its address.
    """
    arguments, errors = GetAccountBalanceForm().load({
        'address': address,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    address = arguments.get('address')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = Account(service=remme).get_balance(address=address)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)


@click.option('--private-key', type=str, required=True, help=PRIVATE_KEY_ARGUMENT_HELP_MESSAGE)
@click.option('--address-to', type=str, required=True, help=ACCOUNT_ADDRESS_TO_ARGUMENT_HELP_MESSAGE)
@click.option('--amount', type=int, required=True, help=AMOUNT_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@account_commands.command('transfer-tokens')
def transfer_tokens(private_key, address_to, amount, node_url):
    """
    Transfer tokens to address.
    """
    arguments, errors = TransferTokensForm().load({
        'private_key': private_key,
        'address_to': address_to,
        'amount': amount,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    private_key = arguments.get('private_key')
    address_to = arguments.get('address_to')
    amount = arguments.get('amount')
    node_url = arguments.get('node_url')

    remme = Remme(
        account_config={'private_key_hex': private_key},
        network_config={'node_address': str(node_url) + ':8080'},
    )

    result, errors = Account(service=remme).transfer_tokens(address_to=address_to, amount=amount)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
