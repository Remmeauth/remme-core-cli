"""
Provide implementation of the node account interfaces.
"""


class NodeAccountInterface:
    """
    Implements node account interface.
    """

    def get(self, address):
        """
        Get information about the node account by its address.

        Arguments:
            address (str, required): node account address to get information about node account by.
        """
        pass

    def set_bet(self, bet):
        """
        Set masternode betting behaviour.

        Arguments:
            bet (string or integer, required): bet type (can be `MIN`, `MAX`, integer).
        """
        pass
