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
        Get the node configurations.
        """
        try:
            node_configurations = loop.run_until_complete(self.service.node_management.get_node_config())

        except Exception as error:
            return None, str(error)

        return {
            'configurations': node_configurations.data,
        }, None

    def get_peers(self):
        """
        Get the node's peers.
        """
        try:
            node_peers = loop.run_until_complete(self.service.blockchain_info.get_peers())

        except Exception as error:
            return None, str(error)

        return {
            'peers': node_peers,
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

    def get_initial_stake(self):
        """
        Get the initial stake of the node.
        """
        try:
            node_initial_stake = loop.run_until_complete(self.service.node_management.get_initial_stake())

        except Exception as error:
            return None, str(error)

        return node_initial_stake, None

    def open(self):
        """
        Open the node to participate in the network.
        """
        try:
            open_node = loop.run_until_complete(self.service.node_management.open_node())

        except Exception as error:
            return None, str(error)

        return {
            'batch_id': open_node.batch_id,
        }, None
