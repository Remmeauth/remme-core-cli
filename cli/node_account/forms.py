"""
Provide forms for command line interface's node account commands.
"""
from marshmallow import (
    Schema,
    fields,
    validate,
)

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeUrlField,
)


class GetNodeAccountInformationForm(Schema):
    """
    Get information about the node account by its address form.
    """

    address = AccountAddressField(required=True)
    node_url = NodeUrlField(required=True)


class TransferTokensFromUnfrozenToOperationalForm(Schema):
    """
    A transfer of tokens from unfrozen reputational balance to operational balance form.
    """

    amount = fields.Integer(
        strict=True,
        required=True,
        validate=[
            validate.Range(min=1, error='Amount must be greater than 0.'),
        ],
    )
