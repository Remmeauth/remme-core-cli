"""
Provide tests for implementation of the node private key file.
"""
import pytest

from cli.config import NodePrivateKey
from cli.errors import NotSupportedOsToGetNodePrivateKeyError


def test_node_private_key_get(create_node_private_key_file, node_private_key_file_path):
    """
    Case: get the node's private key.
    Expect: private key has been read from the node's private key file.
    """
    private_key = NodePrivateKey.get(file_path=node_private_key_file_path)
    assert '8a069bfff838f73d1b072ba72ee0f61b19d9b7216d5a735d7ff4d15063dd9772' == private_key


@pytest.mark.parametrize('operating_system', ['Darwin', 'Windows'])
def test_node_private_key_get_not_supported_os(operating_system, node_private_key_file_path, mocker):
    """
    Case: get the node's private key from not supported operating system.
    Expect: the operating system is not supported to get the node's private key error message.
    """
    mock_account_get_balance = mocker.patch('platform.system')
    mock_account_get_balance.return_value = operating_system

    with pytest.raises(NotSupportedOsToGetNodePrivateKeyError) as error:
        NodePrivateKey.get(file_path=node_private_key_file_path)

    assert 'The current operating system is not supported to get the node\'s private key.' in error.value.message


def test_node_private_key_get_from_non_existing_file(node_private_key_file_path):
    """
    Case: get the node's private key from the non-existing file.
    Expect: private key hasn't been founded on the machine error message.
    """
    with pytest.raises(FileNotFoundError) as error:
        NodePrivateKey.get(file_path=node_private_key_file_path)

    assert 'Private key hasn\'t been founded on the machine.' in str(error)
