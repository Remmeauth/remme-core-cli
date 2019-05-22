"""
Provide tests for command line interface's masternode close command.
"""
import json

from click.testing import CliRunner

from cli.constants import PASSED_EXIT_FROM_COMMAND_CODE
from cli.entrypoint import cli


def test_close_node(mocker, close_masternode_transaction):
    """
    Case: close the masternode.
    Expect: close masternode transaction's batch identifier is returned.
    """
    mock_mock_get_node_private_key = mocker.patch('cli.config.NodePrivateKey.get')
    mock_mock_get_node_private_key.return_value = '42dada12f863528bd456785d8c544154db6ec9455be2c123d91b687df3697314'

    mock_close_masternode = mocker.patch('cli.node.service.loop.run_until_complete')
    mock_close_masternode.return_value = close_masternode_transaction

    runner = CliRunner()
    result = runner.invoke(cli, [
        'masternode',
        'close',
    ])

    node_close_transaction_identifier = json.loads(result.output).get('result').get('batch_id')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert close_masternode_transaction.batch_id == node_close_transaction_identifier
