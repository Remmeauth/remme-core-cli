"""
Provide tests for command line interface's get a list of states command.
"""
import json

import pytest
from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json

ADDRESS_WITH_STATE = '0000000000000000000000000000000000000000000000000000000000000000000001'


def test_get_list_state():
    """
    Case: get a list of states.
    Expect: states are returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_address = json.loads(result.output).get('result')[0].get('address')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_address == ADDRESS_WITH_STATE


def test_get_list_state_with_all_parameters():
    """
    Case: get a state by account address, starting address, limit, head, reverse.
    Expect: state is returned.
    """
    head = '56100bf24eed12d2f72fe3c3ccf75fe2f53d87c224d9dda6fb98a1411070b06a' \
           '40fcf97fccc61cb9c88442953af6ae50344ad7773f1becc6bae108443c18c551'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--address',
        ADDRESS_WITH_STATE,
        '--start',
        ADDRESS_WITH_STATE,
        '--limit',
        1,
        '--head',
        head,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
        '--reverse',
    ])

    expected_address = json.loads(result.output).get('result')[0].get('address')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_address == ADDRESS_WITH_STATE


def test_get_list_state_with_address():
    """
    Case: get a state by its address.
    Expect: state is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--address',
        ADDRESS_WITH_STATE,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_address = json.loads(result.output).get('result')[0].get('address')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_address == ADDRESS_WITH_STATE


@pytest.mark.parametrize('flag', ['--address', '--start'])
def test_get_list_state_with_invalid_address_start(flag):
    """
    Case: get a list of states by its invalid address and account address starting from.
    Expect: the following address is invalid error message.
    """
    invalid_address = '044c7db163cf2'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        flag,
        invalid_address,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': {
            'address': [
                f'The following address `{invalid_address}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


@pytest.mark.parametrize('flag', ['--address', '--start'])
def test_get_list_state_with_non_existing_address_start(flag):
    """
    Case: get a state by its non-existing address and account address starting from.
    Expect: block not found error message.
    """
    non_existing_address = '0000000000000000000000000000000000000000000000000000000000100000000031'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        flag,
        non_existing_address,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': f'Block not found.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_state_with_start():
    """
    Case: get a list states by account address starting from.
    Expect: list of states is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--start',
        ADDRESS_WITH_STATE,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    result_data = json.loads(result.output).get('result')[0]

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert result_data


def test_get_list_state_with_limit():
    """
    Case: get a state by limit.
    Expect: state is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--limit',
        1,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    result_data = json.loads(result.output).get('result')[0]

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert result_data


def test_get_list_state_with_invalid_limit():
    """
    Case: get a list of states by its invalid limit.
    Expect: the following limit is invalid error message.
    """
    invalid_limit = '-3'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--limit',
        invalid_limit,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': {
            'limit': [
                f'Limit must be greater than 0.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_state_with_non_existing_limit():
    """
    Case: get a state by its non-existing limit.
    Expect: invalid limit count error message.
    """
    non_existing_limit = 1e+10**2

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--limit',
        non_existing_limit,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': f'Invalid limit count.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_state_with_reverse():
    """
    Case: get a list of states by reverse.
    Expect: reverse list of a states are returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--reverse',
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    result_data = json.loads(result.output).get('result')[0]

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert result_data


def test_get_list_state_without_node_url(mocker):
    """
    Case: get a list of states by its address without passing node URL.
    Expect: states are returned from node on localhost.
    """
    expected_result = {
        "data": [
            {
                "address": "0000000000000000000000000000000000000000000000000000000000000000000001",
                "data": "CAE=",
            },
        ],
    }

    mock_get_states = mocker.patch('cli.state.service.loop.run_until_complete')
    mock_get_states.return_value = expected_result

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
    ])

    result_data = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result.get('data') == result_data


def test_get_list_state_non_existing_node_url():
    """
    Case: get a list of state by passing non-existing node URL.
    Expect: check if node running at URL error message.
    """
    invalid_node_url = 'my-node-url.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--node-url',
        invalid_node_url,
    ])

    expected_error_message = {
        'errors': f'Please check if your node running at http://{invalid_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_list_state_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get a list of states by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
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


def test_get_list_state_invalid_node_url():
    """
    Case: get a list of states by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
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
