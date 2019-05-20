"""
Provide forms for command line interface's public key commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeUrlField,
    PublicKeyAddressField,
)


class GetPublicKeyInformationForm(Schema):
    """
    Get information about public key of the public key information form.
    """

    address = PublicKeyAddressField(required=True)
    node_url = NodeUrlField(required=True)


class GetPublicKeysForm(Schema):
    """
    Get a list of the addresses of the public keys form.
    """

    address = AccountAddressField(required=True)
    node_url = NodeUrlField(required=True)
