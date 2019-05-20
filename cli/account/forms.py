"""
Provide forms for command line interface's account commands.
"""
from marshmallow import (
    Schema,
    fields,
    validate,
)

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeUrlField,
    PrivateKeyField,
)


class GetAccountBalanceForm(Schema):
    """
    Get balance of the account form.
    """

    address = AccountAddressField(required=True)
    node_url = NodeUrlField(required=True)


class TransferTokensForm(Schema):
    """
    Transfer tokens to address form.
    """

    private_key = PrivateKeyField(required=True)
    address_to = AccountAddressField(required=True)
    amount = fields.Integer(
        strict=True,
        required=True,
        validate=[
            validate.Range(min=1, error='Amount must be greater than 0.'),
        ],
    )
    node_url = NodeUrlField(required=True)
