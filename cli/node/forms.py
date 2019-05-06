"""
Provide forms for command line interface's node commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import NodeUrlField


class GetNodeConfigurationsForm(Schema):
    """
    Get node configurations.
    """

    node_url = NodeUrlField(required=False)


class GetNodePeersForm(Schema):
    """
    Get the node's peers.
    """

    node_url = NodeUrlField(required=False)


class GetNodeInformationForm(Schema):
    """
    Get the node information form.
    """

    node_url = NodeUrlField(required=False)
