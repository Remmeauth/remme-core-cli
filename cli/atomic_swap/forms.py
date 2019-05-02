"""
Provide forms for command line interface's atomic swap commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import (
    NodeURLField,
    SwapIdField,
)


class GetAtomicSwapInformationForm(Schema):
    """
    Get information about atomic swap of the atomic swap form.
    """

    id = SwapIdField(required=True)
    node_url = NodeURLField(allow_none=True, required=False)


class GetAtomicSwapPublicKeyForm(Schema):
    """
    Get public key of the atomic swap form.
    """

    node_url = NodeURLField(allow_none=True, required=False)
