"""
Provide tests for command line interface's account get balance command.
"""
import json

import pytest
from click.testing import CliRunner

from cli.constants import (
    DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    FAILED_EXIT_FROM_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


def test_get_account_balance():
    """
    Case: get a balance of an account by address.
    Expect: balance is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    balance = json.loads(result.output).get('result').get('balance')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(balance, int)


def test_get_account_balance_invalid_address():
    """
    Case: get a balance of an account by invalid address.
    Expect: the following address is invalid error message.
    """
    invalid_address = '1120076ecf036e857f42129b5830'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        invalid_address,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
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


def test_get_account_balance_without_node_url(mocker):
    """
    Case: get a balance of an account by address without passing node URL.
    Expect: balance is returned from a node on localhost.
    """
    balance = 13500

    mock_account_get_balance = mocker.patch('cli.account.service.loop.run_until_complete')
    mock_account_get_balance.return_value = balance

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
    ])

    expected_result = {
        'result': {
            'balance': 13500,
        },
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output)


def test_get_account_balance_invalid_node_url():
    """
    Case: get a balance of an account by passing an invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
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
def test_get_account_balance_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get a balance of an account by passing node URL with an explicit protocol.
    Expect: the following node URL contains a protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
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


def test_get_account_balance_non_existing_node_url():
    """
    Case: get a balance of an account by passing the non-existing node URL.
    Expect: check if node running at the URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
