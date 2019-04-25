"""
Provide tests for command line interface's public key get public keys addresses commands.
"""
import json
import re

from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
    PUBLIC_KEY_ADDRESS_REGEXP,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json

ADDRESS_PRESENTED_ON_THE_TEST_NODE = '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf'


def test_get_public_keys():
    """
    Case: get a list of the addresses of the public keys by account address.
    Expect: list of the addresses of the public keys, each public key address matched regexp checking.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-list',
        '--address',
        ADDRESS_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    public_key_addresses = json.loads(result.output).get('result').get('public_key_addresses')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    for public_key in public_key_addresses:
        assert re.match(pattern=PUBLIC_KEY_ADDRESS_REGEXP, string=public_key) is not None


def test_get_public_keys_invalid_address():
    """
    Case: get a list of the addresses of the public keys by invalid address.
    Expect: the following address is not valid error message.
    """
    invalid_address = '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3zz'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key', 'get-list', '--address', invalid_address, '--node-url', NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': {
            'address': [
                f'The following address `{invalid_address}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_public_keys_without_node_url(mocker):
    """
    Case: get a list of the addresses of the public keys without passing node URL.
    Expect: list of the addresses of the public keys is returned from node on localhost.
    """
    public_key_addresses = [
        'a23be14785e7b073b50e24f72e086675289795b969a895a7f02202404086946e8ddc5b',
        'a23be17265e8393dd9ae7a46f1be662f86130c434fd54576a7d92b678e5c30de4f677f',
    ]

    mock_public_key_get_public_keys = mocker.patch('cli.public_key.service.loop.run_until_complete')
    mock_public_key_get_public_keys.return_value = public_key_addresses

    runner = CliRunner()
    result = runner.invoke(cli, ['public-key', 'get-list', '--address', ADDRESS_PRESENTED_ON_THE_TEST_NODE])

    expected_result = {
        'result': {
            'public_key_addresses': public_key_addresses,
        },
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output)


def test_get_public_keys_invalid_node_url():
    """
    Case: get a list of the addresses of the public keys by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-list',
        '--address',
        ADDRESS_PRESENTED_ON_THE_TEST_NODE,
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


def test_get_public_keys_node_url_with_http():
    """
    Case: get a list of the addresses of the public keys by passing node URL with explicit HTTP protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_http_protocol = 'http://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-list',
        '--address',
        ADDRESS_PRESENTED_ON_THE_TEST_NODE,
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


def test_get_public_keys_node_url_with_https():
    """
    Case: get a list of the addresses of the public keys by passing node URL with explicit HTTPS protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_https_protocol = 'https://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-list',
        '--address',
        ADDRESS_PRESENTED_ON_THE_TEST_NODE,
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


def test_get_public_keys_non_existing_address():
    """
    Case: get a list of the addresses of the public keys by passing non existing address.
    Expect: empty list of the addresses of the public keys is returned.
    """
    non_existing_address = '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3c1'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-list',
        '--address',
        non_existing_address,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    public_key_addresses = json.loads(result.output).get('result').get('public_key_addresses')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(public_key_addresses, list)
    assert public_key_addresses == []


def test_get_public_keys_non_existing_node_url():
    """
    Case: get a list of the addresses of the public keys by passing non existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-list',
        '--address',
        ADDRESS_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
