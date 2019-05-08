"""
Provide forms for command line interface's batch commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    BatchIdentifierField,
    NodeUrlField,
)


class GetBatchForm(Schema):
    """
    Get a batch by its identifier form.
    """

    id = BatchIdentifierField(allow_none=False, required=True)
    node_url = NodeUrlField(required=False)
