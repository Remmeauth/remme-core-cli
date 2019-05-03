"""
Provide forms for command line interface's block commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    BlockIdentifierField,
    NodeUrlField,
)


class GetBlockByIdentifierForm(Schema):
    """
    Transfer tokens to address form.
    """

    id = BlockIdentifierField(required=True)
    node_url = NodeUrlField(required=True)
