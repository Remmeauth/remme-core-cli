"""
Provide forms for command line interface's batch commands.
"""
from marshmallow import (
    Schema,
    fields,
    validate,
)

from cli.generic.forms.fields import (
    BatchIdentifierField,
    BatchIdentifiersListField,
    NodeUrlField,
)


class GetBatchesListForm(Schema):
    """
    Get a list of batch form.
    """

    ids = BatchIdentifiersListField(allow_none=True, required=False)
    start = BatchIdentifierField(allow_none=True, required=False)
    head = BatchIdentifierField(allow_none=True, required=False)
    limit = fields.Integer(
        allow_none=True,
        strict=True,
        required=False,
        validate=[
            validate.Range(min=1, error='Limit must be greater than 0.'),
        ],
    )
    node_url = NodeUrlField(required=False)
