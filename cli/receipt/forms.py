"""
Provide forms for command line interface's node commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    NodeUrlField,
    TransactionIdentifiersListField,
)


class GetReceiptsForm(Schema):
    """
    Get list of the transaction receipts by identifiers form.
    """

    ids = TransactionIdentifiersListField(required=True)
    node_url = NodeUrlField(required=True)
