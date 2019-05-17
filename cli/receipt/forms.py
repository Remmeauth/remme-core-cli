"""
Provide forms for command line interface's receipt commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    NodeUrlField,
    TransactionIdentifiersListField,
)


class GetReceiptsForm(Schema):
    """
    Get a list of the transaction's receipts by identifiers form.
    """

    ids = TransactionIdentifiersListField(required=True)
    node_url = NodeUrlField(required=True)
