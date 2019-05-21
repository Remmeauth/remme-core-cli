"""
Provide tests for command line interface's node open command.
"""
import json

from click.testing import CliRunner

from cli.constants import PASSED_EXIT_FROM_COMMAND_CODE
from cli.entrypoint import cli


def test_open_node(mocker, open_node_transaction):
    """
    Case: open the node.
    Expect: opening node transaction's batch identifier is returned.
    """
    mock_mock_get_node_private_key = mocker.patch('cli.config.NodePrivateKey.get')
    mock_mock_get_node_private_key.return_value = '42dada12f863528bd456785d8c544154db6ec9455be2c123d91b687df3697314'

    mock_open_masternode = mocker.patch('cli.node.service.loop.run_until_complete')
    mock_open_masternode.return_value = open_node_transaction

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'open',
    ])

    node_open_transaction_identifier = json.loads(result.output).get('result').get('batch_id')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert open_node_transaction.batch_id == node_open_transaction_identifier
