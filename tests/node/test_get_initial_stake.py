"""
Provide tests for command line interface's node get initial stake command.
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


def test_get_initial_stake():
    """
    Case: get the initial stake of the node.
    Expect: the initial stake is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-initial-stake',
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    node_initial_stake = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(node_initial_stake, int)


def test_get_initial_stake_without_node_url(mocker):
    """
    Case: get the initial stake of the node without passing node URL.
    Expect: the initial stake is returned from a node on localhost.
    """
    initial_stake = 250000

    mock_node_get_initial_stake = mocker.patch('cli.node.service.loop.run_until_complete')
    mock_node_get_initial_stake.return_value = initial_stake

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-initial-stake',
    ])

    expected_node_initial_stake = {
        'result': initial_stake,
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_node_initial_stake == json.loads(result.output)


def test_get_initial_stake_invalid_node_url():
    """
    Case: get the initial stake of the node by passing an invalid node URL.
    Expect: the following node URL is an invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-initial-stake',
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


def test_get_initial_stake_non_existing_node_url():
    """
    Case: get the initial stake of the node by passing the non-existing node URL.
    Expect: check if node running at the URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-initial-stake',
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_initial_stake_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get the initial stake of the node by passing node URL with an explicit protocol.
    Expect: the following node URL contains the protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-initial-stake',
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
