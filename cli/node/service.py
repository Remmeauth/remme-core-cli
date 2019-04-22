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

    def get_configurations(self):
        """
        Get node configurations.
        """
        # configurations = loop.run_until_complete(self.service.node_management.get_node_config())

        from remme.models.general.methods import RemmeMethods
        configurations = loop.run_until_complete(self.service._remme_api.send_request(method=RemmeMethods.NODE_CONFIG))

        return configurations, None
