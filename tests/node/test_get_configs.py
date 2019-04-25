"""
Provide tests for command line interface's node get configurations command.
"""
import json

from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
    RELEASE_0_9_0_ALPHA_NODE_ADDRESS,
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
        RELEASE_0_9_0_ALPHA_NODE_ADDRESS,
    ])

    expected_node_configurations = {
        'result': {
            'configurations': {
                'node_address': '116829f18683f6c30146559c9cb8d5d302545019ff00f2ab72500df99bceb7b81a1dad',
                'node_public_key': '0350e9cf23966ad404dc56438fd01ec11a913446cfd7c4fb8d95586a58718431e7',
            },
        },
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_node_configurations == json.loads(result.output)


def test_get_node_configs_without_node_url(mocker, node_configurations):
    """
    Case: get node configurations without passing node URL.
    Expect: batch identifier is returned from node on localhost.
    """
    mock_account_get_balance = mocker.patch('cli.node.service.loop.run_until_complete')
    mock_account_get_balance.return_value = node_configurations

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
    Case: get node configurations by passing invalid node URL.
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


def test_get_node_configs_node_url_with_http():
    """
    Case: get node configurations by passing node URL with explicit HTTP protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_http_protocol = 'http://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-configs',
        '--node-url',
        node_url_with_http_protocol,
    ])

    expected_error = {
        'errors': {
            'node_url': [
                f'Pass the following node URL `{node_url_with_http_protocol}` without protocol (http, https, etc.).',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_node_configs_node_url_with_https():
    """
    Case: get node configurations by passing node URL with explicit HTTPS protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_https_protocol = 'https://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-configs',
        '--node-url',
        node_url_with_https_protocol,
    ])

    expected_error = {
        'errors': {
            'node_url': [
                f'Pass the following node URL `{node_url_with_https_protocol}` without protocol (http, https, etc.).',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_node_configs_non_existing_node_url():
    """
    Case: get node configurations by passing non existing node URL.
    Expect: check if node running at URL error message.
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
