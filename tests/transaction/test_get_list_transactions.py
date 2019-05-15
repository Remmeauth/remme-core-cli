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
    RELEASE_0_10_0_NODE_ADDRESS,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


def test_get_list_transactions_with_all_parameters(mocker):
    """
    Case: get a list transactions by identifier, identifier starting from, limit, head, family name, reverse.
    Expect: transaction are returned from node on localhost.
    """
    transaction_id = '79a2780e9f07ca58d97b9de346730ddaba85dbb520778eb3d704cd214f6c580f' \
                     '4f7fe4aa0e4fa9238e535f4af7e2dbae4134b4a726b36a5369c1cb4e971a2568'

    head = '95d78133eb98628d5ff17c7d1972b9ab03e50fceeb8e199d98cb52078550f547' \
           '3bb001e57c116238697bdc1958eaf6d5f096f7b66974e1ea46b9c9da694be9d9'

    expected_result = {
        'data': {
            "header": {
                "batcher_public_key": "02a65796f249091c3087614b4d9c292b00b8eba580d045ac2fd781224b87b6f13e",
                "dependencies": [],
                "family_name": "account",
                "family_version": "0.1",
                "inputs": [
                    "0000000000000000000000000000000000000000000000000000000000000000000001",
                ],
                "nonce": "0x1.73309477e6e96p+30",
                "outputs": [
                    "0000000000000000000000000000000000000000000000000000000000000000000001",
                    "112007e5116c7f40c9ba679bedd8b50fff0a316b1eb0611a3cc1ceb39c56d206588624",
                ],
                "payload_sha512": "5bc11b6e912e3d16f90b49e4ef08661f827b8855c9d87deb5bad497a99107b36774b770"
                                  "15cbe9e4c0a8d4763746c1b93e704f5a32d2d4f1c7fdddf5808013961",
                "signer_public_key": "02a65796f249091c3087614b4d9c292b00b8eba580d045ac2fd781224b87b6f13e",
            },
            "header_signature": "79a2780e9f07ca58d97b9de346730ddaba85dbb520778eb3d704cd214f6c580f"
                                "4f7fe4aa0e4fa9238e535f4af7e2dbae4134b4a726b36a5369c1cb4e971a2568",
            "payload": "CAESBwiAoJSljR0=",
        },
    }

    mock_get_transaction_by_ids = mocker.patch('cli.transaction.service.loop.run_until_complete')
    mock_get_transaction_by_ids.return_value = expected_result

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--ids',
        transaction_id,
        '--start',
        transaction_id,
        '--limit',
        1,
        '--head',
        head,
        '--family-name',
        'account',
        '--reverse',
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output).get('result')


def test_get_list_transactions_with_ids():
    """
    Case: get a list transactions by identifiers.
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

    expected_header_signature = '6601e240044b00db4b7e5eda7800e88236341077879a4a9cf5a1b1f9fb2ece87' \
                                '7bc9a43808d429e68f4d65ee8d7231e4e8711e705ad51be7888d1a7f25b57717'

    result_header_signature = json.loads(result.output).get('result').get('data')[0].get('header_signature')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(json.loads(result.output), dict)
    assert expected_header_signature == result_header_signature


def test_get_list_transactions_with_invalid_ids():
    """
    Case: get a list transactions by invalid identifiers.
    Expect: the following identifier are not valid error message.
    """
    invalid_id = '044c7'
    transaction_ids = '044c7db163cf21ab9eafc9b267693e2d732411056c7530e54282946ec47cc180' \
                      '201e7be5612a671a7028474ad18e3738e676c17a86b7180fc1aad4c97e38b85b, ' \
                      f'{invalid_id}'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--ids',
        transaction_ids,
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


def test_get_list_transactions_with_start():
    """
    Case: get a list transactions by transaction identifier starting from.
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


def test_get_list_transactions_with_reverse():
    """
    Case: get a list transactions by reverse.
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


def test_get_list_transactions_by_head():
    """
    Case: get a list transactions by block identifier.
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
def test_get_list_transactions_with_invalid_start_head(command_flag):
    """
    Case: get a list transactions by invalid block identifier and transaction identifier starting from.
    Expect: the following identifier is not valid error message.
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
                f'The following identifier `{invalid_id}` is invalid.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_transactions_with_limit():
    """
    Case: get a list transactions by limit.
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


def test_get_list_transactions_with_invalid_limit():
    """
    Case: get a list transactions by invalid limit.
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
                'Limit must be greater than 0.',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_transactions_with_family_name():
    """
    Case: get a list transactions by family name.
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


def test_get_list_transactions_with_invalid_family_name():
    """
    Case: get a list transactions by invalid family name.
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


def test_get_list_transactions_with_invalid_node_url():
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


def test_get_list_transactions_without_node_url(mocker):
    """
    Case: get a list transactions by identifier without passing node URL.
    Expect: transactions are returned from node on localhost.
    """
    transaction_id = '8d8cb28c58f7785621b51d220b6a1d39fe5829266495d28eaf0362dc85d7e91c' \
                     '205c1c4634604443dc566c56e1a4c0cf2eb122ac42cb482ef1436694634240c5'

    expected_result = {
        'data': {
            'header': {
                'batcher_public_key': '02a65796f249091c3087614b4d9c292b00b8eba580d045ac2fd781224b87b6f13e',
                'family_name': 'sawtooth_settings',
                'family_version': '1.0',
                'inputs': [
                    '000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b',
                    '000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c12840f169a04216b7',
                    '000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1918142591ba4e8a7',
                    '000000a87cb5eafdcca6a8f82af32160bc5311783bdad381ea57b4e3b0c44298fc1c14',
                ],
                'outputs': [
                    '000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b',
                    '000000a87cb5eafdcca6a8f82af32160bc5311783bdad381ea57b4e3b0c44298fc1c14',
                ],
                'payload_sha512': '82dd686e5298d24826d68ec2cdfbd1438a1b1d37a88abeacd24e25386d5939fa'
                                  '139c3ab8b33ef594df804281c638887a0b9308c1f0a0922c5240202a4e2d0595',
                'signer_public_key': '02a65796f249091c3087614b4d9c292b00b8eba580d045ac2fd781224b87b6f13e',
                'dependencies': [],
                'nonce': '',
            },
            'header_signature': '8d8cb28c58f7785621b51d220b6a1d39fe5829266495d28eaf0362dc85d7e91c'
                                '205c1c4634604443dc566c56e1a4c0cf2eb122ac42cb482ef1436694634240c5',
            'payload': 'CAESRAoic2F3dG9vdGgudmFsaWRhdG9yLmJhdGNoX2luamVj'
                       'dG9ycxIKYmxvY2tfaW5mbxoSMHhhNGY2YzZhZWMxOWQ1OTBi',
        },
    }

    mock_get_transaction_by_ids = mocker.patch('cli.transaction.service.loop.run_until_complete')
    mock_get_transaction_by_ids.return_value = expected_result

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--ids',
        transaction_id,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output).get('result')


@pytest.mark.parametrize('node_url_with_protocol', ['http://masternode.com', 'https://masternode.com'])
def test_get_list_transactions_node_url_with_protocol(node_url_with_protocol):
    """
    Case: get list transactions by passing node URL with explicit protocol.
    Expect: the following node URL contains protocol error message.
    """
    transaction_id = '8d8cb28c58f7785621b51d220b6a1d39fe5829266495d28eaf0362dc85d7e91c' \
                     '205c1c4634604443dc566c56e1a4c0cf2eb122ac42cb482ef1436694634240c5'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get',
        '--id',
        transaction_id,
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


def test_get_transactions_identifiers():
    """
    Case: get a list of transactions' identifiers.
    Expect: a list of transactions' identifiers is returned.
    """
    transaction_id = 'eb662acc48d313c9bba4a72359b0462d607bba8fc66aeb3d169d02fafd21849b' \
                     '6bf8bea8396b54b6fc907e1cce2a386f76bd19889d0f3e496b45b8440b161ebc'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--ids-only',
        '--node-url',
        RELEASE_0_10_0_NODE_ADDRESS,
    ])

    list_of_identifiers = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    for identifier in list_of_identifiers:
        assert identifier == transaction_id
        break


def test_get_transactions_identifiers_with_all_parameters():
    """
    Case: get a list of transactions' identifiers with all parameters.
    Expect: a list of transactions' identifiers is returned.
    """
    transaction_ids = '3c16f739202a58c022115b3a9ded2864ccfdfe36c3ee697904b0ee6414f5e237' \
                      '375b1299798f6f9e1f9303a9728367bab32b21b51c20eb08c8dc26ec1f0d4878, ' \
                      '43ba216bafdffe83ea9383b741c9839c1894b3d2f851c1981649e76ef2dbd3d6' \
                      '62bc5111ff918c78d76881c6ba636c84c673df96b5794398fccaec124d1f7beb'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--ids-only',
        '--start',
        '3c16f739202a58c022115b3a9ded2864ccfdfe36c3ee697904b0ee6414f5e237'
        '375b1299798f6f9e1f9303a9728367bab32b21b51c20eb08c8dc26ec1f0d4878',
        '--limit',
        2,
        '--node-url',
        RELEASE_0_10_0_NODE_ADDRESS,
    ])

    list_of_identifiers = json.loads(result.output).get('result')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    for identifier in list_of_identifiers:
        assert identifier in transaction_ids


def test_get_transactions_identifiers_without_node_url(mocker):
    """
    Case: get a list of transactions' identifiers without passing node URL.
    Expect: a list of transactions' identifiers is returned from a node on localhost.
    """
    expected_transactions = {
        'data': [
            {
                'header': {
                    'batcher_public_key': '03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad',
                    'dependencies': [],
                    'family_name': 'sawtooth_settings',
                    'family_version': '1.0',
                    'inputs': [
                        '000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b',
                        '000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c12840f169a04216b7',
                        '000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1918142591ba4e8a7',
                        '000000a87cb5eafdcca6a8f82af32160bc53119b8878ad4d2117f2e3b0c44298fc1c14',
                    ],
                    'nonce': '',
                    'outputs': [
                        '000000a87cb5eafdcca6a8cde0fb0dec1400c5ab274474a6aa82c1c0cbf0fbcaf64c0b',
                        '000000a87cb5eafdcca6a8f82af32160bc53119b8878ad4d2117f2e3b0c44298fc1c14',
                    ],
                    'payload_sha512': '8a290d2b3702068f81ec1e7a86c2329d341ff0a8b526e8745f47a2b9828dd6b9'
                                      'd08600a07a173c4ee90a2ac079d2acc5718bb7d5b5fb80177bf652b6f76422cd',
                    'signer_public_key': '03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad',
                },
                'header_signature': '656219b616e7ee1f10ae45f1020641a829725bcf1c351734c80df1a8a4ba4824'
                                    '6b8d75cd69cf0049e5d1fc787c45f65308be66c50cbd3c93ac74d1e9f92d1bcd',
                'payload': 'CAESggIKKXNhd3Rvb3RoLnZhbGlkYXRvci5ibG9ja192YWxpZGF0aW9uX3J1bGVzEsABTm9mWDoxLGJsb2NrX2lu'
                           'Zm87WGF0WTpibG9ja19pbmZvLDA7bG9jYWw6MDtOb2ZYOjEsY29uc2Vuc3VzX2FjY291bnQ7WGF0WTpjb25zZW5z'
                           'dXNfYWNjb3VudCwxO2xvY2FsOjA7Tm9mWDoxLG9ibGlnYXRvcnlfcGF5bWVudDtYYXRZOm9ibGlnYXRvcnlfcGF5'
                           'bWVudCwyO2xvY2FsOjA7Tm9mWDoxLGJldDtYYXRZOmJldCwtMTtsb2NhbDowGhIweDZiMGQ5NGFjMzU4MGU4NDY=',
            },
        ],
    }

    mock_get_transactions = mocker.patch('cli.transaction.service.Transaction.get_list')
    mock_get_transactions.return_value = expected_transactions, None

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--ids-only',
    ])

    expected_result = {
        'result': [expected_transactions.get('data')[0].get('header_signature')],
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output)
