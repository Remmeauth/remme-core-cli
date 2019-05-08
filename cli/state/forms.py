"""
Provide forms for command line interface's state commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeUrlField,
)


class GetStateForm(Schema):
    """
    Get a state by its address form.
    """

    address = AccountAddressField(required=True)
    node_url = NodeUrlField(required=False)
