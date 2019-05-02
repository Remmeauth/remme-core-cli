"""
Provide tests for command line interface's node get peers command.
"""
import json

from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_27_IN_TESTNET_ADDRESS,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


def test_get_node_peers_configs():
    """
    Case: get the node's peers.
    Expect: node peers are returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-peers',
        '--node-url',
        NODE_27_IN_TESTNET_ADDRESS,
    ])

    peers = json.loads(result.output).get('result').get('peers')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    for peer in peers:
        assert 'tcp://' in peer
        assert ':8800' in peer


def test_get_node_peers_without_node_url(mocker):
    """
    Case: get the node's peers without passing node URL.
    Expect: node peers are returned from node on localhost.
    """
    peers = [
        'tcp://node-26-testnet.remme.io:8800',
        'tcp://node-12-testnet.remme.io:8800',
        'tcp://node-4-testnet.remme.io:8800',
        'tcp://node-13-testnet.remme.io:8800',
        'tcp://node-18-testnet.remme.io:8800',
    ]

    mock_get_node_peers = mocker.patch('cli.node.service.loop.run_until_complete')
    mock_get_node_peers.return_value = peers

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-peers',
    ])

    expected_node_peers = {
        'result': {
            'peers': peers,
        },
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_node_peers == json.loads(result.output)


def test_get_node_peers_invalid_node_url():
    """
    Case: get the node's peers by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-peers',
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


def test_get_node_peers_node_url_with_http():
    """
    Case: get the node's peers by passing node URL with explicit HTTP protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_http_protocol = 'http://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-peers',
        '--node-url',
        node_url_with_http_protocol,
    ])

    expected_error = {
        'errors': {
            'node_url': [
                f'Pass the following node URL `{node_url_with_http_protocol}` without protocol (http, https, etc.).',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_node_peers_node_url_with_https():
    """
    Case: get the node's peers by passing node URL with explicit HTTPS protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_https_protocol = 'https://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-peers',
        '--node-url',
        node_url_with_https_protocol,
    ])

    expected_error = {
        'errors': {
            'node_url': [
                f'Pass the following node URL `{node_url_with_https_protocol}` without protocol (http, https, etc.).',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_node_peers_non_existing_node_url():
    """
    Case: get the node's peers by passing non existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-peers',
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output