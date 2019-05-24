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

    def transfer_tokens(self, address_to, amount):
        """
        Transfer tokens to address.
        """
        pass

    def transfer_tokens_from_frozen_to_unfrozen(self):
        """
        Transfer available tokens from frozen to unfrozen reputation's balances.
        """
        pass
