"""
Provide tests for command line interface's node get information command.
"""
import json

import pytest
from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_27_IN_TESTNET_ADDRESS,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


def test_get_node_info():
    """
    Case: get information about synchronization and peer count of the node.
    Expect: the flag is synced and peer count are returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-info',
        '--node-url',
        NODE_27_IN_TESTNET_ADDRESS,
    ])

    node_information = json.loads(result.output).get('result').get('information')

    node_is_synced = node_information.get('is_synced')
    node_peer_count = node_information.get('peer_count')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(node_is_synced, bool)
    assert isinstance(node_peer_count, int)


def test_get_node_info_without_node_url(mocker, node_information):
    """
    Case: get information about synchronization and peer count of the node without passing node URL.
    Expect: the flag is synced and peer count are returned from a node on localhost
    """
    mock_node_get_info = mocker.patch('cli.node.service.loop.run_until_complete')
    mock_node_get_info.return_value = node_information

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-info',
    ])

    expected_node_information = {
        'result': {
            'information': node_information.data,
        },
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_node_information == json.loads(result.output)


def test_get_node_info_invalid_node_url():
    """
    Case: get information about synchronization and peer count of the node by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-info',
        '--node-url',
        invalid_node_url,
    ])

    expected_error = {
        'errors': {
            'node_url': [
                f'The following node URL `{invalid_node_url}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_node_info_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get information about synchronization and peer count of the node by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-info',
        '--node-url',
        node_url_with_protocol,
    ])

    expected_error = {
        'errors': {
            'node_url': [
                f'Pass the following node URL `{node_url_with_protocol}` without protocol (http, https, etc.).',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_node_info_non_existing_node_url():
    """
    Case: get information about synchronization and peer count of the node by passing non-existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-info',
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
