"""
Provide tests for command line interface's node get configurations command.
"""
import json
import re

import pytest
from click.testing import CliRunner

from cli.constants import (
    ADDRESS_REGEXP,
    DEV_CONSENSUS_GENESIS_NODE_IP_ADDRESS_FOR_TESTING,
    FAILED_EXIT_FROM_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
    PUBLIC_KEY_REGEXP,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


def test_get_node_configs():
    """
    Case: get node configurations.
    Expect: node public key and address are returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-configs',
        '--node-url',
        DEV_CONSENSUS_GENESIS_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    node_configurations = json.loads(result.output).get('result').get('configurations')

    node_address = node_configurations.get('node_address')
    node_public_key = node_configurations.get('node_public_key')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert re.match(pattern=ADDRESS_REGEXP, string=node_address) is not None
    assert re.match(pattern=PUBLIC_KEY_REGEXP, string=node_public_key) is not None


def test_get_node_configs_without_node_url(mocker, node_configurations):
    """
    Case: get node configurations without passing node URL.
    Expect: batch identifier is returned from a node on localhost.
    """
    mock_get_node_configs = mocker.patch('cli.node.service.loop.run_until_complete')
    mock_get_node_configs.return_value = node_configurations

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-configs',
    ])

    expected_node_configurations = {
        'result': {
            'configurations': node_configurations.data,
        },
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_node_configurations == json.loads(result.output)


def test_get_node_configs_invalid_node_url():
    """
    Case: get node configurations by passing an invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-configs',
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
def test_get_node_configs_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get node configurations by passing node URL with an explicit protocol.
    Expect: the following node URL contains a protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-configs',
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


def test_get_node_configs_non_existing_node_url():
    """
    Case: get node configurations by passing the non-existing node URL.
    Expect: check if node running at the URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-configs',
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
