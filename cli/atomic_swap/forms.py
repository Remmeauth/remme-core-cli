"""
Provide forms for command line interface's atomic swap commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    NodeUrlField,
    SwapIdentifierField,
)


class GetAtomicSwapInformationForm(Schema):
    """
    Get information about atomic swap by its identifier form.
    """

    id = SwapIdentifierField(required=True)
    node_url = NodeUrlField(required=False)


class GetAtomicSwapPublicKeyForm(Schema):
    """
    Get public key of the atomic swap form.
    """

    node_url = NodeUrlField(required=False)
