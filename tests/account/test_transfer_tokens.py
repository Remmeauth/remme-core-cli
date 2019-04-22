"""
Provide tests for command line interface's account transfer tokens command.
"""
import json
import re

from click.testing import CliRunner

from cli.constants import (
    BATCH_ID_REGEXP,
    FAILED_EXIT_FROM_COMMAND_CODE,
    INCORRECT_ENTERED_COMMAND_CODE,
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
    PRIVATE_KEY_FOR_TESTING,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


def test_transfer_tokens():
    """
    Case: transfer tokens to address.
    Expect: batch identifier is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    batch_id = json.loads(result.output).get('batch_id')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert re.match(pattern=BATCH_ID_REGEXP, string=batch_id) is not None


def test_transfer_tokens_invalid_private_key_from():
    """
    Case: transfer tokens to address with invalid private key from..
    Expect: the following private key is invalid error message.
    """
    invalid_private_key = 'b03e31d2f310305eab249133b53b5fb327'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key-from',
        invalid_private_key,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'private_key_from': [
            f'The following private key `{invalid_private_key}` is invalid.',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_transfer_tokens_invalid_address_to():
    """
    Case: transfer tokens to invalid address.
    Expect: the following address to is invalid error message.
    """
    invalid_address_to = '1120076ecf036e857f42129b5830'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--address-to',
        invalid_address_to,
        '--amount',
        '1000',
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'address_to': [
            f'The following address `{invalid_address_to}` is invalid.',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_transfer_tokens_invalid_amount():
    """
    Case: transfer tokens to address with invalid amount.
    Expect: amount is not a valid integer error message.
    """
    invalid_amount = 'je682'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        invalid_amount,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert INCORRECT_ENTERED_COMMAND_CODE == result.exit_code
    assert f'{invalid_amount} is not a valid integer' in result.output


def test_transfer_tokens_without_node_url(mocker):
    """
    Case: transfer tokens to address without passing node URL.
    Expect: batch identifier is returned from node on localhost.
    """
    transfer_tokens_info = {
        'batch_id': '37809770b004dcbc7dae116fd9f17428255ddddee3304c9b3d14609d2792e78f'
                    '08f5308af03fd4aa18ff1d868f043b12dd7b0a792e141f000a2505acd4b7a956',
    }, None

    mock_account_transfer_tokens = mocker.patch('cli.account.service.Account.transfer_tokens')
    mock_account_transfer_tokens.return_value = transfer_tokens_info

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
    ])

    batch_id = json.loads(result.output).get('batch_id')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert re.match(pattern=BATCH_ID_REGEXP, string=batch_id) is not None


def test_transfer_tokens_invalid_node_url():
    """
    Case: transfer tokens to address by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
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


def test_transfer_tokens_node_url_with_http():
    """
    Case: transfer tokens to address by passing node URL with explicit HTTP protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_http_protocol = 'http://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
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


def test_transfer_tokens_node_url_with_https():
    """
    Case: transfer tokens to address by passing node URL with explicit HTTPS protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_https_protocol = 'https://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
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