"""
Provide tests for command line interface's get list of batches command.
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


def test_get_list_batches_with_all_parameters(mocker):
    """
    Case: get a list of batches by identifiers, identifier starting from, limit, head, reverse.
    Expect: batches are returned from node on localhost.
    """
    batch_id = '169c3691a4a78b476a1891bf2a7afac27bb218d182889443bfbbc4090bb933b1' \
               '0a8a9ea3866b5f478020831d7efa41c834903f2f9adc324d965b207714f72ed9'

    head = '2eeebae97b8a813ca64a76717a44de9fdd787342ed122e9e9399570be35ba354' \
           '279639ad2a5848b136891bcdac343e2628938e63dbf9dc0f3d2a0e63cc6cb51f'

    expected_result = {
        "data": [
            {
                "header": {
                    "signer_public_key": "03d425d2d17b64e3ef8fee028089a567fbb05bd556f98c0b6fb62bc5750ea62b8f",
                    "transaction_ids": [
                        "ea15ec70968c6cf23d44a15431e4f2eea190db377eee0ebcaa605adabbc7d205"
                        "768a8088ea7b1c45cab73835b76e1f187be52fc06ca37deb975c693bfe7a0874",
                    ],
                },
                "header_signature": "169c3691a4a78b476a1891bf2a7afac27bb218d182889443bfbbc4090bb933b1"
                                    "0a8a9ea3866b5f478020831d7efa41c834903f2f9adc324d965b207714f72ed9",
                "transactions": [
                    {
                        "header": {
                            "batcher_public_key": "03d425d2d17b64e3ef8fee028089a567fbb05bd556f98c0b6fb62bc5750ea62b8f",
                            "dependencies": [],
                            "family_name": "sawtooth_settings",
                            "family_version": "1.0",
                            "inputs": [
                                "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b",
                                "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c12840f169a04216b7",
                                "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1918142591ba4e8a7",
                                "000000a87cb5eafdcca6a8f82af32160bc5311783bdad381ea57b4e3b0c44298fc1c14",
                            ],
                            "nonce": "",
                            "outputs": [
                                "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b",
                                "000000a87cb5eafdcca6a8f82af32160bc5311783bdad381ea57b4e3b0c44298fc1c14",
                            ],
                        },
                        "header_signature": "ea15ec70968c6cf23d44a15431e4f2eea190db377eee0ebcaa605adabbc7d205"
                                            "768a8088ea7b1c45cab73835b76e1f187be52fc06ca37deb975c693bfe7a0874",
                        "payload": "CAESRAoic2F3dG9vdGgudmFsaWRhdG9yLmJhdGNoX2luamVj"
                                   "dG9ycxIKYmxvY2tfaW5mbxoSMHgyNzVkYWUwZDZkODg4NjE5",
                    },
                ],
            },
        ],
        "head": "2eeebae97b8a813ca64a76717a44de9fdd787342ed122e9e9399570be35ba354"
                "279639ad2a5848b136891bcdac343e2628938e63dbf9dc0f3d2a0e63cc6cb51f",
    }

    mock_get_batch_by_ids = mocker.patch('cli.batch.service.loop.run_until_complete')
    mock_get_batch_by_ids.return_value = expected_result

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--ids',
        batch_id,
        '--start',
        batch_id,
        '--limit',
        1,
        '--head',
        head,
        '--reverse',
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output).get('result')


def test_get_list_batches_with_ids():
    """
    Case: get a list of batches by identifiers.
    Expect: batches are returned.
    """
    batch_ids = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
                '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751, ' \
                '257353cb1180bdce4e19f290e4bfdb48212744a8ae08f6fc974e8c7c2cfe4692' \
                '19d257a7c62197bd614b9dc13cd562c6612aee45ab0bccfcdd6b0d1ed0b3cdcf'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--ids',
        batch_ids,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_header_signature = '257353cb1180bdce4e19f290e4bfdb48212744a8ae08f6fc974e8c7c2cfe4692' \
                                '19d257a7c62197bd614b9dc13cd562c6612aee45ab0bccfcdd6b0d1ed0b3cdcf'

    result_header_signature = json.loads(result.output).get('result').get('data')[0].get('header_signature')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)
    assert expected_header_signature == result_header_signature


def test_get_list_batches_with_invalid_ids():
    """
    Case: get a list of batches by invalid identifiers.
    Expect: the following identifier is not valid error message.
    """
    invalid_id = '6f200'
    batch_ids = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
                '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751, ' \
                f'{invalid_id}'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--ids',
        batch_ids,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': {
            'ids': [
                f'The following identifier `{invalid_id}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_batches_with_start():
    """
    Case: get a list of batches by batch identifier starting from.
    Expect: batches are returned.
    """
    start = 'fa2d1a209ad04fd2ad7fb5183976e647cc47b4c08e2e578097afc2566a0284e7' \
            '60eb3f2ff8f72f290765211d4da3341f23091cc7a16805025a17c04a90818a44'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--start',
        start,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


def test_get_list_batches_with_reverse():
    """
    Case: get a list of batches by reverse.
    Expect: reversed list of batches is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
        '--reverse',
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


def test_get_list_batches_by_head():
    """
    Case: get a list of batches by block identifier.
    Expect: batches are returned.
    """
    head = '56100bf24eed12d2f72fe3c3ccf75fe2f53d87c224d9dda6fb98a1411070b06a' \
           '40fcf97fccc61cb9c88442953af6ae50344ad7773f1becc6bae108443c18c551'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--head',
        head,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


@pytest.mark.parametrize('command_flag', ('--start', '--head'))
def test_get_list_batches_with_invalid_start_head(command_flag):
    """
    Case: get a list of batches by invalid block identifier and batch identifier starting from.
    Expect: the following identifier is invalid error message.
    """
    invalid_id = '044c7db163cf21ab9eafc9b267693e2d732411056c7530e54282946ec47cc180'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        command_flag,
        invalid_id,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': {
            f'{command_flag[2:]}': [
                f'The following identifier `{invalid_id}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_batches_with_limit():
    """
    Case: get a list of batches by limit.
    Expect: batch is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--limit',
        1,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)


def test_get_list_batches_with_invalid_limit():
    """
    Case: get a list of batches by invalid limit.
    Expect: limit must be greater than 0 error message.
    """
    invalid_limit = -33

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--limit',
        invalid_limit,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
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


def test_get_list_batches_with_invalid_node_url():
    """
    Case: get a list of batches by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'my-node-url.com'
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--ids',
        batch_id,
        '--node-url',
        invalid_node_url,
    ])

    expected_error_message = {
        'errors': f'Please check if your node running at http://{invalid_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_batches_without_node_url(mocker):
    """
    Case: get a list of batches by identifier without passing node URL.
    Expect: batches are returned from node on localhost.
    """
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8752'

    expected_result = {
        "data": [
            {
                "header": {
                    "signer_public_key": "03d425d2d17b64e3ef8fee028089a567fbb05bd556f98c0b6fb62bc5750ea62b8f",
                    "transaction_ids": [
                        "ea15ec70968c6cf23d44a15431e4f2eea190db377eee0ebcaa605adabbc7d205"
                        "768a8088ea7b1c45cab73835b76e1f187be52fc06ca37deb975c693bfe7a0874",
                    ],
                },
                "header_signature": "169c3691a4a78b476a1891bf2a7afac27bb218d182889443bfbbc4090bb933b1"
                                    "0a8a9ea3866b5f478020831d7efa41c834903f2f9adc324d965b207714f72ed9",
                "transactions": [
                    {
                        "header": {
                            "batcher_public_key": "03d425d2d17b64e3ef8fee028089a567fbb05bd556f98c0b6fb62bc5750ea62b8f",
                            "dependencies": [],
                            "family_name": "sawtooth_settings",
                            "family_version": "1.0",
                            "inputs": [
                                "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b",
                                "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c12840f169a04216b7",
                                "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1918142591ba4e8a7",
                                "000000a87cb5eafdcca6a8f82af32160bc5311783bdad381ea57b4e3b0c44298fc1c14",
                            ],
                            "nonce": "",
                            "outputs": [
                                "000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b",
                                "000000a87cb5eafdcca6a8f82af32160bc5311783bdad381ea57b4e3b0c44298fc1c14",
                            ],
                        },
                        "header_signature": "ea15ec70968c6cf23d44a15431e4f2eea190db377eee0ebcaa605adabbc7d205"
                                            "768a8088ea7b1c45cab73835b76e1f187be52fc06ca37deb975c693bfe7a0874",
                        "payload": "CAESRAoic2F3dG9vdGgudmFsaWRhdG9yLmJhdGNoX2luamVj"
                                   "dG9ycxIKYmxvY2tfaW5mbxoSMHgyNzVkYWUwZDZkODg4NjE5",
                    },
                ],
            },
        ],
        "head": "2eeebae97b8a813ca64a76717a44de9fdd787342ed122e9e9399570be35ba354"
                "279639ad2a5848b136891bcdac343e2628938e63dbf9dc0f3d2a0e63cc6cb51f",
    }

    mock_get_batch_by_ids = mocker.patch('cli.batch.service.loop.run_until_complete')
    mock_get_batch_by_ids.return_value = expected_result

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--ids',
        batch_id,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output).get('result')


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_list_batches_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get a list of batches by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    batch_id = '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e' \
               '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'batch',
        'get-list',
        '--ids',
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
