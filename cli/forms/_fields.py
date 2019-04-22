"""
Provide implementation of the custom fields.
"""
import re

from marshmallow import (
    ValidationError,
    fields,
)

from cli.constants import (
    ADDRESS_REGEXP,
    DOMAIN_NAME_REGEXP,
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


class NodeURL(fields.Field):
    """
    Validate node URL.

    If node URL is localhost, it means client didn't passed any URL, so nothing to validate.
    """

    def _deserialize(self, value, attr, obj, **kwargs):

        if value == 'localhost':
            return value

        if 'http' in value or 'https' in value:
            raise ValidationError(f'Pass the following node URL `{value}` without protocol (http, https, etc.).')

        if re.match(pattern=DOMAIN_NAME_REGEXP, string=value) is None:
            raise ValidationError(f'The following node URL `{value}` is invalid.')

        return value


class NodeAddress(fields.Field):
    """
    Validate account address.
    """

    def _deserialize(self, value, attr, obj, **kwargs):

        if re.match(pattern=ADDRESS_REGEXP, string=value) is None:
            raise ValidationError(f'The following address `{value}` is invalid.')

        return value
