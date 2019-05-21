"""
Provide tests for command line interface's masternode set bet command.
"""
import json

from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


def test_set_bet(mocker, set_bet_masternode_transaction):
    """
    Case: set masternode betting behaviour.
    Expect: betting masternode transaction's batch identifier is returned.
    """
    mock_get_node_private_key = mocker.patch('cli.config.NodePrivateKey.get')
    mock_get_node_private_key.return_value = '42dada12f863528bd456785d8c544154db6ec9455be2c123d91b687df3697314'

    mock_set_bet_masternode = mocker.patch('cli.masternode.service.loop.run_until_complete')
    mock_set_bet_masternode.return_value = set_bet_masternode_transaction

    runner = CliRunner()
    result = runner.invoke(cli, [
        'masternode',
        'set-bet',
        '--bet',
        'MAX',
    ])

    set_bet_masternode_transaction_identifier = json.loads(result.output).get('result').get('batch_id')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert set_bet_masternode_transaction.batch_id == set_bet_masternode_transaction_identifier


def test_set_bet_with_invalid_bet():
    """
    Case: set masternode with invalid betting behaviour.
    Expect: the following bet is not a valid error message.
    """
    invalid_bet = 'qwqwqwq'

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
