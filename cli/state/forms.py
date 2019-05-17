"""
Provide forms for command line interface's state commands.
"""
from marshmallow import (
    Schema,
    fields,
    validate,
)

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeUrlField,
    StateIdentifierField,
)


class GetStateForm(Schema):
    """
    Get a state by its address form.
    """

    address = AccountAddressField(required=True)
    node_url = NodeUrlField(required=False)


class GetStateListForm(Schema):
    """
    Get a list of states form.
    """

    address = AccountAddressField(allow_none=True, required=False)
    head = StateIdentifierField(allow_none=True, required=False)
    limit = fields.Integer(
        allow_none=True,
        strict=True,
        required=False,
        validate=[
            validate.Range(min=1, error='Limit must be greater than 0.'),
        ],
    )
    node_url = NodeUrlField(required=False)
