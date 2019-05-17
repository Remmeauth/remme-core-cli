"""
Provide implementation of the generic form fields.

References:
    - https://marshmallow.readthedocs.io/en/3.0/custom_fields.html
"""
import re

from marshmallow import (
    ValidationError,
    fields,
)

from cli.constants import (
    ADDRESS_REGEXP,
    BATCH_IDENTIFIER_REGEXP,
    BLOCK_IDENTIFIER_REGEXP,
    DOMAIN_NAME_REGEXP,
    FAMILY_NAMES,
    PRIVATE_KEY_REGEXP,
    PUBLIC_KEY_ADDRESS_REGEXP,
    SWAP_IDENTIFIER_REGEXP,
    TRANSACTION_IDENTIFIER_REGEXP,
)


class AccountAddressField(fields.Field):
    """
    Implements validation of the account address.
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
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (family name) that was passed to field.
        """
        family_name = value

        if family_name not in FAMILY_NAMES:
            raise ValidationError(f'The following family name `{family_name}` is invalid.')

        return family_name


class TransactionIdentifiersListField(fields.Field):
    """
    Implements validation of the list of the identifiers.
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (list of the identifiers) that was passed to field.
        """
        validated_identifiers = []

        for identifier in value.split(','):
            identifier = identifier.strip()

            if re.match(pattern=TRANSACTION_IDENTIFIER_REGEXP, string=identifier) is None:
                raise ValidationError(f'The following identifier `{identifier}` is invalid.')

            validated_identifiers.append(identifier)

        return validated_identifiers


class TransactionIdentifierField(fields.Field):
    """
    Implements validation of the identifier.
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (identifier) that was passed to field.
        """
        transaction_identifier = value

        if re.match(pattern=TRANSACTION_IDENTIFIER_REGEXP, string=transaction_identifier) is None:
            raise ValidationError(f'The following identifier `{transaction_identifier}` is invalid.')

        return transaction_identifier


class BatchIdentifiersListField(fields.Field):
    """
    Implements validation of the list of the identifiers.
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (list of the identifiers) that was passed to field.
        """
        validated_identifiers = []

        for identifier in value.split(','):
            identifier = identifier.strip()

            if re.match(pattern=BATCH_IDENTIFIER_REGEXP, string=identifier) is None:
                raise ValidationError(f'The following identifier `{identifier}` is invalid.')

            validated_identifiers.append(identifier)

        return validated_identifiers


class BatchIdentifierField(fields.Field):
    """
    Implements validation of the identifier.
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (batch identifier) that was passed to field.
        """
        batch_identifier = value

        if re.match(pattern=BATCH_IDENTIFIER_REGEXP, string=batch_identifier) is None:
            raise ValidationError(f'The following identifier `{batch_identifier}` is invalid.')

        return batch_identifier


class NodeUrlField(fields.Field):
    """
    Implements validation of the node URL.

    If node URL is localhost, it means client didn't passed any URL, so nothing to validate.
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (node URL) that was passed to field.
        """
        node_url = value

        if node_url == 'localhost' or node_url == '127.0.0.1':
            return node_url

        if 'http' in node_url or 'https' in node_url:
            raise ValidationError(f'Pass the following node URL `{node_url}` without protocol (http, https, etc.).')

        if re.match(pattern=DOMAIN_NAME_REGEXP, string=node_url) is None:
            raise ValidationError(f'The following node URL `{node_url}` is invalid.')

        return node_url


class PrivateKeyField(fields.Field):
    """
    Implements validation of the private key.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        """
        Validate data (private key) that was passed to field.
        """
        private_key = value

        if re.match(pattern=PRIVATE_KEY_REGEXP, string=private_key) is None:
            raise ValidationError(f'The following private key `{private_key}` is invalid.')

        return private_key


class PublicKeyAddressField(fields.Field):
    """
    Implements validation of the public key address.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        """
        Validate data (public key address) that was passed to field.
        """
        public_key_address = value

        if re.match(pattern=PUBLIC_KEY_ADDRESS_REGEXP, string=public_key_address) is None:
            raise ValidationError(f'The following public key address `{public_key_address}` is invalid.')

        return public_key_address


class SwapIdentifierField(fields.Field):
    """
    Implements validation of the swap identifier.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        """
        Validate data (swap identifier) that was passed to field.
        """
        swap_identifier = value

        if re.match(pattern=SWAP_IDENTIFIER_REGEXP, string=swap_identifier) is None:
            raise ValidationError(f'The following swap identifier `{swap_identifier}` is invalid.')

        return swap_identifier


class BlockIdentifierField(fields.Field):
    """
    Implements validation of the block identifier.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        """
        Validate data (block identifier) that was passed to field.
        """
        block_identifier = value

        if re.match(pattern=BLOCK_IDENTIFIER_REGEXP, string=block_identifier) is None:
            raise ValidationError(f'The following block identifier `{block_identifier}` is invalid.')

        return block_identifier


class BlockIdentifiersListField(fields.Field):
    """
    Implements validation of the list of block identifiers.
    """

    def _deserialize(self, value, attr, obj, **kwargs):
        """
        Validate data (list of block identifiers) that was passed to field.
        """
        block_identifiers = value
        block_validated_identifiers = []

        for identifier in block_identifiers.split(','):
            identifier = identifier.strip()

            if re.match(pattern=BLOCK_IDENTIFIER_REGEXP, string=identifier) is None:
                raise ValidationError(f'The following block identifier `{identifier}` is invalid.')

            block_validated_identifiers.append(identifier)

        return block_validated_identifiers
