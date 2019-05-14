"""
Provide tests for command line interface's get receipts command.
"""
import json

import pytest
from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json

TRANSACTION_IDENTIFIERS_PRESENTED_ON_THE_TEST_NODE = \
    '7c5d2651b8a1bb04b99b9a1ce201aaf9e0cb35357b9ab31611b7f7957e931a71' \
    '4e059ecfa9fac73f49c6631c1a5e549218f1700366d82e5d84e0e7eb403e73ea, ' \
    '640fe45794d2f63fbe1850aa99d0ac830ed94e1ac9b475e1e8c841f714b6250e' \
    '64bc6fbd9f821147ee1eab4d76e5437f5b878a9b5288f1d4c1dc192060a82cf1'


def test_get_receipts_with_identifiers():
    """
    Case: get a list of the transaction's receipts by identifiers.
    Expect: a list of the transaction's receipts is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'receipt',
        'get',
        '--ids',
        TRANSACTION_IDENTIFIERS_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    list_of_receipts = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    for receipt in list_of_receipts:
        assert receipt.get('id') in TRANSACTION_IDENTIFIERS_PRESENTED_ON_THE_TEST_NODE


def test_get_receipts_with_identifier():
    """
    Case: get a list of the transaction's receipts by identifier.
    Expect: a list of the transaction's receipts is returned.
    """
    transaction_identifier = '7c5d2651b8a1bb04b99b9a1ce201aaf9e0cb35357b9ab31611b7f7957e931a71' \
                             '4e059ecfa9fac73f49c6631c1a5e549218f1700366d82e5d84e0e7eb403e73ea'
    runner = CliRunner()
    result = runner.invoke(cli, [
        'receipt',
        'get',
        '--ids',
        transaction_identifier,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    list_of_receipts = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert transaction_identifier == list_of_receipts[0].get('id')


def test_get_receipts_without_node_url(mocker):
    """
    Case: get a list of the transaction's receipts without passing node URL.
    Expect: a list of the transaction's receipts is returned from a node on localhost.
    """
    expected_list_of_receipts = [
        {
            'data': [],
            'events': [],
            'id': 'e79a883581c184787360de8607c5f970cdeeaa684af3e50d8532aa9dd07afa8e'
                  '7fc92f0dc509b41b9695e795704bdd50455bebd1ed327a5330710ba40698b492',
            'state_changes': [
                {
                    'address': '00b10c0100000000000000000000000000000000000000000000000000000000000000',
                    'type': 'SET',
                    'value': 'CL0BGIACIKwC',
                },
                {
                    'address': '00b10c00000000000000000000000000000000000000000000000000000000000000bd',
                    'type': 'SET',
                    'value': 'CL0BEoABZmQ3ODBjZTA3NjQwYmE0MTEyMjQ4NjkxNTgxYTU5NTg0NWZlNzYyYmYzZmViNDliODQzOTc0Y'
                             'WFlNTc4NDc4YzZiZjUxODczOWVjZGM0OWQ3MDE5MzgzZDNiZDllM2FhNmZhMGFmODM4NGI0NDkxOGYwYm'
                             'ZmMzc0MDJiNTEwYjIaQjAyZDFmYmRhNTBkYmNkMGQzYzI4NmE2YTlmYTcxYWE3Y2UyZDk3MTU5YjkwZGR'
                             'kNDYzZTA4MTY0MjJkNjIxZTEzNSKAAWZlNTZhMTZkYWIwMDljYzk2ZTcxMjVjNjQ3YjZjNzFlYjEwNjM4'
                             'MThjZjhkZWNlMjgzYjEyNTQyM2VjYjE4NGY3ZjFlNjE4MDJiZjY2MzgyZGE5MDQ2OTg0MTNmODA4MzEwM'
                             'zFmOGExYjI5MTUwMjYwYzNmYTRkYjUzN2ZkZjRjKIzggeYF',
                },
            ],
        },
        {
            'data': [],
            'events': [],
            'id': '6593d21046519022ba32c98e934d7dfc81e8b4edf6c064dbf70feb13db431087'
                  '3ec00816bce8660cafd4fa2a8c80d0147d63cf616c624babd03142c694272017',
            'state_changes': [
                {
                    'address': '00b10c00000000000000000000000000000000000000000000000000000000000000bc',
                    'type': 'SET',
                    'value': 'CLwBEoABOWI4Y2NhODk3Nzk2NDJiYWEyMGMwZWUyZjEzOWVlMGNlMWNjYjEwMjY5OTVjNDY3NDYzZDEzOT'
                             'I0ZDg3YTg3NjNlODMzOWI2YzIyMzNmMTZiY2I5ZDVjNjEwMzVmNzAzY2FiNjBiNzQxMGJlMjJkZjkzNWEy'
                             'YWE4YmIzNGE1NTcaQjAyZDFmYmRhNTBkYmNkMGQzYzI4NmE2YTlmYTcxYWE3Y2UyZDk3MTU5YjkwZGRkND'
                             'YzZTA4MTY0MjJkNjIxZTEzNSKAAWZkNzgwY2UwNzY0MGJhNDExMjI0ODY5MTU4MWE1OTU4NDVmZTc2MmJm'
                             'M2ZlYjQ5Yjg0Mzk3NGFhZTU3ODQ3OGM2YmY1MTg3MzllY2RjNDlkNzAxOTM4M2QzYmQ5ZTNhYTZmYTBhZj'
                             'gzODRiNDQ5MThmMGJmZjM3NDAyYjUxMGIyKMzfgeYF',
                },
                {
                    'address': '00b10c0100000000000000000000000000000000000000000000000000000000000000',
                    'type': 'SET',
                    'value': 'CLwBGIACIKwC',
                },
            ],
        },
    ]

    mock_get_receipts = mocker.patch('cli.receipt.service.loop.run_until_complete')
    mock_get_receipts.return_value = expected_list_of_receipts

    runner = CliRunner()
    result = runner.invoke(cli, [
        'receipt',
        'get',
        '--ids',
        TRANSACTION_IDENTIFIERS_PRESENTED_ON_THE_TEST_NODE,
    ])

    expected_node_information = {
        'result': expected_list_of_receipts,
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_node_information == json.loads(result.output)


def test_get_receipts_invalid_identifiers():
    """
    Case: get a list of the transaction's receipts by passing invalid identifiers.
    Expect: the following identifier is not a valid error message.
    """
    invalid_identifier = 'e79a883581c184787360de8607c5f970cdeeaa684af3e50d8532aa9dd07afa8e'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'receipt',
        'get',
        '--ids',
        invalid_identifier,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': {
            'ids': [
                f'The following identifier `{invalid_identifier}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_receipts_invalid_node_url():
    """
    Case: get a list of the transaction's receipts by passing an invalid node URL.
    Expect: the following node URL is an invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'receipt',
        'get',
        '--ids',
        TRANSACTION_IDENTIFIERS_PRESENTED_ON_THE_TEST_NODE,
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


def test_get_receipts_non_existing_identifiers():
    """
    Case: get a list of the transaction's receipts by passing non-existing identifiers.
    Expect: transactions with identifiers not found the error message.
    """
    non_existing_identifiers = \
        'e79a883581c184787360de8607c5f970cdeeaa684af3e50d8532aa9dd07afa8e' \
        '7fc92f0dc509b41b9695e795704bdd50455bebd1ed327a5330710ba40698b4cc, ' \
        '6593d21046519022ba32c98e934d7dfc81e8b4edf6c064dbf70feb13db431087' \
        '3ec00816bce8660cafd4fa2a8c80d0147d63cf616c624babd03142c6942720cc'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'receipt',
        'get',
        '--ids',
        non_existing_identifiers,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    list_of_identifiers = []

    for identifier in non_existing_identifiers.split(','):
        identifier = identifier.strip()
        list_of_identifiers.append(identifier)

    expected_error = {
        'errors': f'Transactions with ids "{list_of_identifiers}" not found.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_receipts_non_existing_node_url():
    """
    Case: get a list of the transaction's receipts by passing the non-existing node URL.
    Expect: check if node running at the URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'receipt',
        'get',
        '--ids',
        TRANSACTION_IDENTIFIERS_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_receipts_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get a list of the transaction's receipts by passing node URL with an explicit protocol.
    Expect: the following node URL contains the protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'receipt',
        'get',
        '--ids',
        TRANSACTION_IDENTIFIERS_PRESENTED_ON_THE_TEST_NODE,
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
