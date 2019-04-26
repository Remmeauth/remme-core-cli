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

        Arguments:
            query (dict, optional): dictionary with specific parameters.
        """
        pass

    async def get(self, transaction_id):
        """
        Get transaction by its identifier.

        Arguments:
            transaction_id (string, required): transaction id
        """
        pass
