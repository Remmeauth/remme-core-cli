"""
Provide tests for command line interface's public key commands.
"""
import json
import re

from click.testing import CliRunner

from cli.constants import (
    ADDRESS_REGEXP,
    FAILED_EXIT_FROM_COMMAND,
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli

ADDRESS_PRESENTED_ON_THE_TEST_NODE = '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf'


def test_get_public_keys():
    """
    Case: get a list of the public keys by account address.
    Expect: list of public keys, each public key matched regexp checking.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-list',
        '--address',
        ADDRESS_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    for public_key in json.loads(result.output):
        assert re.match(pattern=ADDRESS_REGEXP, string=public_key) is not None


def test_get_public_keys_invalid_address():
    """
    Case: get a list of the public keys by invalid address.
    Expect: the following address is not valid error message.
    """
    invalid_address = '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3zz'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key', 'get-list', '--address', invalid_address, '--node-url', NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert FAILED_EXIT_FROM_COMMAND == result.exit_code
    assert f'The following address `{invalid_address}` is not valid.' in result.output
