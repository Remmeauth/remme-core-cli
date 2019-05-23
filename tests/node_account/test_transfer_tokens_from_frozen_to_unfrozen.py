"""
Provide tests for command line interface's node account transfer tokens from frozen to unfrozen operational balances.
"""
import json

from click.testing import CliRunner

from cli.constants import PASSED_EXIT_FROM_COMMAND_CODE
from cli.entrypoint import cli


def test_transfer_tokens_from_frozen_to_unfrozen(mocker, transaction):
    """
    Case: transfer available tokens from frozen to unfrozen.
    Expect: transaction's batch identifier is returned.
    """
    mock_get_node_private_key = mocker.patch('cli.config.NodePrivateKey.get')
    mock_get_node_private_key.return_value = '42dada12f863528bd456785d8c544154db6ec9455be2c123d91b687df3697314'

    mock_node_account_transfer_tokens_from_frozen_to_unfrozen = \
        mocker.patch('cli.node_account.service.loop.run_until_complete')
    mock_node_account_transfer_tokens_from_frozen_to_unfrozen.return_value = transaction

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node-account',
        'transfer-tokens-from-frozen-to-unfrozen',
    ])

    transaction_batch_identifier = json.loads(result.output).get('result').get('batch_identifier')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert transaction.batch_id == transaction_batch_identifier
