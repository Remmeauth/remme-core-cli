"""
Provide implementation of the custom fields.
"""
import re

from marshmallow import (
    ValidationError,
    fields,
)

from cli.constants import (
    FAMILY_NAMES,
    HEADER_SIGNATURE_REGEXP,
)


class IdList(fields.Field):
    """
    List of ids custom field.

    Raises a ValidationError if ids do not correspond to HEADER_SIGNATURE_REGEXP.
    """

    def _deserialize(self, value, attr, obj, **kwargs):

        value = value.split()
        for id_ in value:

            if not re.match(pattern=HEADER_SIGNATURE_REGEXP, string=id_) is not None:
                raise ValidationError(f'The following ids `{value}` are not valid.')

        return value


class FamilyName(fields.Field):
    """
    FamilyName custom field.

    Raises a ValidationError if family name not exist.
    """

    def _deserialize(self, value, attr, obj, **kwargs):

        if value not in FAMILY_NAMES:
            raise ValidationError(f'The following family name `{value}` is not valid.')

        return value


class Limit(fields.Field):
    """
    Id custom field.

    Raises a ValidationError if the limit is a negative number.
    """

    def _deserialize(self, value, attr, obj, **kwargs):

        if value <= 0:
            raise ValidationError(f'The following limit `{value}` should be a positive.')

        return value


class Id(fields.Field):
    """
    Id custom field.

    Raises a ValidationError if id not corresponds to HEADER_SIGNATURE_REGEXP.
    """

    def _deserialize(self, value, attr, obj, **kwargs):

        if not re.match(pattern=HEADER_SIGNATURE_REGEXP, string=value) is not None:
            raise ValidationError(f'The following id `{value}` is not valid.')

        return value
