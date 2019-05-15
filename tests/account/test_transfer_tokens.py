"""
Provide tests for command line interface's account transfer tokens command.
"""
import json
import re

import pytest
from click.testing import CliRunner

from cli.constants import (
    BATCH_ID_REGEXP,
    DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    DEV_BRANCH_NODE_PRIVATE_KEY_WITH_MONEY,
    FAILED_EXIT_FROM_COMMAND_CODE,
    INCORRECT_ENTERED_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
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
        '--private-key',
        DEV_BRANCH_NODE_PRIVATE_KEY_WITH_MONEY,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    batch_id = json.loads(result.output).get('result').get('batch_identifier')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert re.match(pattern=BATCH_ID_REGEXP, string=batch_id) is not None


def test_transfer_tokens_invalid_private_key():
    """
    Case: transfer tokens to address with invalid private key.
    Expect: the following private key is invalid error message.
    """
    invalid_private_key = 'b03e31d2f310305eab249133b53b5fb327'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key',
        invalid_private_key,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': {
            'private_key': [
                f'The following private key `{invalid_private_key}` is invalid.',
            ],
        },
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
        '--private-key',
        DEV_BRANCH_NODE_PRIVATE_KEY_WITH_MONEY,
        '--address-to',
        invalid_address_to,
        '--amount',
        '1000',
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': {
            'address_to': [
                f'The following address `{invalid_address_to}` is invalid.',
            ],
        },
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
        '--private-key',
        DEV_BRANCH_NODE_PRIVATE_KEY_WITH_MONEY,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        invalid_amount,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert INCORRECT_ENTERED_COMMAND_CODE == result.exit_code
    assert f'{invalid_amount} is not a valid integer' in result.output


@pytest.mark.parametrize('insufficient_amount', [-1, 0])
def test_transfer_tokens_with_insufficient_amount(insufficient_amount):
    """
    Case: transfer tokens to address with insufficient amount.
    Expect: amount must be greater than 0 error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key',
        DEV_BRANCH_NODE_PRIVATE_KEY_WITH_MONEY,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        insufficient_amount,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': {
            'amount': [
                f'Amount must be greater than 0.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_transfer_tokens_without_node_url(mocker, sent_transaction):
    """
    Case: transfer tokens to address without passing node URL.
    Expect: batch identifier is returned from node on localhost.
    """
    mock_account_transfer_tokens = mocker.patch('cli.account.service.loop.run_until_complete')
    mock_account_transfer_tokens.return_value = sent_transaction

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key',
        DEV_BRANCH_NODE_PRIVATE_KEY_WITH_MONEY,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
    ])

    batch_id = json.loads(result.output).get('result').get('batch_identifier')

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
        '--private-key',
        DEV_BRANCH_NODE_PRIVATE_KEY_WITH_MONEY,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
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
def test_transfer_tokens_node_url_with_protocol(node_url_with_protocol):
    """
    Case: transfer tokens to address by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key',
        DEV_BRANCH_NODE_PRIVATE_KEY_WITH_MONEY,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
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


def test_transfer_tokens_non_existing_node_url():
    """
    Case: transfer tokens to address by passing non-existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'transfer-tokens',
        '--private-key',
        DEV_BRANCH_NODE_PRIVATE_KEY_WITH_MONEY,
        '--address-to',
        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
        '--amount',
        '1000',
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
