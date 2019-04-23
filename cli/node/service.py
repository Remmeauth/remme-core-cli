"""
Provide implementation of the node.
"""
import asyncio

from accessify import implements

from cli.node.interfaces import NodeInterface

loop = asyncio.get_event_loop()


@implements(NodeInterface)
class Node:
    """
    Implements account.
    """

    def __init__(self, service):
        """
        Constructor.

        Arguments:
            service: object to interact with Remme core API.
        """
        self.service = service

    def get_configs(self):
        """
        Get node configurations.
        """
        configurations = loop.run_until_complete(self.service.node_management.get_node_config())

        return {
            'configurations': configurations.data,
        }, None
