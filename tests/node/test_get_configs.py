"""
Provide tests for command line interface's node get configurations command.
"""
import json

from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    LATEST_RELEASE_NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
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
        LATEST_RELEASE_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_node_configurations = {
        'result': {
            'configurations': {
                'node_address': '11682919ed54658edf965f955a5783e6a653ce3bb411b99c8afe9f6e5840af45171774',
                'node_public_key': '03725231d64d1b379a1d855d0e7614684744ba915bd657e398f5a5cefc9ced896d',
            }
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
