"""
Provide forms for command line interface's batch commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    BatchIdentifierField,
    NodeUrlField,
)


class GetBatchStatusForm(Schema):
    """
    Get batch status form.
    """

    id = BatchIdentifierField(allow_none=True, required=True)
    node_url = NodeUrlField(required=False)
