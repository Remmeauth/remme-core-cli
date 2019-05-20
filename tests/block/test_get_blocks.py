"""
Provide tests for command line interface's get a list of blocks command.
"""
import json
import re

import pytest
from click.testing import CliRunner

from cli.constants import (
    BLOCK_IDENTIFIER_REGEXP,
    DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    FAILED_EXIT_FROM_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json

EXISTING_BLOCKS_IDENTIFIERS = 'b757c74fbcd57ae12577b71490878affb6b688434c2e20170138760e72e937ca' \
                              '1bb3d6773e2ef37b5151ed74dcb663114a181072e0870e7a4d452c58659a6dbb, ' \
                              '585f23725d1236e90e2b961b0c0c1404aba0ba5a96e4d85cd2f048b1d61b0276' \
                              '69153e3618c84fc09a8041f8e149b97d50a89ee7761d0458cd57c63d5f354cbd'


def test_get_blocks_all_parameters():
    """
    Case: get a list of blocks by identifier, limit, head, reverse.
    Expect: blocks are returned.
    """
    limit = 2

    head_identifier = '585f23725d1236e90e2b961b0c0c1404aba0ba5a96e4d85cd2f048b1d61b0276' \
                      '69153e3618c84fc09a8041f8e149b97d50a89ee7761d0458cd57c63d5f354cbd'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--ids',
        EXISTING_BLOCKS_IDENTIFIERS,
        '--head',
        head_identifier,
        '--limit',
        limit,
        '--reverse',
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    list_of_blocks = json.loads(result.output).get('result')
    first_block_identifier = list_of_blocks[0].get('header_signature')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert first_block_identifier == head_identifier

    for block in list_of_blocks:
        block_identifier = block.get('header_signature')
        block_batches = block.get('batches')

        assert re.match(pattern=BLOCK_IDENTIFIER_REGEXP, string=block_identifier) is not None
        assert len(block_batches) > 0


def test_get_blocks():
    """
    Case: get a list of blocks.
    Expect: blocks are returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    list_of_blocks = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    for block in list_of_blocks:
        block_identifier = block.get('header_signature')
        block_batches = block.get('batches')

        assert re.match(pattern=BLOCK_IDENTIFIER_REGEXP, string=block_identifier) is not None
        assert len(block_batches) > 0


def test_get_blocks_with_ids():
    """
    Case: get a list of blocks by its identifiers.
    Expect: blocks with header signatures which matches specified identifiers are returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--ids',
        EXISTING_BLOCKS_IDENTIFIERS,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    list_of_blocks = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    for block in list_of_blocks:
        block_identifier = block.get('header_signature')

        assert re.match(pattern=BLOCK_IDENTIFIER_REGEXP, string=block_identifier) is not None
        assert block_identifier in EXISTING_BLOCKS_IDENTIFIERS


def test_get_blocks_invalid_ids():
    """
    Case: get a list of blocks by its invalid identifiers.
    Expect: the following identifiers are not a valid error message.
    """
    invalid_block_identifier = 'fe56a16dab009cc96e7125c647b6c71eb1063818cf8dece283b125423ecb184f'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--ids',
        invalid_block_identifier,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'errors': {
            'ids': [
                f'The following block identifier `{invalid_block_identifier}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_blocks_with_non_existing_ids():
    """
    Case: get a list of blocks by non-existing identifiers.
    Expect: resource not found error message.
    """
    non_existing_blocks_ids = 'fe56a16dab009cc96e7125c647b6c71eb1063818cf8dece283b125423ecb184f' \
                              '7f1e61802bf66382da904698413f80831031f8a1b29150260c3fa4db537fdfcc, ' \
                              '56100bf24eed12d2f72fe3c3ccf75fe2f53d87c224d9dda6fb98a1411070b06a' \
                              '40fcf97fccc61cb9c88442953af6ae50344ad7773f1becc6bae108443c18c5c1'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--ids',
        non_existing_blocks_ids,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': 'List of blocks not found.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_blocks_with_head():
    """
    Case: get a list of blocks filtering by head identifier.
    Expect: the first block's header signature matches specified head identifiers.
    """
    head_identifier = 'abd66e73a9354d0eacb419c23689c6e912f444985f1f699531080148702c5d46' \
                      '7ff778dff1ae3deab94684add561020fa69403e82c45b0f38f03897984581ed8'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--head',
        head_identifier,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    list_of_blocks = json.loads(result.output).get('result')
    first_block_identifier = list_of_blocks[0].get('header_signature')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert first_block_identifier == head_identifier

    for block in list_of_blocks:
        block_identifier = block.get('header_signature')

        assert re.match(pattern=BLOCK_IDENTIFIER_REGEXP, string=block_identifier) is not None


def test_get_blocks_invalid_head():
    """
    Case: get a list of blocks by invalid head identifier.
    Expect: the following identifiers are not a valid error message.
    """
    invalid_head = 'fe56a16dab009cc96e7125c647b6c71eb1063818cf8dece283b125423ecb184f'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
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


def test_get_blocks_with_limit():
    """
    Case: get a list of blocks limiting by a number.
    Expect: a specified number of blocks are returned.
    """
    limit = 2

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--limit',
        2,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    list_of_blocks = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert len(list_of_blocks) == limit

    for block in list_of_blocks:
        block_identifier = block.get('header_signature')

        assert re.match(pattern=BLOCK_IDENTIFIER_REGEXP, string=block_identifier) is not None


def test_get_blocks_with_negative_limit():
    """
    Case: get a list of blocks limiting by a negative number.
    Expect: the following limit should be a positive error message.
    """
    invalid_limit = -33

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
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


def test_get_blocks_with_invalid_limit():
    """
    Case: get a list of blocks limiting by an invalid number.
    Expect: invalid limit count error message.
    """
    invalid_limit = 123456789009876543234567890

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--limit',
        invalid_limit,
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': 'Invalid limit count.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_blocks_identifiers():
    """
    Case: get a list of blocks' identifiers.
    Expect: a list of blocks' identifiers is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--ids-only',
        '--node-url',
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    blocks = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    for block_identifier in blocks:
        assert re.match(pattern=BLOCK_IDENTIFIER_REGEXP, string=block_identifier) is not None


def test_get_blocks_invalid_node_url():
    """
    Case: get a list of blocks by passing an invalid node URL.
    Expect: the following node URL is an invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
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


def test_get_blocks_non_existing_node_url():
    """
    Case: get a list of blocks by passing an invalid node URL.
    Expect: check if node running at the URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_blocks_without_node_url(mocker):
    """
    Case: get a list of blocks without passing node URL.
    Expect: blocks are returned from a node on localhost.
    """
    blocks_ids = 'fe56a16dab009cc96e7125c647b6c71eb1063818cf8dece283b125423ecb184f' \
                 '7f1e61802bf66382da904698413f80831031f8a1b29150260c3fa4db537fdf4c, ' \
                 '56100bf24eed12d2f72fe3c3ccf75fe2f53d87c224d9dda6fb98a1411070b06a' \
                 '40fcf97fccc61cb9c88442953af6ae50344ad7773f1becc6bae108443c18c551'

    blocks = {
        'data': [
            {
                'batches': [
                    {
                        'header': {
                            'signer_public_key': '2d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135',
                            'transaction_ids': [
                                'e79a883581c184787360de8607c5f970cdeeaa684af3e50d8532aa9dd07afa8e'
                                '7fc92f0dc509b41b9695e795704bdd50455bebd1ed327a5330710ba40698b492',
                            ],
                        },
                        'header_signature': '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e'
                                            '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751',
                        'trace': 'false',
                        'transactions': [
                            {
                                'header': {
                                    'batcher_public_key': '02d1fbda50dbcd0d3c286a6a9fa71aa7c'
                                                          'e2d97159b90ddd463e0816422d621e135',
                                    'dependencies': [],
                                    'family_name': 'account',
                                    'family_version': '0.1',
                                    'inputs': [
                                        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
                                        '112007a90f66c661b32625f17e27177034a6d2cb552f89cba8c78868705ae276897df6',
                                    ],
                                    'nonce': '420c05684e84586a1cb796ee43a3821f88f26f3cf54dcd139b82f12f9a9d138e'
                                             '2affc98dd0e18a404ee20a10eebe13cba121b86df106af8633959354a4293f42',
                                    'outputs': [
                                        '112007d71fa7e120c60fb392a64fd69de891a60c667d9ea9e5d9d9d617263be6c20202',
                                        '112007a90f66c661b32625f17e27177034a6d2cb552f89cba8c78868705ae276897df6',
                                    ],
                                    'payload_sha512':
                                        'bb0e5d9898c92b9b922a4de677ed6cab106ed5c90e975941cd5d1e22ce6f0d39'
                                        '7b812c7152796b410a9cfe1d3fd4af080c6ee88c9548fc8393e7a55cae596b8c',
                                    'signer_public_key': '02d1fbda50dbcd0d3c286a6a9fa71aa7c'
                                                         'e2d97159b90ddd463e0816422d621e135',
                                },
                                'header_signature': 'e96318d4e6810870f69b494ff5305bd7b9e37e6f4fb5352ef8e5eb3653fb03b7'
                                                    '240e87b1af5c5c512d84cf36b5c24fc97b15b0a0411a74d488abd44b517572e8',
                                'payload': 'EksSRjExMjAwN2Q3MWZhN2UxMjBjNjBmYjM5MmE2NGZkNjlkZTg5'
                                           'MWE2MGM2NjdkOWVhOWU1ZDlkOWQ2MTcyNjNiZTZjMjAyMDIY6Ac=',
                            },
                        ],
                    },
                ],
                'header': {
                    'batch_ids': [
                        '6f200995e766da7218ec2a3d0aeabbe1151128063cdf4e954cd08390a879b28e'
                        '085a06f8708d2e6bb34f6501e8ddc981f0353627c1d4f90c80a656a8090c8751',
                        '257353cb1180bdce4e19f290e4bfdb48212744a8ae08f6fc974e8c7c2cfe4692'
                        '19d257a7c62197bd614b9dc13cd562c6612aee45ab0bccfcdd6b0d1ed0b3cdcf',
                    ],
                    'block_num': '190',
                    'consensus': 'RGV2bW9kZcsBkH/e/VBqd/U/9wICwe3sngQQIziXCRP1ZB2SFXoM',
                    'previous_block_id': 'fe56a16dab009cc96e7125c647b6c71eb1063818cf8dece283b125423ecb184f'
                                         '7f1e61802bf66382da904698413f80831031f8a1b29150260c3fa4db537fdf4c',
                    'signer_public_key': '02d1fbda50dbcd0d3c286a6a9fa71aa7ce2d97159b90ddd463e0816422d621e135',
                },
            },
        ],
    }

    mock_get_blocks = mocker.patch('cli.block.service.loop.run_until_complete')
    mock_get_blocks.return_value = blocks

    expected_result = {
        'result': blocks.get('data'),
    }

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-list',
        '--ids',
        blocks_ids,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output)


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_blocks_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get a list of blocks by passing node URL with an explicit protocol.
    Expect: the following node URL contains the protocol error message.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
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
