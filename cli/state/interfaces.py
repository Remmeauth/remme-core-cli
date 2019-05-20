"""
Provide implementation of the state interfaces.
"""


class StateInterface:
    """
    Implements state interface.
    """

    def get(self, address):
        """
        Get a state by its address.
        """
        pass

    def get_list(self, address, limit, head, reverse):
        """
        Get a list of states.

        A list of states could be filtered by account address, start address, limit, head identifier, reverse.

        Arguments:
            address (string, optional): account address to get a state by.
            limit (int, optional): maximum amount of states to return.
            head (string, optional): block identifier to get a list of states to.
            reverse (bool, optional): parameter to reverse result.
        """
        pass
