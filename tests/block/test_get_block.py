"""
Provide tests for command line interface's get block by its identifier command.
"""
import json

import pytest
from click.testing import CliRunner

from cli.constants import (
    DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    FAILED_EXIT_FROM_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json

EXISTING_BLOCK_IDENTIFIER = '95849a2a9a4775b6432b181e12749c43724682e37ca3560223586b01cbb40593' \
                            '31a7d970e4ebfdc328cd000adb4ddc9e3296b5cfb7045543006ca58214c25eb7'


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
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
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
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
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
    Expect: block data is returned from a node on localhost.
    """
    block = {
        'data': {
            'batches': [
                {
                    'header': {
                        'signer_public_key': '03309c84260e7265a296c77df42397372c658e30541ddc99b39cc52ce1f86dfb19',
                        'transaction_ids': [
                            '384bea4918e3396d6f0afb68c922f9b7d9454a6036891759ce5fbbc959e541ca'
                            '50fe9da7fc05b291bab0e77730808aa3bab831b0e2ca89f51a47e85f9962073b',
                        ],
                    },
                    'header_signature': '2b892618024170f23a77c9ebd4c1205bfbc3a032a644c5664290735a29400b6f'
                                        '29df1657fac3f3b4f880ee0a0cac3841195c316a324672a7fc41b397cb0ac1cc',
                    'trace': 'false',
                    'transactions': [
                        {
                            'header': {
                                'batcher_public_key': '03309c84260e7265a296c77df42397372'
                                                      'c658e30541ddc99b39cc52ce1f86dfb19',
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
                                'payload_sha512': 'a239acce64f765e9f2d9abdcb35172ed99a7a1927d0ea710bd7dac9caf0271fe'
                                                  '2d22a73c7f5d5b1e444531eea1b22e9cd0516a16c3d578542c2cd4ad012813f5',
                                'signer_public_key': '03309c84260e7265a296c77df42397372'
                                                     'c658e30541ddc99b39cc52ce1f86dfb19',
                            },
                            'header_signature': '384bea4918e3396d6f0afb68c922f9b7d9454a6036891759ce5fbbc959e541ca'
                                                '50fe9da7fc05b291bab0e77730808aa3bab831b0e2ca89f51a47e85f9962073b',
                            'payload': 'CtICCAISgAE3YmFjNjcwNWE4NWZiNTg1Mjc1NzIwYzI0MzIzMmVlZDk0MTY5ZTFiNjczYzI3M'
                                       'Dk1OGJkODlmYjdjYjk1ZmY3MDdiOWFmYWRhNGQ2NDkzOTUxMmU5MDQzYzAxYzk0NDY1MGY1ZG'
                                       'Y3M2YzODVjOGY4Yjk1ZGZjOTllOTYzNmQwYhpCMDMzMDljODQyNjBlNzI2NWEyOTZjNzdkZjQ'
                                       'yMzk3MzcyYzY1OGUzMDU0MWRkYzk5YjM5Y2M1MmNlMWY4NmRmYjE5IoABMTE2YWY2MmM4NzIx'
                                       'MmM1Y2VhMjdhMGQ0ZmQzMjRiMjY4MjEyMjA0ODQ0M2VjNzNmOGI0YWE2OWQxM2NkYTU3OTQwM'
                                       'jRiNjhlZTMwN2EzY2ZkZGU1ZTJhZTI3MmEzN2NmYjE0MjRhNmJiODZiZjUxZjA3MTYwOGZiZm'
                                       'M2MWQzMGIo2/Lq5gU=',
                        },
                    ],
                },
            ],
            'header': {
                'batch_ids': [
                    '2b892618024170f23a77c9ebd4c1205bfbc3a032a644c5664290735a29400b6f'
                    '29df1657fac3f3b4f880ee0a0cac3841195c316a324672a7fc41b397cb0ac1cc',
                    '39a8690637cd926c3b8bbc008768d0f4bc9f3fb90e9275ae1a5e0689d582ac96'
                    '067ed804db3271135a2fa337f77daa3ac8c1abf77467c1ff65f36a4e2ab398b9',
                ],
                'block_num': '3',
                'consensus': 'RGV2bW9kZVvhE13lUZSAXG1nKz4P557eT/VZW3jE16JXMMAt4mWz',
                'previous_block_id': '116af62c87212c5cea27a0d4fd324b2682122048443ec73f8b4aa69d13cda579'
                                     '4024b68ee307a3cfdde5e2ae272a37cfb1424a6bb86bf51f071608fbfc61d30b',
                'signer_public_key': '03309c84260e7265a296c77df42397372c658e30541ddc99b39cc52ce1f86dfb19',
                'state_root_hash': 'dc3f81453b7a69ae88d5886929b11e39adf232b1a22188f8c85db78778640fa0',
            },
            'header_signature': '95849a2a9a4775b6432b181e12749c43724682e37ca3560223586b01cbb40593'
                                '31a7d970e4ebfdc328cd000adb4ddc9e3296b5cfb7045543006ca58214c25eb7',
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
    Case: get a block by identifier by passing an invalid node URL.
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
    Case: get a block by identifier by passing node URL with an explicit protocol.
    Expect: the following node URL contains a protocol error message.
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
    Case: get a block by identifier by passing the non-existing node URL.
    Expect: check if node running at the URL error message.
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
    Case: get a block by identifier by passing the non-existing identifier.
    Expect: block with an identifier not found error message.
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
        DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'errors': f'Block with id `{non_existing_block_identifier}` not found.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
