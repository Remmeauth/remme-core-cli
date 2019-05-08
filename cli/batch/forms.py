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
    Get a batch status by its identifier form.
    """

    id = BatchIdentifierField(required=True)
    node_url = NodeUrlField(required=False)
