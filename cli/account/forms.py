"""
Provide forms for command line interface's account commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeUrlField,
)


class GetAccountBalanceForm(Schema):
    """
    Get balance of the account form.
    """

    address = AccountAddressField(required=True)
    node_url = NodeUrlField(required=True)
