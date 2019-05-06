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
    Implements node.
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
        try:
            configurations = loop.run_until_complete(self.service.node_management.get_node_config())

        except Exception as error:
            return None, str(error)

        return {
            'configurations': configurations.data,
        }, None

    def get_peers(self):
        """
        Get the node's peers.
        """
        try:
            peers = loop.run_until_complete(self.service.blockchain_info.get_peers())

        except Exception as error:
            return None, str(error)

        return {
            'peers': peers,
        }, None

    def get_info(self):
        """
        Get information about synchronization and peer count of the node form.
        """
        try:
            node_information = loop.run_until_complete(self.service.node_management.get_node_info())

        except Exception as error:
            return None, str(error)

        return {
            'information': node_information.data,
        }, None
