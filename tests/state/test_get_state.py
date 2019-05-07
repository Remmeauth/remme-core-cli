"""
Provide tests for command line interface's get state command.
"""
import json
import re

import pytest
from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    HEADER_SIGNATURE_REGEXP,
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json

ADDRESS_WITH_STATE = '0000000000000000000000000000000000000000000000000000000000000000000001'


def test_get_state_with_address():
    """
    Case: get a state by its address.
    Expect: state is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get',
        '--address',
        ADDRESS_WITH_STATE,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    result_header_signature = json.loads(result.output).get('result').get('state').get('head')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert re.match(pattern=HEADER_SIGNATURE_REGEXP, string=result_header_signature) is not None
    assert isinstance(json.loads(result.output), dict)


def test_get_state_with_invalid_address():
    """
    Case: get a state by its invalid address.
    Expect: the following address is invalid error message.
    """
    invalid_address = '044c7db163cf2'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get',
        '--address',
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


def test_get_state_with_non_existing_address():
    """
    Case: get a state by its non-existing address.
    Expect: block for address not found error message.
    """
    non_existing_address = '0000000000000000000000000000000000000000000000000000000000100000000031'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get',
        '--address',
        non_existing_address,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': f'Block for address `{non_existing_address}` not found.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_state_without_node_url(mocker):
    """
    Case: get a state by its address without passing node URL.
    Expect: state is returned from node on localhost.
    """
    expected_result = {
        "data": "CAE=",
        "head": "2f7c6645c8e95c42ee229e14c64a80e382e3b3ef4edf73fadbc8f3605f4588ad"
                "2e9272264d138278057de2f7961dcc962b4b89713cf69d256299a6635532017b",
    }

    mock_get_state_by_address = mocker.patch('cli.state.service.loop.run_until_complete')
    mock_get_state_by_address.return_value = expected_result

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get',
        '--address',
        ADDRESS_WITH_STATE,
    ])

    result_output = json.loads(result.output).get('result').get('state')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == result_output


def test_get_state_with_invalid_node_url():
    """
    Case: get a state by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'my-node-url.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get',
        '--address',
        ADDRESS_WITH_STATE,
        '--node-url',
        invalid_node_url,
    ])

    expected_error_message = {
        'errors': f'Please check if your node running at http://{invalid_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_state_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get a state by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'state',
        'get',
        '--address',
        ADDRESS_WITH_STATE,
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
