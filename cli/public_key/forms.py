"""
Provide forms for command line interface's account commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeURLField,
)


class GetPublicKeysForm(Schema):
    """
    Get list of the public keys of the public key form.
    """

    address = AccountAddressField(required=True)
    node_url = NodeURLField(allow_none=True, required=False)
