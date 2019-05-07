"""
Provide forms for command line interface's block commands.
"""
from marshmallow import (
    Schema,
    fields,
    validate,
)

from cli.generic.forms.fields import (
    BlockIdentifierField,
    BlockIdentifiersListField,
    NodeUrlField,
)


class GetBlocksListForm(Schema):
    """
    Get a list of transactions form.
    """

    ids = BlockIdentifiersListField(allow_none=True, required=False)
    limit = fields.Integer(
        allow_none=True,
        strict=True,
        required=False,
        validate=[
            validate.Range(min=1, error='Limit must be greater than 0.'),
        ],
    )
    node_url = NodeUrlField(required=False)


class GetBlockByIdentifierForm(Schema):
    """
    Transfer tokens to address form.
    """

    id = BlockIdentifierField(required=True)
    node_url = NodeUrlField(required=True)
