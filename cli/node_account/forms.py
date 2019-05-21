"""
Provide forms for command line interface's node account commands.
"""
from marshmallow import (
    Schema,
    fields,
)

from cli.generic.forms.fields import (
    AccountAddressField,
    NodeUrlField,
)


class GetNodeAccountInformationForm(Schema):
    """
    Get information about the node account by its address form.
    """

    address = AccountAddressField(required=True)
    node_url = NodeUrlField(required=True)


class SetBetNodeAccountForm(Schema):
    """
    Set masternode betting behaviour form.
    """

    bet = fields.String(required=True)
