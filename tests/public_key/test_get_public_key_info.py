"""
Provide tests for command line interface's public key information commands.
"""
import json
import re

import pytest
from click.testing import CliRunner

from cli.constants import (
    ADDRESS_REGEXP,
    DEV_CONSENSUS_GENESIS_NODE_IP_ADDRESS_FOR_TESTING,
    FAILED_EXIT_FROM_COMMAND_CODE,
    HEADER_SIGNATURE_REGEXP,
    PASSED_EXIT_FROM_COMMAND_CODE,
    PUBLIC_KEY_REGEXP,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json

PUBLIC_KEY_ADDRESS_PRESENTED_ON_THE_TEST_NODE = \
    'a23be1a8c94d4a06d3dc8fa8f3df543d87ae79b3bf59cbae37490e1534393048873070'


def test_get_public_key_info():
    """
    Case: get information about public key by its address.
    Expect: dictionary of public key information, keys matched regexp checking.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-info',
        '--address',
        PUBLIC_KEY_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        DEV_CONSENSUS_GENESIS_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    public_key_info = json.loads(result.output).get('result').get('information')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert re.match(pattern=ADDRESS_REGEXP, string=public_key_info.get('address')) is not None
    assert re.match(pattern=HEADER_SIGNATURE_REGEXP, string=public_key_info.get('entity_hash')) is not None
    assert re.match(pattern=PUBLIC_KEY_REGEXP, string=public_key_info.get('owner_public_key')) is not None
    assert isinstance(public_key_info.get('valid_from'), int)
    assert isinstance(public_key_info.get('valid_to'), int)
    assert isinstance(public_key_info.get('is_revoked'), bool)
    assert isinstance(public_key_info.get('is_valid'), bool)


def test_get_public_key_info_invalid_address():
    """
    Case: get information about public key by invalid address.
    Expect: the following public key address is not valid error message.
    """
    invalid_address = 'a23be14785e7b073b50e24f72e086675289795b969a895a7f02202404086946e8ddczz'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-info',
        '--address',
        invalid_address,
        '--node-url',
        DEV_CONSENSUS_GENESIS_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': {
            'address': [
                f'The following public key address `{invalid_address}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_public_key_info_without_node_url(mocker, public_key_information):
    """
    Case: get information about public key without passing node URL.
    Expect: dictionary of public key information is returned from node on localhost.
    """
    mock_public_key_get_info = mocker.patch('cli.public_key.service.loop.run_until_complete')
    mock_public_key_get_info.return_value = public_key_information

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-info',
        '--address',
        PUBLIC_KEY_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
    ])

    expected_result = {
        'result': {
            'information': public_key_information.data,
        },
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output)


def test_get_public_key_info_invalid_node_url():
    """
    Case: get information about public key by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-info',
        '--address',
        PUBLIC_KEY_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
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
def test_get_public_key_info_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get information about public key by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-list',
        '--address',
        PUBLIC_KEY_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
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


def test_get_public_key_info_non_existing_address():
    """
    Case: get information about public key by passing non-existing address.
    Expect: public key information not found error message.
    """
    non_existing_address = 'a23be14785e7b073b50e24f72e086675289795b969a895a7f02202404086946e8ddc5c'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-info',
        '--address',
        non_existing_address,
        '--node-url',
        DEV_CONSENSUS_GENESIS_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': 'Public key info not found',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_public_key_info_non_existing_node_url():
    """
    Case: get information about public key by passing non-existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-info',
        '--address',
        PUBLIC_KEY_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
