"""
Provide forms for command line interface's node commands.
"""
from marshmallow import Schema

from cli.generic.forms.fields import NodeUrlField


class GetNodeConfigurationsForm(Schema):
    """
    Get the node configurations form.
    """

    node_url = NodeUrlField(required=True)


class GetNodePeersForm(Schema):
    """
    Get the node's peers form.
    """

    node_url = NodeUrlField(required=True)


class GetNodeInformationForm(Schema):
    """
    Get the node information form.
    """

    node_url = NodeUrlField(required=True)


class GetNodeInitialStakeForm(Schema):
    """
    Get the initial stake of the node form.
    """

    node_url = NodeUrlField(required=True)
