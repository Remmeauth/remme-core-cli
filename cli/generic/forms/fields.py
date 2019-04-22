"""
Provide generic form fields.
"""
import re

from marshmallow import (
    ValidationError,
    fields,
)

from cli.constants import (
    PRIVATE_KEY_REGEXP,
    SWAP_IDENTIFIER_REGEXP,
)


class SwapIdField(fields.Field):
    """
    Implements validation of the swap identifier.

    References:
        - https://marshmallow.readthedocs.io/en/3.0/custom_fields.html
    """

    def _deserialize(self, value, attr, data, **kwargs):
        """
        Validate data (swap identifier) that was passed to field.
        """
        swap_id = value

        if re.match(pattern=SWAP_IDENTIFIER_REGEXP, string=swap_id) is None:
            raise ValidationError(f'The following swap identifier `{swap_id}` is invalid.')

        return value


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
