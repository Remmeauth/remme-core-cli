"""
Provide implementation of the generic form fields.
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
    PRIVATE_KEY_REGEXP,
)


class AccountAddressField(fields.Field):
    """
    Implements validation of the account address.

    References:
        - https://marshmallow.readthedocs.io/en/3.0/custom_fields.html
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (account address) that was passed to field.
        """
        address = value

        if re.match(pattern=ADDRESS_REGEXP, string=address) is None:
            raise ValidationError(f'The following address `{address}` is invalid.')

        return address


class FamilyNameField(fields.Field):
    """
    Implements validation of the family name.

    Raises a ValidationError if the family name not exist.

    References:
        - https://marshmallow.readthedocs.io/en/3.0/custom_fields.html
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (family name) that was passed to field.
        """
        if value not in FAMILY_NAMES:
            raise ValidationError(f'The following family name `{value}` is not valid.')

        return value


class IdListField(fields.Field):
    """
    Implements validation of the list identifiers.

    Raises a ValidationError if the identifier does not correspond to HEADER_SIGNATURE_REGEXP.

    References:
        - https://marshmallow.readthedocs.io/en/3.0/custom_fields.html
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (list identifiers) that was passed to field.
        """
        value = [v.strip() for v in value.split(',')]
        for id_ in value:

            if not re.match(pattern=HEADER_SIGNATURE_REGEXP, string=id_) is not None:
                raise ValidationError(f'The following ids `{value}` are not valid.')

        return value


class IdField(fields.Field):
    """
    Implements validation of the identifier.

    Raises a ValidationError if the identifier does not correspond to HEADER_SIGNATURE_REGEXP.

    References:
        - https://marshmallow.readthedocs.io/en/3.0/custom_fields.html
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (list identifier) that was passed to field.
        """
        if not re.match(pattern=HEADER_SIGNATURE_REGEXP, string=value) is not None:
            raise ValidationError(f'The following id `{value}` is not valid.')

        return value


class NodeURLField(fields.Field):
    """
    Implements validation of the node URL.

    If node URL is localhost, it means client didn't passed any URL, so nothing to validate.

    References:
        - https://marshmallow.readthedocs.io/en/3.0/custom_fields.html
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (node URL) that was passed to field.
        """
        node_url = value

        if node_url == 'localhost':
            return node_url

        if 'http' in node_url or 'https' in node_url:
            raise ValidationError(f'Pass the following node URL `{node_url}` without protocol (http, https, etc.).')

        if re.match(pattern=DOMAIN_NAME_REGEXP, string=node_url) is None:
            raise ValidationError(f'The following node URL `{node_url}` is invalid.')

        return node_url


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


class ReverseField(fields.Field):
    """
    Implements validation of the reverse.

    If reverse is True, reverse equal empty line.

    References:
        - https://marshmallow.readthedocs.io/en/3.0/custom_fields.html
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (reverse) that was passed to field.
        """
        if value:
            return ''

        return 'false'
