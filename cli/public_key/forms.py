"""
Provide forms for command line interface's public key commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeURLField,
)


class GetPublicKeysForm(Schema):
    """
    Get a list of the addresses of the public keys form.
    """

    address = AccountAddressField(required=True)
    node_url = NodeURLField(allow_none=True, required=False)
