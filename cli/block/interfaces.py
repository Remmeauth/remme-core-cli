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

    def get_list(self, ids, limit, reverse):
        """
        Get a list of blocks.

        A list of blocks could be filtered by blocks identifiers, limit, reverse.

        Arguments:
            ids (list, optional): identifiers to get a list of blocks by.
            limit (int, optional): maximum amount of blocks to return.
            reverse (string, optional): parameter to reverse result.
        """
        pass
