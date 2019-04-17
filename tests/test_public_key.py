"""
Provide tests for command line interface's public key commands.
"""
import json
import re

from click.testing import CliRunner

from cli.constants import (
    ADDRESS_REGEXP,
    FAILED_EXIT_FROM_COMMAND,
    HEADER_SIGNATURE_REGEXP,
    PASSED_EXIT_FROM_COMMAND_CODE,
    PUBLIC_KEY_REGEXP,
    NODE_IP_ADDRESS_FOR_TESTING,
)
from cli.entrypoint import cli

PUBLIC_KEY_ADDRESS_PRESENTED_ON_THE_TEST_NODE = 'a23be14785e7b073b50e24f72e086675289795b969a895a7f02202404086946e8ddc5b'


def test_get_public_key_info():
    """
    Case: get information about public key by public key address.
    Expect: dictionary of public key information, keys matched regexp checking.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key',
        'get-single',
        '--address',
        PUBLIC_KEY_ADDRESS_PRESENTED_ON_THE_TEST_NODE,
        '--node-url',
        'node-6-testnet.remme.io',
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    for key, value in json.loads(result.output).items():
        if key == 'address':
            assert re.match(pattern=ADDRESS_REGEXP, string=value) is not None

        if key == 'entity_hash':
            assert re.match(pattern=HEADER_SIGNATURE_REGEXP, string=value) is not None

        if key in ('is_revoked', 'is_valid'):
            assert isinstance(value, bool)

        if key == 'owner_public_key':
            assert re.match(pattern=PUBLIC_KEY_REGEXP, string=value) is not None


def test_get_public_key_info_invalid_address():
    """
    Case: get information about public key by invalid address.
    Expect: the following address is not valid error message.
    """
    invalid_address = 'a23be14785e7b073b50e24f72e086675289795b969a895a7f02202404086946e8ddczz'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'public-key', 'get-single', '--address', invalid_address, '--node-url', NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert FAILED_EXIT_FROM_COMMAND == result.exit_code
    assert f'The following address `{invalid_address}` is not valid.' in result.output
