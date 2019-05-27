"""
Provide tests for command line interface's node account transfer tokens from unfrozen to operational balance.
"""
import json

import pytest
from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    INCORRECT_ENTERED_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


def test_transfer_tokens_from_unfrozen_to_operational(mocker, transaction):
    """
    Case: transfer tokens from unfrozen reputational balance to operational balance.
    Expect: transaction's batch identifier is returned.
    """
    mock_get_node_private_key = mocker.patch('cli.config.NodePrivateKey.get')
    mock_get_node_private_key.return_value = '42dada12f863528bd456785d8c544154db6ec9455be2c123d91b687df3697314'

    mock_node_account_transfer_tokens_from_unfrozen_to_operational = \
        mocker.patch('cli.node_account.service.loop.run_until_complete')
    mock_node_account_transfer_tokens_from_unfrozen_to_operational.return_value = transaction

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'transfer-tokens-from-unfrozen-to-operational',
        '--amount',
        1000,
    ])

    transaction_batch_identifier = json.loads(result.output).get('result').get('batch_identifier')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert transaction.batch_id == transaction_batch_identifier


def test_transfer_tokens_from_unfrozen_to_operational_invalid_amount(mocker, transaction):
    """
    Case: transfer tokens from unfrozen reputational balance to operational balance with invalid amount.
    Expect: amount is not a valid integer error message.
    """
    invalid_amount = 'je682'

    mock_get_node_private_key = mocker.patch('cli.config.NodePrivateKey.get')
    mock_get_node_private_key.return_value = '42dada12f863528bd456785d8c544154db6ec9455be2c123d91b687df3697314'

    mock_node_account_transfer_tokens_from_unfrozen_to_operational = \
        mocker.patch('cli.node_account.service.loop.run_until_complete')
    mock_node_account_transfer_tokens_from_unfrozen_to_operational.return_value = transaction

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'transfer-tokens-from-unfrozen-to-operational',
        '--amount',
        invalid_amount,
    ])

    assert INCORRECT_ENTERED_COMMAND_CODE == result.exit_code
    assert f'{invalid_amount} is not a valid integer' in result.output


@pytest.mark.parametrize('insufficient_amount', [-1, 0])
def test_transfer_tokens_from_unfrozen_to_operational_insufficient_amount(mocker, transaction, insufficient_amount):
    """
    Case: transfer tokens from unfrozen reputational balance to operational balance with insufficient amount.
    Expect: amount must be greater than 0 error message.
    """
    mock_get_node_private_key = mocker.patch('cli.config.NodePrivateKey.get')
    mock_get_node_private_key.return_value = '42dada12f863528bd456785d8c544154db6ec9455be2c123d91b687df3697314'

    mock_node_account_transfer_tokens_from_unfrozen_to_operational = \
        mocker.patch('cli.node_account.service.loop.run_until_complete')
    mock_node_account_transfer_tokens_from_unfrozen_to_operational.return_value = transaction

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'transfer-tokens-from-unfrozen-to-operational',
        '--amount',
        insufficient_amount,
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
