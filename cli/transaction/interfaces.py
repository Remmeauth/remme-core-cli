"""
Provide implementation of the transaction interfaces.
"""


class TransactionInterface:
    """
    Implements transaction interface.
    """

    def get_list(self, ids, start, limit, head, reverse, family_name):
        """
        Get a list of transactions.

        A list of transactions could be filtered by transactions identifiers, start identifier, limit, head identifier,
        reverse, family name.

        Arguments:
            ids (list, optional): identifiers to get a list of transactions by.
            start (string, optional): transaction identifier to get a list transaction starting from.
            limit (int, optional): maximum amount of transactions to return.
            head (string, optional): block identifier to get a list of transactions from.
            reverse (bool, optional): parameter to reverse result.
            family_name (string, optional): list of a transactions by its family name.
        """
        pass

    def get_list_ids(self, ids, start, limit, head, reverse, family_name):
        """
        Get a list of transactions' identifiers.

        A list of transactions' identifiers could be filtered by transactions' identifiers,
        start, limit, head, reverse, family_name.

        Arguments:
            ids (list, optional): identifiers to get a list of blocks by.
            start (string, optional): transaction identifier to get a list transaction starting from.
            limit (int, optional): maximum amount of blocks to return.
            head (string, optional): block identifier to get a list of transactions to.
            reverse (bool, optional): parameter to reverse result.
            family_name (string, optional): list of a transactions by its family name.
        """
        pass

    def get(self, transaction_id):
        """
        Get transaction by its identifier.

        Arguments:
            transaction_id (string, required): transaction identifier.
        """
        pass
