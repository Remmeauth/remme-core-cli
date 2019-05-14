"""
Provide tests for command line interface's get batch command.
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


def test_get_batch():
    """
    Case: get a batch by identifier.
    Expect: batch is returned.
    """
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get',
        '--id',
        batch_id,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


def test_get_batch_with_invalid_id():
    """
    Case: get a batch by its invalid identifier.
    Expect: the following identifier is invalid error message.
    """
    invalid_batch_id = 'abcefg'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get',
        '--id',
        invalid_batch_id,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
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


def test_get_batch_without_node_url(mocker):
    """
    Case: get a batch by its identifier without passing node URL.
    Expect: batch is returned from node on localhost.
    """
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751' \

    expected_result = {
        "data": {
            "header": {
                "signer_public_key": "03d425d2d17b64e3ef8fee028089a567fbb05bd556f98c0b6fb62bc5750ea62b8f",
                "transaction_ids": [
                    "5a84ff8747e16d15a988a8b13134d24981a6b516bb41042e6ea95c47f6c9429c"
                    "1c6fdf787ca2ea7fb8725b2bc2d0cd6aa3836aadfe85354deb714e048d41b4d7",
                ],
            },
            "header_signature": "57692f2bcc9be7fe2b59c052d5938eb92bd7be8a36487c1c7efc2c5758bf108e"
                                "232892987e898071e5ea13b4cbe283e96ac45d8f63cd9065522df7b85b050977",
            "transactions": [
                {
                    "header": {
                        "batcher_public_key": "03d425d2d17b64e3ef8fee028089a567fbb05bd556f98c0b6fb62bc5750ea62b8f",
                        "family_name": "sawtooth_settings",
                        "family_version": "1.0",
                        "inputs": [
                            "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b",
                            "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c12840f169a04216b7",
                        ],
                        "outputs": [
                            "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b",
                        ],
                        "signer_public_key": "03d425d2d17b64e3ef8fee028089a567fbb05bd556f98c0b6fb62bc5750ea62b8f",
                    },
                    "header_signature": "5a84ff8747e16d15a988a8b13134d24981a6b516bb41042e6ea95c47f6c9429c"
                                        "1c6fdf787ca2ea7fb8725b2bc2d0cd6aa3836aadfe85354deb714e048d41b4d7",
                    "payload": "CAESgAEKJnNhd3Rvb3RoLnNldHRpbmdzLnZvdGUuYyaXplZF9rZXlzEkIwM2Q0MjVkMmQxN2I2NGUzZWY4Zm"
                               "VlMDI4MDg5YTU2N2ZiYjA1YmQ1NTZmOThjMGI2ZmIJjNMGVhNjJiOGYaEjB4ZDU0NzJhOTY1NWJkYTNmNg==",
                },
            ],
        },
    }

    mock_get_batch_by_id = mocker.patch('cli.batch.service.loop.run_until_complete')
    mock_get_batch_by_id.return_value = expected_result

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get',
        '--id',
        batch_id,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result.get('data') == json.loads(result.output).get('result')


def test_get_batch_with_invalid_node_url():
    """
    Case: get a batch by its identifier by by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'my-node-url.com'
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get',
        '--id',
        batch_id,
        '--node-url',
        invalid_node_url,
    ])

    expected_error_message = {
        'errors': f'Please check if your node running at http://{invalid_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_batch_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get a batch by its identifier by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get',
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
