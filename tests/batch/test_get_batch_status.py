"""
Provide tests for command line interface's get batch status command.
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


def test_get_batch_status():
    """
    Case: get a batch status by its identifier.
    Expect: batch status is returned.
    """
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-status',
        '--id',
        batch_id,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


def test_get_batch_status_with_invalid_id():
    """
    Case: get a batch status by invalid identifier.
    Expect: the following identifier is invalid error message.
    """
    invalid_batch_id = 'abcefg'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-status',
        '--id',
        invalid_batch_id,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': {
            'id': [
                f'The following identifier `{invalid_batch_id}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_batch_status_without_node_url(mocker):
    """
    Case: get a batch status by its identifier without passing node URL.
    Expect: batch status is returned from node on localhost.
    """
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751' \

    expected_result = {
        "result": "COMMITTED",
    }

    mock_get_batch_status_by_id = mocker.patch('cli.batch.service.loop.run_until_complete')
    mock_get_batch_status_by_id.return_value = expected_result

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-status',
        '--id',
        batch_id,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output).get('result')


def test_get_batch_status_with_invalid_node_url():
    """
    Case: get a batch status by its identifier by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-status',
        '--id',
        batch_id,
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
def test_get_batch_status_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get batch a status by its identifier by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-status',
        '--id',
        batch_id,
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


def test_get_batch_status_with_non_existing_node_url():
    """
    Case: get a batch status by its identifier by passing non-existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-status',
        '--id',
        batch_id,
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output