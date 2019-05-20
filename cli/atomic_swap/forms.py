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
    node_url = NodeUrlField(required=True)


class GetAtomicSwapPublicKeyForm(Schema):
    """
    Get the public key of the atomic swap form.
    """

    node_url = NodeUrlField(required=True)
