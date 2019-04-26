"""
Provide implementation of the command line interface's node commands.
"""
import sys

import click
from remme import Remme

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_URL_ARGUMENT_HELP_MESSAGE,
)
from cli.node.forms import (
    GetNodeConfigurationsForm,
    GetNodePeersForm,
)
from cli.node.service import Node
from cli.utils import (
    default_node_url,
    print_errors,
    print_result,
)


@click.group('node', chain=True)
def node_commands():
    """
    Provide commands for working with node.
    """
    pass


@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@node_commands.command('get-configs')
def get_config(node_url):
    """
    Get node configurations.
    """
    arguments, errors = GetNodeConfigurationsForm().load({
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = Node(service=remme).get_configs()

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)


@click.option('--node-url', type=str, required=False, help=NODE_URL_ARGUMENT_HELP_MESSAGE, default=default_node_url())
@node_commands.command('get-peers')
def get_peers(node_url):
    """
    Get the node's peers.
    """
    arguments, errors = GetNodePeersForm().load({
        'node_url': node_url,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    node_url = arguments.get('node_url')

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })

    result, errors = Node(service=remme).get_peers()

    if errors is not None:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(result=result)
