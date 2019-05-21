"""
Provide implementation of the command line interface's masternode commands.
"""
import sys

import click
from remme import Remme
from remme.models.account.account_type import AccountType

from cli.config import NodePrivateKey
from cli.constants import FAILED_EXIT_FROM_COMMAND_CODE
from cli.errors import NotSupportedOsToGetNodePrivateKeyError
from cli.masternode.forms import OpenMasternodeForm
from cli.masternode.help import STARTING_AMOUNT_ARGUMENT_HELP_MESSAGE
from cli.masternode.service import Masternode
from cli.utils import (
    print_errors,
    print_result,
)


@click.group('masternode', chain=True)
def masternode_commands():
    """
    Provide commands for working with masternode.
    """
    pass


@click.option('--amount', type=int, required=True, help=STARTING_AMOUNT_ARGUMENT_HELP_MESSAGE)
@masternode_commands.command('open')
def open(amount):
    """
    Open the masternode with starting amount.
    """
    arguments, errors = OpenMasternodeForm().load({
        'amount': amount,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    amount = arguments.get('amount')

    try:
        node_private_key = NodePrivateKey().get()

    except (NotSupportedOsToGetNodePrivateKeyError, FileNotFoundError) as error:
        print_errors(errors=str(error))
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    remme = Remme(
        account_config={'private_key_hex': node_private_key, 'account_type': AccountType.NODE},
        network_config={'node_address': 'localhost' + ':8080'},
    )

    result, errors = Masternode(service=remme).open(amount=amount)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
