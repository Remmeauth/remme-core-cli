"""
Provide forms for command line interface's node account commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeUrlField,
)


class GetNodeAccountInformationForm(Schema):
    """
    Get the node account information.
    """

    address = AccountAddressField(required=True)
    node_url = NodeUrlField(required=False)
