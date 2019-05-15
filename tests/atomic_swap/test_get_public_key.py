"""
Provide tests for command line interface's get public key of the atomic swap commands.
"""
import json
import re

import pytest
from click.testing import CliRunner

from cli.constants import (
    DEV_CONSENSUS_GENESIS_NODE_IP_ADDRESS_FOR_TESTING,
    FAILED_EXIT_FROM_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
    PUBLIC_KEY_REGEXP,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


def test_get_public_key():
    """
    Case: get the public key of atomic swap.
    Expect: public key is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-public-key',
        '--node-url',
        DEV_CONSENSUS_GENESIS_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    public_key = json.loads(result.output).get('result').get('public_key')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert re.match(pattern=PUBLIC_KEY_REGEXP, string=public_key) is not None


def test_get_public_key_without_node_url(mocker):
    """
    Case: get the public key of atomic swap without passing node URL.
    Expect: public key is returned from node on localhost.
    """
    public_key = '03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad'
    mock_swap_get_public_key = mocker.patch('cli.node.service.loop.run_until_complete')
    mock_swap_get_public_key.return_value = public_key

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-public-key',
    ])

    expected_result = {
        'result': {
            'public_key': public_key,
        },
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output)


def test_get_public_key_invalid_node_url():
    """
    Case: get the public key of atomic swap by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-public-key',
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
def test_get_public_key_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get the public key of atomic swap by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-public-key',
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


def test_get_public_key_non_existing_node_url():
    """
    Case: get the public key of atomic swap by passing non-existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-public-key',
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
