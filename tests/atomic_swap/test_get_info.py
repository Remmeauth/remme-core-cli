"""
Provide tests for command line interface's atomic swap commands.
"""
import json
import re

import pytest
from click.testing import CliRunner

from cli.constants import (
    ADDRESS_REGEXP,
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_27_IN_TESTNET_ADDRESS,
    PASSED_EXIT_FROM_COMMAND_CODE,
    SWAP_IDENTIFIER_REGEXP,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json

SWAP_IDENTIFIER_PRESENTED_ON_THE_TEST_NODE = '033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808'


def test_get_swap_info():
    """
    Case: get information about atomic swap by its identifier.
    Expect: information about the swap is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--id',
        SWAP_IDENTIFIER_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        NODE_27_IN_TESTNET_ADDRESS,
    ])

    swap_info = json.loads(result.output).get('result').get('information')
    swap_identifier = swap_info.get('swap_id')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert SWAP_IDENTIFIER_PRESENTED_ON_THE_TEST_NODE == swap_identifier
    assert re.match(pattern=ADDRESS_REGEXP, string=swap_info.get('sender_address')) is not None
    assert re.match(pattern=ADDRESS_REGEXP, string=swap_info.get('receiver_address')) is not None
    assert re.match(pattern=SWAP_IDENTIFIER_REGEXP, string=swap_identifier) is not None
    assert isinstance(swap_info.get('is_initiator'), bool)


def test_get_swap_info_without_node_url(mocker, swap_info):
    """
    Case: get information about atomic swap by its identifier without passing node URL.
    Expect: information about the swap is returned from node on localhost.
    """
    mock_swap_get_info = mocker.patch('cli.atomic_swap.service.loop.run_until_complete')
    mock_swap_get_info.return_value = swap_info

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--id',
        SWAP_IDENTIFIER_PRESENTED_ON_THE_TEST_NODE,
    ])

    expected_result = {
        'result': {
            'information': swap_info.data,
        },
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output)


def test_get_swap_info_invalid_swap_id():
    """
    Case: get information about atomic swap by its invalid identifier.
    Expect: the following swap identifier is invalid error message.
    """
    invalid_swap_id = '033402fe1346742486b15a3a9966eb524927'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--id',
        invalid_swap_id,
        '--node-url',
        NODE_27_IN_TESTNET_ADDRESS,
    ])

    expected_error = {
        'errors': {
            'id': [
                f'The following swap identifier `{invalid_swap_id}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_swap_info_non_existing_swap_id():
    """
    Case: get information about atomic swap by passing non-existing identifier.
    Expect: atomic swap with identifier not found error message.
    """
    non_existing_swap_id = '033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6809'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--id',
        non_existing_swap_id,
        '--node-url',
        NODE_27_IN_TESTNET_ADDRESS,
    ])

    expected_error = {
        'errors': f'Atomic swap with id "{non_existing_swap_id}" not found.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_swap_info_non_existing_node_url():
    """
    Case: get information about atomic swap by passing non-existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--id',
        SWAP_IDENTIFIER_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_swap_info_invalid_node_url():
    """
    Case: get information about atomic swap by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--id',
        SWAP_IDENTIFIER_PRESENTED_ON_THE_TEST_NODE,
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
def test_get_swap_info_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get information about atomic swap by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--id',
        SWAP_IDENTIFIER_PRESENTED_ON_THE_TEST_NODE,
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
