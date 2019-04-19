"""
Provide tests for implementation of the config commands.
"""
from cli.config import ConfigFile

CLI_CONFIG_FILE_NAME_EMPTY_FILE = 'remme-core-cli-empty-file'
CLI_CONFIG_FILE_NAME_WITHOUT_URL = 'remme-core-cli-without-url'


def test_get_node_url(create_config_file):
    """
    Case: get node url from configuration file.
    Expect: node url address in string format.
    """
    config = ConfigFile().parse()

    assert config.node_url == 'node-genesis-testnet.remme.io'


def test_get_node_url_without_node_url(create_config_file_without_node_url):
    """
    Case: get node url from configuration file without node url.
    Expect: none is returned.
    """
    config = ConfigFile().parse(name=CLI_CONFIG_FILE_NAME_WITHOUT_URL)

    assert config.node_url is None


def test_get_node_url_from_empty_file(create_empty_config_file):
    """
    Case: get node url from empty configuration file.
    Expect: none is returned.
    """
    config = ConfigFile().parse(name=CLI_CONFIG_FILE_NAME_EMPTY_FILE)

    assert config.node_url is None
