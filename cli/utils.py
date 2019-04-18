"""
Provide utils for command line interface.
"""
import json
import re
import sys

import click
from remme import Remme

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND,
    FAMILY_NAMES,
)


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
    Validate function for list of ids.
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


def validate_limit(limit):
    """
    Validate function for limit.
    """
    if limit is None:
        return

    if limit <= 0:
        click.echo(
            'The following limit `{limit}` should be a positive.'.format(limit=limit))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    return limit


def validate_sign(sign, regexp_pattern, type_sign):
    """
    Validate function for signature.
    """
    if sign is None:
        return

    if not re.match(pattern=regexp_pattern, string=sign) is not None:

        click.echo(
            'The following {type_sign} `{sign}` is not valid.'.format(sign=sign, type_sign=type_sign))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    return sign


def validate_family_name(family_name):
    """
    Validate function for family name.
    """
    if family_name is None:
        return

    if family_name not in FAMILY_NAMES:

        click.echo(
            'The following family name `{family_name}` is not valid.'.format(family_name=family_name))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    return family_name
