"""
Provide forms for command line interface's masternode commands.
"""
from marshmallow import (
    Schema,
    fields,
    validate,
)


class OpenMasternodeForm(Schema):
    """
    Open the masternode with starting amount form.
    """

    amount = fields.Integer(
        strict=True,
        required=True,
        validate=[
            validate.Range(min=1, error='Amount must be greater than 0.'),
        ],
    )
