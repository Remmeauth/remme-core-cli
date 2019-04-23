"""
Provide forms for command line interface's account commands.
"""
from marshmallow import (
    Schema,
    fields,
)

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeURLField,
    PrivateKeyField,
)


class GetAccountBalanceForm(Schema):
    """
    Get balance of the account form.
    """

    address = AccountAddressField(required=True)
    node_url = NodeURLField(allow_none=True, required=False)


class TransferTokensForm(Schema):
    """
    Transfer tokens to address form.
    """

    private_key = PrivateKeyField(required=True)
    address_to = AccountAddressField(required=True)
    amount = fields.Integer(required=True)
    node_url = NodeURLField(allow_none=True, required=False)
