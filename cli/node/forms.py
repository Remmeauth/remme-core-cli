"""
Provide forms for command line interface's node commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import NodeURLField


class GetNodeConfigurationsForm(Schema):
    """
    Get node configurations.
    """

    node_url = NodeURLField(allow_none=True, required=False)


class GetNodePeersForm(Schema):
    """
    Get the node's peers.
    """

    node_url = NodeURLField(allow_none=True, required=False)


class GetNodeInformationForm(Schema):
    """
    Get node information.
    """

    node_url = NodeURLField(required=False)
