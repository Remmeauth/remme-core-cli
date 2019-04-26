"""
Provide implementation of the transaction interfaces.
"""


class TransactionInterface:
    """
    Implements transaction interface.
    """

    def get_list(self, transaction_ids, start, limit, head, reverse, family_name):
        """
        Get a list of transactions.

         The following filters could be applied:
            transaction identifiers: identifiers to get a list of transactions by.
            start: transaction identifier to get a list transaction starting from.
            limit: maximum amount of transactions to return.
            head: block identifier to get a list of transactions from.
            reverse: parameter to reverse result.
            family-name: list of a transactions by its family name.

        Arguments:
            transaction_ids (list, optional): transaction identifiers
            start (string, optional): start
            limit (int, optional): limit
            head (string, optional): head
            reverse (string, optional): reverse
            family_name (string, optional): family name
        """
        pass

    def get(self, transaction_id):
        """
        Get transaction by its identifier.

        Arguments:
            transaction_id (string, required): transaction identifier
        """
        pass
