"""
Provide forms for command line interface's masternode commands.
"""
from marshmallow import (
    Schema,
    fields,
    validate,
)

from cli.generic.forms.fields import BetField


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


class SetBetMasternodeForm(Schema):
    """
    Set the masternode betting behavior form.
    """

    bet = BetField(required=True)
