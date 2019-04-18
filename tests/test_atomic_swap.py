"""
Provide tests for command line interface's public key commands.
"""
import re

from click.testing import CliRunner

from cli.constants import (
    NODE_IP_ADDRESS_FOR_TESTING,
    PASSED_EXIT_FROM_COMMAND_CODE,
    PUBLIC_KEY_REGEXP,
)
from cli.entrypoint import cli


def test_get_public_key():
    """
    Case: get the public keys of atomic swap.
    Expect: public key is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['atomic-swap', 'get-public-key', '--node-url', NODE_IP_ADDRESS_FOR_TESTING])

    public_key = result.output

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code

    assert re.match(pattern=PUBLIC_KEY_REGEXP, string=public_key) is not None
