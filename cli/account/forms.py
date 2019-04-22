"""
Provide forms for command line interface's account commands.
"""
import re

from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validates,
)

from cli.constants import (
    ADDRESS_REGEXP,
    DOMAIN_NAME_REGEXP,
)


class GetAccountBalanceForm(Schema):
    """
    Get balance of the account form.
    """

    address = fields.String(required=True)
    node_url = fields.String(allow_none=True, required=False)

    @validates('address')
    def validate_address(self, address):
        """
        Validate account address.
        """
        if re.match(pattern=ADDRESS_REGEXP, string=address) is None:
            raise ValidationError(f'The following address `{address}` is invalid.')

    @validates('node_url')
    def validate_node_url(self, node_url):
        """
        Validate node URL.

        If node URL is localhost, it means client didn't passed any URL, so nothing to validate.
        """
        if node_url == 'localhost':
            return

        if 'http' in node_url or 'https' in node_url:
            raise ValidationError(f'Pass the following node URL `{node_url}` without protocol (http, https, etc.).')

        if re.match(pattern=DOMAIN_NAME_REGEXP, string=node_url) is None:
            raise ValidationError(f'The following node URL `{node_url}` is invalid.')
