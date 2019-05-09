"""
Provide tests for command line interface's node account information by its address commands.
"""
import json

import pytest
from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json

NODE_ACCOUNT_ADDRESS_PRESENTED_ON_THE_TEST_NODE = \
    '1168290a2cbbce30382d9420fd5f8b0ec75e953e5c695365b1c22862dce713fa1e48ca'


def test_get_information_with_address():
    """
    Case: get information about the node account by its address.
    Expect: information about the node account is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'get',
        '--address',
        NODE_ACCOUNT_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        'node-1-testnet.remme.io',
    ])

    node_account_information = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(node_account_information.get('min'), bool)
    assert isinstance(node_account_information.get('reputation'), dict)
    assert isinstance(node_account_information.get('shares'), list)


def test_get_information_without_node_url(mocker, node_account_information):
    """
    Case: get information about the node account without passing node URL.
    Expect: information about the node account is returned from node on localhost.
    """
    mock_node_account_get_info = mocker.patch('cli.atomic_swap.service.loop.run_until_complete')
    mock_node_account_get_info.return_value = node_account_information

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'get',
        '--address',
        NODE_ACCOUNT_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
    ])

    expected_result = {
        'result': node_account_information.node_account_response,
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output)


def test_get_information_invalid_address():
    """
    Case: get information about the node account by invalid address.
    Expect: the following address is not valid error message.
    """
    invalid_address = '1168290a2cbbce30382d9420fd5f8b0ec75e953e5c695365b1c22862dce713fa1e48zz'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'get',
        '--address',
        invalid_address,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': {
            'address': [
                f'The following address `{invalid_address}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_information_invalid_node_url():
    """
    Case: get information about the node account by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'get',
        '--address',
        NODE_ACCOUNT_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
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


def test_get_information_non_existing_address():
    """
    Case: get information about the node account by passing non-existing address.
    Expect: resource not found is returned.
    """
    non_existing_address = '1168290a2cbbce30382d9420fd5f8b0ec75e953e5c695365b1c22862dce713fa1e48cc'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'get',
        '--address',
        non_existing_address,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': 'Resource not found',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_information_non_existing_node_url():
    """
    Case: get information about the node account by passing non-existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'get',
        '--address',
        NODE_ACCOUNT_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_information_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get information about the node account by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'get',
        '--address',
        NODE_ACCOUNT_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
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
