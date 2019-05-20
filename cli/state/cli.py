"""
Provide implementation of the command line interface's state commands.
"""
import sys

import click
from remme import Remme

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.state.forms import (
    GetStateForm,
    GetStateListForm,
)
from cli.state.help import (
    STATE_ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE,
    STATES_HEAD_ARGUMENT_HELP_MESSAGE,
    STATES_LIMIT_ARGUMENT_HELP_MESSAGE,
    STATES_REVERSE_ARGUMENT_HELP_MESSAGE,
)
from cli.state.service import State
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('state', chain=True)
def state_command():
    """
    Provide commands for working with state.
    """
    pass


@click.option('--address', required=True, type=str, help=STATE_ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@state_command.command('get')
def get_state(address, node_url):
    """
    Get a state by its address.
    """
    arguments, errors = GetStateForm().load({
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

    result, errors = State(service=remme).get(address=address)

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)


@click.option('--address', required=False, type=str, help=STATE_ACCOUNT_ADDRESS_ARGUMENT_HELP_MESSAGE)
@click.option('--limit', required=False, type=int, help=STATES_LIMIT_ARGUMENT_HELP_MESSAGE)
@click.option('--head', required=False, type=str, help=STATES_HEAD_ARGUMENT_HELP_MESSAGE)
@click.option('--reverse', required=False, is_flag=True, help=STATES_REVERSE_ARGUMENT_HELP_MESSAGE)
@click.option('--node-url', required=False, type=str, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@state_command.command('get-list')
def get_states(address, limit, head, reverse, node_url):
    """
    Get a list of states.
    """
    arguments, errors = GetStateListForm().load({
        'address': address,
        'limit': limit,
        'head': head,
        'reverse': reverse,
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    address = arguments.get('address')
    limit = arguments.get('limit')
    head = arguments.get('head')
    reverse = arguments.get('reverse')
    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = State(service=remme).get_list(
        address=address, limit=limit, head=head, reverse=reverse,
    )

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
