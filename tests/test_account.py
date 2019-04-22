"""
Provide tests for command line interface's account commands.
"""
import json

from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import (
    dict_to_pretty_json,
    return_async_value,
)


def test_get_balance():
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
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), int)


def test_get_balance_invalid_address():
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
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'address': [
            f'The following address `{invalid_address}` is invalid.',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_balance_without_node_url(mocker):
    """
    Case: get a balance of an account by address without passing node URL.
    Expect: balance is returned.
    """
    balance_from_localhost = 13500

    mock_account_get_balance = mocker.patch('cli.account.service.Account.get_balance')
    mock_account_get_balance.return_value = return_async_value(balance_from_localhost)

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), int)
    assert str(balance_from_localhost) in result.output


def test_get_balance_invalid_node_url():
    """
    Case: get a balance of an account by passing invalid node URL.
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
        'node_url': [
            f'The following node URL `{invalid_node_url}` is invalid.',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_balance_node_url_with_http():
    """
    Case: get a balance of an account by passing node URL with explicit HTTP protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_http_protocol = 'http://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
        '--node-url',
        node_url_with_http_protocol,
    ])

    expected_error = {
        'node_url': [
            f'Pass the following node URL `{node_url_with_http_protocol}` without protocol (http, https, etc.).',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_balance_node_url_with_https():
    """
    Case: get a balance of an account by passing node URL with explicit HTTPS protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_https_protocol = 'https://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
        '--node-url',
        node_url_with_https_protocol,
    ])

    expected_error = {
        'node_url': [
            f'Pass the following node URL `{node_url_with_https_protocol}` without protocol (http, https, etc.).',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
