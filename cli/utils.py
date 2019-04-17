"""
Provide utils for command line interface.
"""

import sys
import re
import click
import json
from cli.constants import FAILED_EXIT_FROM_COMMAND

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


def validate_ids(ids, regexp_pattern):
    """
    Validation function for list of ids.
    """
    if ids is None:
        return

    ids = ids.split(" ")
    for id_ in ids:

        if not re.match(pattern=regexp_pattern, string=id_) is not None:

            click.echo(
                'The following ids `{ids}` are not valid.'.format(ids=id_))
            sys.exit(FAILED_EXIT_FROM_COMMAND)

    return ids


def validate_id(id_, regexp_pattern):
    """
    Validation function for id.
    """
    if id_ is None:
        return

    if not re.match(pattern=regexp_pattern, string=id_) is not None:

        click.echo(
            'The following id `{id_}` is not valid.'.format(id_=id_))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    return id_


def validate_limit(limit):
    """
    Validation function for limit.
    """
    if limit is None:
        return

    if limit <= 0:
        click.echo(
            'The following limit `{limit}` should be a positive.'.format(limit=limit))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    return limit


def validate_head_sign(sign, regexp_pattern):
    """
    Validation function for head.
    """
    if sign is None:
        return

    if not re.match(pattern=regexp_pattern, string=sign) is not None:

        click.echo(
            'The following header signature `{sign}` is not valid.'.format(sign=sign))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    return sign
