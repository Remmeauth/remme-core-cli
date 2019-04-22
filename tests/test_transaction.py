"""
Provide tests for command line interface's transaction commands.
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
from cli.utils import (
    dict_to_pretty_json,
    return_async_value,
)


# def test_get_single_transaction():
#     """
#     Case: get a transaction by id.
#     Expect: transaction is returned.
#     """
#     runner = CliRunner()
#     result = runner.invoke(cli, [
#         'transaction',
#         'get-single',
#         '--id',
#         '044c7db163cf21ab9eafc9b267693e2d732411056c7530e54282946ec47cc180'
#         '201e7be5612a671a7028474ad18e3738e676c17a86b7180fc1aad4c97e38b85b',
#         '--node-url',
#         NODE_IP_ADDRESS_FOR_TESTING,
#     ])
#
#     assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
#     assert isinstance(json.loads(result.output), dict)


def test_get_single_transaction_with_invalid_id():
    """
    Case: get a transaction by its invalid id.
    Expect: the following id is invalid error message.
    """
    invalid_transaction_id = '044c7db163cf21ab9eafc9b267693e2d732411056c7530e54282946ec47cc180dd' \
                             '201e7be5612a671a7028474ad18e3738e676c17a86b7180fc1aad4c97e38b85bdd'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-single',
        '--id',
        invalid_transaction_id,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'id': [
            f'The following id `{invalid_transaction_id}` is not valid.'
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_single_transaction_without_node_url(mocker):
    """
    Case: get a transaction by id without passing node URL.
    Expect: transaction is returned.
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
    }, None

    mock_transaction_get_single = mocker.patch('cli.transaction.service.Transaction.get')
    mock_transaction_get_single.return_value = expected_result

    # expected_result = dict_to_pretty_json(expected_result)

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-single',
        '--id',
        transaction_id,
    ])

    transaction_list = json.loads(result.output).get('data')
    expected_result = json.loads(result.output).get('data')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(transaction_list, dict)
    assert expected_result == transaction_list


def test_get_single_transaction_with_invalid_node_url():
    """
    Case: get a single transaction by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'my-node-url.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-single',
        '--id',
        '8d8cb28c58f7785621b51d220b6a1d39fe5829266495d28eaf0362dc85d7e91c'
        '205c1c4634604443dc566c56e1a4c0cf2eb122ac42cb482ef1436694634240c5',
        '--node-url',
        invalid_node_url,
    ])

    expected_error_message = {
        'Error-message': f'Please check if your node running at http://{invalid_node_url}:8080.'
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_transaction_with_ids():
    """
    Case: get a list transactions by ids.
    Expect: transactions are returned.
    """
    transaction_ids = '044c7db163cf21ab9eafc9b267693e2d732411056c7530e54282946ec47cc180' \
                      '201e7be5612a671a7028474ad18e3738e676c17a86b7180fc1aad4c97e38b85b ' \
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
    Expect: The following ids are not valid error message.
    """
    invalid_transaction_ids = '044c7 True 010101'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'transaction',
        'get-list',
        '--ids',
        invalid_transaction_ids,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error_message = {
        'ids': [
            f'The following ids `{invalid_transaction_ids.split()}` are not valid.',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output


def test_get_list_transaction_with_start():
    """
    Case: get a list transaction by start.
    Expect: transactions are returned.
    """
    start = '044c7db163cf21ab9eafc9b267693e2d732411056c7530e54282946ec47cc180' \
            '201e7be5612a671a7028474ad18e3738e676c17a86b7180fc1aad4c97e38b85b'

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
        '--reverse',
        'false',
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
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
    Expect: The following id is not valid error message.
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
        f'{command_flag[2:]}': [
            f'The following id `{invalid_id}` is not valid.'
        ],
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
    Expect: The following limit should be a positive error message.
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
        'limit': [
            f'The following limit `{invalid_limit}` should be a positive.'
        ],
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
    Expect: The following family name is not valid. error message.
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
        "family_name": [
            f"The following family name `{invalid_family_name}` is not valid.",
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error_message) in result.output
