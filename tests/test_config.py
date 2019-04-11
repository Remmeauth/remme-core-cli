from cli.config import ConfigFile


def test_get_node_url(create_config_file):
    """
    Case: get node url from configuration file.
    Expect: node url address in string format.
    """
    config = ConfigFile().parse()

    assert config.node_url == 'node-genesis-testnet.remme.io'
