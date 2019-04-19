"""
Provide utils for command line interface.
"""
import json

from remme import Remme


def dict_to_pretty_json(data):
    """
    Convert dictionary to string with indents as human readable text.
    """
    return json.dumps(data, indent=4, sort_keys=True)


def get_network(node_url):
    """
    Create object for sending requests to chain.
    """
    if node_url is None:
        node_url = 'localhost'

    remme = Remme(network_config={
        'node_address': str(node_url) + ':8080',
    })
    return remme
