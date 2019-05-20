"""
Provide implementation of the block interfaces.
"""


class BlockInterface:
    """
    Implements block interface.
    """

    def get(self, identifier):
        """
        Get a block by its identifier.
        """
        pass

    def get_list(self, ids, head, limit, reverse):
        """
        Get a list of blocks.

        A list of blocks could be filtered by blocks identifiers, limit, head, reverse.

        Arguments:
            ids (list, optional): identifiers to get a list of blocks by.
            limit (int, optional): maximum amount of blocks to return.
            head (string, optional): block identifier to get a list of transactions to.
            reverse (bool, optional): parameter to reverse result.
        """
        pass

    def get_list_ids(self, ids, head, limit, reverse):
        """
        Get a list of blocks identifiers.

        A list of blocks identifiers could be filtered by blocks identifiers, limit, head, reverse.

        Arguments:
            ids (list, optional): identifiers to get a list of blocks by.
            limit (int, optional): maximum amount of blocks to return.
            head (string, optional): block identifier to get a list of transactions to.
            reverse (bool, optional): parameter to reverse result.
        """
        pass
