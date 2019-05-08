"""
Provide implementation of the batch interfaces.
"""


class BatchInterface:
    """
    Implements batch interface.
    """

    def get(self, id):
        """
        Get a batch by its identifier.

        Arguments:
            id (string, required): batch identifier.
        """
        pass

    def get_status(self, id):
        """
        Get a batch status by its identifier.

        Arguments:
            id (string, required): batch identifier.
        """
        pass
