"""
Provide tests for command line interface's atomic swap commands.
"""
import json
import re

from click.testing import CliRunner

from cli.constants import (
    ADDRESS_REGEXP,
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
    PRIVATE_KEY_FOR_TESTING,
    SWAP_IDENTIFIER_REGEXP,
)
from cli.entrypoint import cli
from cli.utils import (
    dict_to_pretty_json,
    return_async_value,
)

# def test_get_swap_info():
#     """
#     Case: get information about atomic swap by swap identifier.
#     Expect: information about swap is returned.
#     """
#     runner = CliRunner()
#     result = runner.invoke(cli, [
#         'atomic-swap',
#         'get-info',
#         '--private-key-from',
#         PRIVATE_KEY_FOR_TESTING,
#         '--id',
#         '033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808',
#         '--node-url',
#         NODE_IP_ADDRESS_FOR_TESTING,
#     ])
#
#     assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
#
#     swap_info = json.loads(result.output)
#
#     assert re.match(pattern=ADDRESS_REGEXP, string=swap_info.get('sender_address')) is not None
#     assert re.match(pattern=ADDRESS_REGEXP, string=swap_info.get('receiver_address')) is not None
#     assert re.match(pattern=SWAP_IDENTIFIER_REGEXP, string=swap_info.get('swap_id')) is not None
#
#     assert isinstance(int(float(swap_info.get('amount'))), int)
#     assert isinstance(swap_info.get('is_initiator'), bool)


def test_get_swap_info_invalid_private_key_from():
    """
    Case: get information about atomic swap with invalid private key from.
    Expect: the following private key is invalid error message.
    """
    invalid_private_key = 'b03e31d2f310305eab249133b53b5fb327'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--private-key-from',
        invalid_private_key,
        '--id',
        '033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808',
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'private_key_from': [
            f'The following private key `{invalid_private_key}` is invalid.',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_swap_info_without_node_url(mocker):
    """
    Case: get information about atomic swap by swap identifier without passing node URL.
    Expect: information about swap is returned from node on localhost.
    """
    expected_swap_info = {
        'sender_address': '112007be95c8bb240396446ec359d0d7f04d257b72aeb4ab1ecfe50cf36e400a96ab9c',
        'receiver_address': '112007484def48e1c6b77cf784aeabcac51222e48ae14f3821697f4040247ba01558b1',
        'amount': '10.0000',
        'swap_id': '033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808',
        'secret_lock': '0728356568862f9da0825aa45ae9d3642d64a6a732ad70b8857b2823dbf2a0b8',
        'created_at': 1555943451,
        'sender_address_non_local': '0xe6ca0e7c974f06471759e9a05d18b538c5ced11e',
        'state': 'OPENED',
        'email_address_encrypted_optional': '',
        'secret_key': '',
        'is_initiator': False,
    }

    mock_swap_get_info = mocker.patch('cli.atomic_swap.service.AtomicSwap.get_info')
    mock_swap_get_info.return_value = return_async_value(expected_swap_info)

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--id',
        '033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808',
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    swap_info = json.loads(result.output)

    assert re.match(pattern=ADDRESS_REGEXP, string=swap_info.get('sender_address')) is not None
    assert re.match(pattern=ADDRESS_REGEXP, string=swap_info.get('receiver_address')) is not None
    assert re.match(pattern=SWAP_IDENTIFIER_REGEXP, string=swap_info.get('swap_id')) is not None

    assert isinstance(int(float(swap_info.get('amount'))), int)
    assert isinstance(swap_info.get('is_initiator'), bool)


def test_get_swap_info_invalid_swap_id():
    """
    Case: get information about atomic swap by invalid swap identifier.
    Expect: the following swap identifier is invalid error message.
    """
    invalid_swap_id = '033402fe1346742486b15a3a9966eb524927'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--id',
        invalid_swap_id,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    expected_error = {
        'id': [
            f'The following swap identifier `{invalid_swap_id}` is invalid.',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_swap_info_invalid_node_url():
    """
    Case: get information about atomic swap by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--id',
        '033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808',
        '--node-url',
        invalid_node_url,
    ])

    expected_error = {
        'node_url': [
            f'The following node URL `{invalid_node_url}` is invalid.',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_swap_info_node_url_with_http():
    """
    Case: get information about atomic swap by passing node URL with explicit HTTP protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_http_protocol = 'http://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--id',
        '033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808',
        '--node-url',
        node_url_with_http_protocol,
    ])

    expected_error = {
        'node_url': [
            f'Pass the following node URL `{node_url_with_http_protocol}` without protocol (http, https, etc.).',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_swap_info_node_url_with_https():
    """
    Case: get information about atomic swap by passing node URL with explicit HTTPS protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_https_protocol = 'https://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'atomic-swap',
        'get-info',
        '--private-key-from',
        PRIVATE_KEY_FOR_TESTING,
        '--id',
        '033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808',
        '--node-url',
        node_url_with_https_protocol,
    ])

    expected_error = {
        'node_url': [
            f'Pass the following node URL `{node_url_with_https_protocol}` without protocol (http, https, etc.).',
        ],
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
