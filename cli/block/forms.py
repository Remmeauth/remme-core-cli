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
    Get a list of blocks form.
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
    head = BlockIdentifierField(allow_none=True, required=False)
    reverse = fields.Boolean(required=False)
    ids_only = fields.Boolean(required=False)
    node_url = NodeUrlField(required=True)


class GetBlockByIdentifierForm(Schema):
    """
    Get a block by its identifier form.
    """

    id = BlockIdentifierField(required=True)
    node_url = NodeUrlField(required=True)
