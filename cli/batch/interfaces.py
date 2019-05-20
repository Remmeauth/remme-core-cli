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

    def get_list(self, ids, start, limit, head, reverse):
        """
        Get a list of batches.

        A list of batches could be filtered by batch identifiers, start identifier, limit, head identifier,
        reverse.

        Arguments:
            ids (list, optional): identifiers to get a list of batches by.
            start (string, optional): batch identifier to get a list of batches starting from.
            limit (int, optional): maximum amount of batches to return.
            head (string, optional): block identifier to get a list of batches from.
            reverse (bool, optional): parameter to reverse result.
        """
        pass

    def get_list_ids(self, ids, start, limit, head, reverse):
        """
        Get a list of batches' identifiers.

        A list of batch identifiers could be filtered by batch identifiers, start identifier, limit, head identifier,
        reverse.

        Arguments:
            ids (list, optional): identifiers to get a list of batches by.
            start (string, optional): batch identifier to get a list of batches starting from.
            limit (int, optional): maximum amount of batches to return.
            head (string, optional): block identifier to get a list of batches from.
            reverse (bool, optional): parameter to reverse result.
        """
        pass
