"""
Provide tests for command line interface's account commands.
"""
import json

from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli


def test_get_balance():
    """
    Case: get a balance of an account by address.
    Expect: balance is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        '1120076ecf036e857f42129b58303bcf1e03723764a1702cbe98529802aad8514ee3cf',
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert True is isinstance(json.loads(result.output), int)


def test_get_balance_invalid_address():
    """
    Case: get a balance of an account by invalid address.
    Expect: the following address is invalid error message.
    """
    invalid_address = '1120076ecf036e857f42129b5830'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'account',
        'get-balance',
        '--address',
        invalid_address,
        '--node-url',
        NODE_IP_ADDRESS_FOR_TESTING,
    ])

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert f'The following address `{invalid_address}` is invalid.' in result.output
