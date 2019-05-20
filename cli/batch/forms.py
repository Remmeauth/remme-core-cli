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


class GetBatchForm(Schema):
    """
    Get a batch by its identifier form.
    """

    id = BatchIdentifierField(required=True)
    node_url = NodeUrlField(required=True)


class GetBatchStatusForm(Schema):
    """
    Get a batch status by its identifier form.
    """

    id = BatchIdentifierField(required=True)
    node_url = NodeUrlField(required=True)


class GetBatchesListForm(Schema):
    """
    Get a list of batches form.
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
    reverse = fields.Boolean(required=False)
    ids_only = fields.Boolean(required=False)
    node_url = NodeUrlField(required=True)
