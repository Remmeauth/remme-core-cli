"""
Provide tests for command line interface's block commands.
"""
import json

from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json


def test_get_block():
    """
    Case: get a block by identifier.
    Expect: block data is returned, batches are presented, header signature is block identifier.
    """
    existing_block_indifier = \
        '4a7897650db9863aca34874778e6c5802f86c3df0e22b39cfea730bc83654357' \
        '037a422f8ef51ac85a9bc61d2484bd0f37be10cfc861588c41dc6f1bbfd92cde'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-single',
        '--id',
        existing_block_indifier,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    block = json.loads(result.output).get('result')

    batches = block.get('batches')
    header_signature = block.get('header_signature')

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert existing_block_indifier == header_signature
    assert len(batches) > 0


def test_get_block_invalid_identifier():
    """
    Case: get a block by invalid identifier.
    Expect: the following block is invalid error message.
    """
    invalid_block_identifier = '152f3be91d8238538a83077ec8cd5d1d937767c0930eea61b59151b0dfa7c5a1'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-single',
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
    Case: get a balance of an account by address without passing node URL.
    Expect: balance is returned from node on localhost.
    """
    balance = 13500

    mock_account_get_balance = mocker.patch('cli.account.service.loop.run_until_complete')
    mock_account_get_balance.return_value = balance

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
    ])

    expected_result = {
        'result': {
            'balance': 13500,
        },
    }

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_result == json.loads(result.output)


def test_get_block_invalid_node_url():
    """
    Case: get a block by passing invalid node URL.
    Expect: the following node URL is invalid error message.
    """
    invalid_node_url = 'domainwithoutextention'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
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


def test_get_block_node_url_with_http():
    """
    Case: get a block by passing node URL with explicit HTTP protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_http_protocol = 'http://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
        '--node-url',
        node_url_with_http_protocol,
    ])

    expected_error = {
        'errors': {
            'node_url': [
                f'Pass the following node URL `{node_url_with_http_protocol}` without protocol (http, https, etc.).',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_block_node_url_with_https():
    """
    Case: get a block by passing node URL with explicit HTTPS protocol.
    Expect: the following node URL contains protocol error message.
    """
    node_url_with_https_protocol = 'https://masternode.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
        '--node-url',
        node_url_with_https_protocol,
    ])

    expected_error = {
        'errors': {
            'node_url': [
                f'Pass the following node URL `{node_url_with_https_protocol}` without protocol (http, https, etc.).',
            ],
        },
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output


def test_get_block_non_existing_identifier():
    """
    Case: get a block by passing non-existing identifier.
    Expect: check if node running at URL error message.
    """
    non_existing_block_identifier = '7a7897650db9863aca34874778e6c5802f86c3df0e22b39cfea730bc83654357' \
                                    '037a422f8ef51ac85a9bc61d2484bd0f37be10cfc861588c41dc6f1bbfd92cde'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'block',
        'get-single',
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


def test_get_block_non_existing_node_url():
    """
    Case: get a block by passing non-existing node URL.
    Expect: check if node running at URL error message.
    """
    non_existing_node_url = 'non-existing-node.com'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'node',
        'get-configs',
        '--node-url',
        non_existing_node_url,
    ])

    expected_error = {
        'errors': f'Please check if your node running at http://{non_existing_node_url}:8080.',
    }

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert dict_to_pretty_json(expected_error) in result.output
