"""
Provide implementation of the transaction interfaces.
"""


class TransactionInterfaces:
    """
    Implements transaction interface.
    """

    async def get_list(self, query):
        """
        Get a list of transactions.

        List of transactions can be filtered by identifiers, start pagging, identifier of block's head, limit
        of transactions, reversed result, family-name of transactions

        Arguments:
            query (dict, optional): dictionary with specific parameters
        """
        pass

    async def get(self, transaction_id):
        """
        Get transaction by its identifier.

        Arguments:
            transaction_id (string, required): transaction id
        """
        pass
