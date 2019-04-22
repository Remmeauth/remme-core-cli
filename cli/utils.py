"""
Provide utils for command line interface.
"""
import json

from cli.config import ConfigFile


def dict_to_pretty_json(data):
    """
    Convert dictionary to string with indents as human readable text.
    """
    return json.dumps(data, indent=4, sort_keys=True)


def default_node_url():
    """
    Get default node URL.
    """
    config_parameters = ConfigFile().parse()

    if config_parameters.node_url is None:
        return 'localhost'

    else:
        return config_parameters.node_url
