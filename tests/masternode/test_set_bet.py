"""
Provide tests for command line interface's masternode set bet command.
"""
import json

import pytest
from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


@pytest.mark.parametrize('bet', ['max', 'min', '2'])
def test_set_bet_masternode(mocker, transaction, bet):
    """
    Case: set the masternode betting behaviour.
    Expect: betting masternode transaction's batch identifier is returned.
    """
    mock_get_node_private_key = mocker.patch('cli.config.NodePrivateKey.get')
    mock_get_node_private_key.return_value = '42dada12f863528bd456785d8c544154db6ec9455be2c123d91b687df3697314'

    mock_set_bet_masternode = mocker.patch('cli.masternode.service.loop.run_until_complete')
    mock_set_bet_masternode.return_value = transaction

    runner = CliRunner()
    result = runner.invoke(cli, [
        'masternode',
        'set-bet',
        '--bet',
        bet,
    ])

    masternode_set_bet_transaction_identifier = json.loads(result.output).get('result').get('batch_id')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert transaction.batch_id == masternode_set_bet_transaction_identifier


@pytest.mark.parametrize('invalid_bet', ['-1', 'qwqwqwq'])
def test_set_bet_masternode_with_invalid_bet(invalid_bet):
    """
    Case: set the masternode with invalid betting behaviour.
    Expect: the following bet is not a valid error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'masternode',
        'set-bet',
        '--bet',
        invalid_bet,
    ])

    expected_error = {
        'errors': {
            'bet': [
                f'The following bet `{invalid_bet}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


@pytest.mark.parametrize('non_supported_bet', ['0', '10'])
def test_set_bet_masternode_with_non_supported_bet(mocker, non_supported_bet):
    """
    Case: set the masternode with non supported bet.
    Expect: the following bet is not a valid error message.
    """
    mock_get_node_private_key = mocker.patch('cli.config.NodePrivateKey.get')
    mock_get_node_private_key.return_value = '42dada12f863528bd456785d8c544154db6ec9455be2c123d91b687df3697314'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'masternode',
        'set-bet',
        '--bet',
        non_supported_bet,
    ])

    expected_error = {
        'errors': f'The following bet {non_supported_bet} is not supported to be set as masternode betting behavior.',

    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_set_bet_masternode_without_private_key():
    """
    Case: set the masternode without private key.
    Expect: the private key hasn't been founded on the machine error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'masternode',
        'set-bet',
        '--bet',
        '1',
    ])

    expected_error = {
        'errors': 'Private key hasn\'t been founded on the machine.',

    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
