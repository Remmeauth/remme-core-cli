import sys
import re
import click
from cli.constants import FAILED_EXIT_FROM_COMMAND


def validate_ids(ids, regexp_pattern):

    if ids is None:
        return

    ids = ids.split(" ")
    for id_ in ids:

        if not re.match(pattern=regexp_pattern, string=id_) is not None:

            click.echo(
                'The following transaction ids `{ids}` are not valid.'.format(ids=id_))
            sys.exit(FAILED_EXIT_FROM_COMMAND)

    return ids


def validate_id(id_, regexp_pattern):

    if id_ is None:
        return

    if not re.match(pattern=regexp_pattern, string=id_) is not None:

        click.echo(
            'The following transaction id `{id_}` is not valid.'.format(id_=id_))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    return id_


def validate_limit(limit):

    if limit is None:
        return

    if limit <= 0:
        click.echo(
            'The following limit `{limit}` should be a positive.'.format(limit=limit))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    return limit


def validate_head_sign(sign, regexp_pattern):

    if sign is None:
        return

    if not re.match(pattern=regexp_pattern, string=sign) is not None:

        click.echo(
            'The following header signature `{sign}` is not valid.'.format(sign=sign))
        sys.exit(FAILED_EXIT_FROM_COMMAND)

    return sign
