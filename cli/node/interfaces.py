"""
Provide implementation of the node interfaces.
"""


class NodeInterface:
    """
    Implements node interface.
    """

    def get_configs(self):
        """
        Get the node configurations.
        """
        pass

    def get_peers(self):
        """
        Get the node's peers.
        """
        pass

    def get_info(self):
        """
        Get information about synchronization and peer count of the node.
        """
        pass

    def get_initial_stake(self):
        """
        Get the initial stake of the node.
        """
        pass
