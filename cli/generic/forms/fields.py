"""
Provide generic form fields.
"""
import re

from marshmallow import (
    ValidationError,
    fields,
)

from cli.constants import PRIVATE_KEY_REGEXP


class PrivateKeyField(fields.Field):
    """
    Implements validation of the private key.

    References:
        - https://marshmallow.readthedocs.io/en/3.0/custom_fields.html
    """

    def _deserialize(self, value, attr, data, **kwargs):
        """
        Validate data (private key) that was passed to field.
        """
        private_key = value

        if re.match(pattern=PRIVATE_KEY_REGEXP, string=private_key) is None:
            raise ValidationError(f'The following private key `{private_key}` is invalid.')

        return value
