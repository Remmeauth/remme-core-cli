"""
Provide tests for command line interface's get block by its identifier command.
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

EXISTING_BLOCK_IDENTIFIER = '4a7897650db9863aca34874778e6c5802f86c3df0e22b39cfea730bc83654357' \
                            '037a422f8ef51ac85a9bc61d2484bd0f37be10cfc861588c41dc6f1bbfd92cde'


def test_get_block():
    """
    Case: get a block by identifier.
    Expect: block data is returned, batches are presented, header signature is block identifier.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get',
        '--id',
        EXISTING_BLOCK_IDENTIFIER,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    result_block = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert EXISTING_BLOCK_IDENTIFIER == result_block.get('header_signature')
    assert len(result_block.get('batches')) > 0


def test_get_block_invalid_identifier():
    """
    Case: get a block by invalid identifier.
    Expect: the following block is an invalid error message.
    """
    invalid_block_identifier = '152f3be91d8238538a83077ec8cd5d1d937767c0930eea61b59151b0dfa7c5a1'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get',
        '--id',
        invalid_block_identifier,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': {
            'id': [
                f'The following block identifier `{invalid_block_identifier}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_block_without_node_url(mocker):
    """
    Case: get a block by identifier without passing node URL.
    Expect: blocks is returned from a node on localhost.
    """
    block = {
        'data': {
            'batches': [
                {
                    'header': {
                        'signer_public_key': '02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135',
                        'transaction_ids': [
                            'ce8dd0946326072eb4c70818d7d0df32ebd80b3a24525306ff92e8caa8c886ee'
                            '571d8ba9f01c73c2c4aaab7960c0ef88865ace6dd9274dd378649f5b9da7c820',
                        ],
                    },
                    'header_signature': 'b684d527666cce92ea57d8e14d467ee3cec5515759e1d0a78df65dbcd2a5ff99'
                                        '3f95c8efac7c35a6380cbce81941119e98b72956278e663b9fa04e396bb7849f',
                    'trace': 'false',
                    'transactions': [
                        {
                            'header': {
                                'batcher_public_key': '02d1fbda50dbcd0d3c286a6a9fa71aa7c'
                                                      'e2d97159b90ddd463e0816422d621e135',
                                'dependencies': [],
                                'family_name': 'block_info',
                                'family_version': '1.0',
                                'inputs': [
                                    '00b10c0100000000000000000000000000000000000000000000000000000000000000',
                                    '00b10c00',
                                ],
                                'nonce': '',
                                'outputs': [
                                    '00b10c0100000000000000000000000000000000000000000000000000000000000000',
                                    '00b10c00',
                                ],
                                'payload_sha512': 'ef5953af5e24047f92cea476c6706da72b6207ac89077cb314d6d518a1293433'
                                                  '955c0a5012c52c4acb34e2220ac8fcc33f83b33ab847631f0471f10dcdf0a54f',
                                'signer_public_key': '02d1fbda50dbcd0d3c286a6a9fa71aa7c'
                                                     'e2d97159b90ddd463e0816422d621e135',
                            },
                            'header_signature': 'ce8dd0946326072eb4c70818d7d0df32ebd80b3a24525306ff92e8caa8c886ee'
                                                '571d8ba9f01c73c2c4aaab7960c0ef88865ace6dd9274dd378649f5b9da7c820',
                            'payload': 'CtICCAESgAExNTJmM2JlOTFkODIzODUzOGE4MzA3N2VjOGNkNWQxZDkzNzc2N2MwOTMwZWVhNjFiN'
                                       'TkxNTFiMGRmYTdjNWExNzlhNjZmMTc2Y2UyM2MxNGE2N2Q4NDUxY2VjMjg1MmM4ZmY2MGZlOWU4OT'
                                       'YzYzNlZDExNWJkNjA3ODg5OGRhMBpCMDJkMWZiZGE1MGRiY2QwZDNjMjg2YTZhOWZhNzFhYTdjZTJ'
                                       'kOTcxNTliOTBkZGQ0NjNlMDgxNjQyMmQ2MjFlMTM1IoABNGFlNmYzOWY0ZDZlNWJiNDhmYzA0Y2Y0'
                                       'MGJhNzEwMTNmYzA0NGZlNTdjOWE3Njg3ZjRlMTNkZjhjZDQ4ODQ1OTA4YTAxNjAzOTRlN2RjNjRjN'
                                       'Dc5YTg0YzVkYmYwZmUzYzVlZTZkNmIxMDhlNzZjODYyNzQ4NzkxMWZjNjgxYWUokIr35QU=',
                        },
                    ],
                },
            ],
            'header': {
                'batch_ids': [
                    'b684d527666cce92ea57d8e14d467ee3cec5515759e1d0a78df65dbcd2a5ff99'
                    '3f95c8efac7c35a6380cbce81941119e98b72956278e663b9fa04e396bb7849f',
                    'cd11713211c6eb2fe4adc0e44925c1f82e9300e0b8827bd3c73d8be10e61cd2b'
                    '1e8da810078845ca1665b4adf7f691ad731ab4cea0fc994c55a8863b30220c6e',
                ],
                'block_num': '2',
                'consensus': 'RGV2bW9kZVrz+4RUt+Xyzhofvok/lkMcK3ZtAh/zcO/6gbPJPLPw',
                'previous_block_id': '4ae6f39f4d6e5bb48fc04cf40ba71013fc044fe57c9a7687f4e13df8cd488459'
                                     '08a0160394e7dc64c479a84c5dbf0fe3c5ee6d6b108e76c8627487911fc681ae',
                'signer_public_key': '02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135',
                'state_root_hash': '54eeacdf8fe3262862782110d4396b60f4b8c3863ff1b1b208fa996b6bb24a0f',
            },
            'header_signature': '4a7897650db9863aca34874778e6c5802f86c3df0e22b39cfea730bc83654357'
                                '037a422f8ef51ac85a9bc61d2484bd0f37be10cfc861588c41dc6f1bbfd92cde',
        },
    }

    mock_get_block_by_id = mocker.patch('cli.block.service.loop.run_until_complete')
    mock_get_block_by_id.return_value = block

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get',
        '--id',
        EXISTING_BLOCK_IDENTIFIER,
    ])

    expected_result = {
        'result': block.get('data'),
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output)
    assert EXISTING_BLOCK_IDENTIFIER == block.get('data').get('header_signature')


def test_get_block_invalid_node_url():
    """
    Case: get a block by identifier by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get',
        '--id',
        EXISTING_BLOCK_IDENTIFIER,
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
def test_get_block_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get a block by identifier by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get',
        '--id',
        EXISTING_BLOCK_IDENTIFIER,
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


def test_get_block_non_existing_node_url():
    """
    Case: get a block by identifier by passing non-existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get',
        '--id',
        EXISTING_BLOCK_IDENTIFIER,
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_block_non_existing_identifier():
    """
    Case: get a block by identifier by passing non-existing identifier.
    Expect: block with identifier not found error message.
    """
    non_existing_block_identifier = '7a7897650db9863aca34874778e6c5802f86c3df0e22b39cfea730bc83654357' \
                                    '037a422f8ef51ac85a9bc61d2484bd0f37be10cfc861588c41dc6f1bbfd92cde'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get',
        '--id',
        non_existing_block_identifier,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': f'Block with id `{non_existing_block_identifier}` not found.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
