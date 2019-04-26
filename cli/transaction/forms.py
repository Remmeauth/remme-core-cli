"""
Provide forms for command line interface's transaction commands.
"""
from marshmallow import (
    Schema,
    fields,
    validate,
)

from cli.generic.forms.fields import (
    FamilyNameField,
    NodeURLField,
    ReverseField,
    TransactionIdentifierField,
    TransactionIdentifierListField,
)


class GetListTransactionForm(Schema):
    """
    Get list of transactions form.
    """

    ids = TransactionIdentifierListField(allow_none=True, required=False)
    start = TransactionIdentifierField(allow_none=True, required=False)
    head = TransactionIdentifierField(allow_none=True, required=False)
    limit = fields.Integer(
        allow_none=True,
        strict=True,
        required=False,
        validate=[
            validate.Range(min=1, error='Limit must be greater than 0.'),
        ],
    )
    family_name = FamilyNameField(allow_none=True, required=False)
    reverse = ReverseField(allow_none=True, required=False)
    node_url = NodeURLField(allow_none=True, required=False)


class GetSingleTransaction(Schema):
    """
    Get transaction form.
    """

    id = TransactionIdentifierField(allow_none=True, required=False)
    node_url = NodeURLField(allow_none=True, required=False)
