"""
Provide forms for command line interface's block commands.
"""
import re

from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validates,
)

from cli.constants import DOMAIN_NAME_REGEXP
from cli.generic.forms.fields import BlockIdentifierField


class GetBlockByIdentifierForm(Schema):
    """
    Transfer tokens to address form.
    """

    id = BlockIdentifierField(required=True)
    node_url = fields.String(allow_none=True, required=False)

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
