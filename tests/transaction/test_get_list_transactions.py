"""
Provide tests for command line interface's get list of transactions command.
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


def test_get_list_transaction_with_ids():
    """
    Case: get a list transactions by ids.
    Expect: transactions are returned.
    """
    transaction_ids = '044c7db163cf21ab9eafc9b267693e2d732411056c7530e54282946ec47cc180' \
                      '201e7be5612a671a7028474ad18e3738e676c17a86b7180fc1aad4c97e38b85b, ' \
                      '6601e240044b00db4b7e5eda7800e88236341077879a4a9cf5a1b1f9fb2ece87' \
                      '7bc9a43808d429e68f4d65ee8d7231e4e8711e705ad51be7888d1a7f25b57717'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--ids',
        transaction_ids,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


def test_get_list_transaction_with_invalid_ids():
    """
    Case: get a list transaction by invalid ids.
    Expect: the following ids are not valid error message.
    """
    invalid_transaction_ids = '044c7, True 010101'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--ids',
        invalid_transaction_ids,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    invalid_transaction_ids = [id_.strip() for id_ in invalid_transaction_ids.split(',')]

    expected_error_message = {
        'errors': {
            'ids': [
                f'The following id `{invalid_transaction_ids}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_transaction_with_start():
    """
    Case: get a list transaction by start.
    Expect: transactions are returned.
    """
    start = 'c13fff007b5059ea0f95fc0dc0bdc897ef185b1e1187e355f3b02fb0aad515eb' \
            '1d679241758805d82fc1b07975cb49ee36e7c9574315fc1df5bae8eb5b2766f4'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--start',
        start,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


def test_get_list_transaction_with_reverse():
    """
    Case: get a list transaction by reverse.
    Expect: reverse list transactions are returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
        '--reverse',
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


def test_get_list_transaction_by_head():
    """
    Case: get a list transaction by head.
    Expect: transactions are returned.
    """
    head = '152f3be91d8238538a83077ec8cd5d1d937767c0930eea61b59151b0dfa7c5a1' \
           '79a66f176ce23c14a67d8451cec2852c8ff60fe9e8963c3ed115bd6078898da0'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--head',
        head,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


@pytest.mark.parametrize('command_flag', ('--start', '--head'))
def test_get_list_transaction_with_invalid_start_head(command_flag):
    """
    Case: get a list transaction by invalid start and head.
    Expect: the following id is not valid error message.
    """
    invalid_id = '044c7db163cf21ab9eafc9b267693e2d732411056c7530e54282946ec47cc180'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        command_flag,
        invalid_id,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': {
            f'{command_flag[2:]}': [
                f'The following id `{invalid_id}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_transaction_with_limit():
    """
    Case: get a list transaction by limit.
    Expect: transaction is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--limit',
        1,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


def test_get_list_transaction_with_invalid_limit():
    """
    Case: get a list transaction by invalid limit.
    Expect: the following limit should be a positive error message.
    """
    invalid_limit = -33

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
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


def test_get_list_transaction_with_family_name():
    """
    Case: get a list transaction by family name.
    Expect: transactions are returned.
    """
    family_name = 'account'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--family-name',
        family_name,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


def test_get_list_transaction_with_invalid_family_name():
    """
    Case: get a list transaction by invalid family name.
    Expect: the following family name is not valid error message.
    """
    invalid_family_name = 'non-existing family name'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--family-name',
        invalid_family_name,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': {
            "family_name": [
                f"The following family name `{invalid_family_name}` is invalid.",
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_transaction_with_invalid_node_url():
    """
    Case: get a list of transactions by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'my-node-url.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--ids',
        '8d8cb28c58f7785621b51d220b6a1d39fe5829266495d28eaf0362dc85d7e91c'
        '205c1c4634604443dc566c56e1a4c0cf2eb122ac42cb482ef1436694634240c5',
        '--node-url',
        invalid_node_url,
    ])

    expected_error_message = {
        'errors': f'Please check if your node running at http://{invalid_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output
