"""
Provide implementation of the command line interface's node account commands.
"""
import sys

import click
from remme import Remme
from remme.models.account.account_type import AccountType

from cli.config import NodePrivateKey
from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.errors import NotSupportedOsToGetNodePrivateKeyError
from cli.generic.forms.forms import TransferTokensForm
from cli.node_account.forms import GetNodeAccountInformationForm
from cli.node_account.help import (
    ACCOUNT_ADDRESS_TO_ARGUMENT_HELP_MESSAGE,
    AMOUNT_ARGUMENT_HELP_MESSAGE,
    NODE_ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE,
    PRIVATE_KEY_ARGUMENT_HELP_MESSAGE,
)
from cli.node_account.service import NodeAccount
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('node-account', chain=True)
def node_account_commands():
    """
    Provide commands for working with node account.
    """
    pass


@click.option('--address', type=str, required=True, help=NODE_ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@node_account_commands.command('get')
def get(address, node_url):
    """
    Get information about the node account by its address.
    """
    arguments, errors = GetNodeAccountInformationForm().load({
        'address': address,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    node_account_address = arguments.get('address')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080'},
    )

    result, errors = NodeAccount(service=remme).get(address=node_account_address)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)


@click.option('--private-key', type=str, required=True, help=PRIVATE_KEY_ARGUMENT_HELP_MESSAGE)
@click.option('--address-to', type=str, required=True, help=ACCOUNT_ADDRESS_TO_ARGUMENT_HELP_MESSAGE)
@click.option('--amount', type=int, required=True, help=AMOUNT_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@node_account_commands.command('transfer-tokens')
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
        account_config={'private_key_hex': private_key, 'account_type': AccountType.NODE},
        network_config={'node_address': str(node_url) + ':8080'},
    )

    result, errors = NodeAccount(service=remme).transfer_tokens(address_to=address_to, amount=amount)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)


@node_account_commands.command('transfer-tokens-from-frozen-to-unfrozen')
def transfer_tokens_from_frozen_to_unfrozen():
    """
    Transfer available tokens from frozen to unfrozen reputation's balances.
    """
    try:
        node_private_key = NodePrivateKey().get()

    except (NotSupportedOsToGetNodePrivateKeyError, FileNotFoundError) as error:
        print_errors(errors=str(error))
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    remme = Remme(
        account_config={'private_key_hex': node_private_key, 'account_type': AccountType.NODE},
        network_config={'node_address': 'localhost' + ':8080'},
    )

    result, errors = NodeAccount(service=remme).transfer_tokens_from_frozen_to_unfrozen()

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
