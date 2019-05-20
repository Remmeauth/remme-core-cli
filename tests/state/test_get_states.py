"""
Provide tests for command line interface's get a list of states command.
"""
import json
import re

import pytest
from click.testing import CliRunner

from cli.constants import (
    ADDRESS_REGEXP,
    DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    FAILED_EXIT_FROM_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json

ADDRESS_WITH_STATE = '0000000000000000000000000000000000000000000000000000000000000000000001'


def test_get_states():
    """
    Case: get a list of states.
    Expect: list of states is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    result_state_address = json.loads(result.output).get('result')
    first_state_address = result_state_address[0]

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert first_state_address.get('address') == ADDRESS_WITH_STATE


def test_get_states_with_all_parameters():
    """
    Case: get a list of states by account address, limit, head, reverse.
    Expect: list of states is returned.
    """
    head = 'c892656e3efd5459d782d97cba9cb046a73c7facc12e6849b804a7af7a600949' \
           '7d554ec1e3f9b191b1cdd512fb5d4b0c256cea3d3bd1475cf1f61a60f74cc4ed'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--address',
        ADDRESS_WITH_STATE,
        '--limit',
        1,
        '--head',
        head,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
        '--reverse',
    ])

    result_state_address = json.loads(result.output).get('result')
    single_state_address = result_state_address[0]

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert single_state_address.get('address') == ADDRESS_WITH_STATE


def test_get_states_with_address():
    """
    Case: get a list of states by its address.
    Expect: list of states is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--address',
        ADDRESS_WITH_STATE,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    result_state_address = json.loads(result.output).get('result')
    single_state_address = result_state_address[0]

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert single_state_address.get('address') == ADDRESS_WITH_STATE


def test_get_states_with_invalid_address():
    """
    Case: get a list of states by its invalid address.
    Expect: the following address is invalid error message.
    """
    invalid_address = '044c7db163cf2'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--address',
        invalid_address,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
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


def test_get_states_with_non_existing_address():
    """
    Case: get a list of states by its non-existing address.
    Expect: block not found error message.
    """
    non_existing_address = '0000000000000000000000000000000000000000000000000000000000100000000031'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--address',
        non_existing_address,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': 'Block not found.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_states_with_limit():
    """
    Case: get a list of states by limit.
    Expect: list of states is returned.
    """
    limit = 1

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--limit',
        limit,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    single_state_result = json.loads(result.output).get('result')
    single_state_address = single_state_result[0].get('address')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert re.match(pattern=ADDRESS_REGEXP, string=single_state_address) is not None
    assert len(single_state_result) == limit


def test_get_states_with_invalid_limit():
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
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': {
            'limit': [
                'Limit must be greater than 0.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_states_with_non_existing_limit():
    """
    Case: get a list of states by its non-existing limit.
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
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': 'Invalid limit count.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_states_with_invalid_head():
    """
    Case: get a list of states by its invalid head.
    Expect: the following block identifier is invalid error message.
    """
    invalid_head = '8d8cb28c58f7785621b51d220b6a1d39fe5829266495d28eaf0362dc85d7e91c'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--head',
        invalid_head,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': {
            'head': [
                f'The following block identifier `{invalid_head}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_states_with_non_existing_head():
    """
    Case: get a list of states by its non-existing head.
    Expect: block not found error message.
    """
    non_existing_head = '8d8cb28c58f7785621b51d220b6a1d39fe5829266495d28eaf0362dc85d7e91c' \
                        '205c1c4634604443dc566c56e1a4c0cf2eb122ac42cb482ef1436694634240ca'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--head',
        non_existing_head,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': 'Block not found.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_states_with_reverse():
    """
    Case: get a list of states by reverse.
    Expect: reverse list of states is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--reverse',
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    result_reverse_states = json.loads(result.output).get('result')
    first_reverse_state_address = result_reverse_states[0].get('address')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert re.match(pattern=ADDRESS_REGEXP, string=first_reverse_state_address) is not None


def test_get_states_without_node_url(mocker):
    """
    Case: get a list of states by its address without passing node URL.
    Expect: list of states is returned from a node on localhost.
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

    result_states = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result.get('data') == result_states


def test_get_states_non_existing_node_url():
    """
    Case: get a list of states by passing the non-existing node URL.
    Expect: check if node running at the URL error message.
    """
    non_existing_node_url = 'my-node-url.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get-list',
        '--node-url',
        non_existing_node_url,
    ])

    expected_error_message = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_states_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get a list of states by passing node URL with an explicit protocol.
    Expect: the following node URL contains a protocol error message.
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


def test_get_states_invalid_node_url():
    """
    Case: get a list of states by passing an invalid node URL.
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
