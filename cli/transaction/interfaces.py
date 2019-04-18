"""
Provide implementation of the transaction interfaces.
"""


class TransactionInterfaces:
    """
    Implements transaction interface.
    """

    async def get_list(self, query):
        """
        Get list transaction by: ids, start, head, limit, reverse.

        Arguments:
            query (dict, optional): dictionary with specific parameters

        Returns:
            List of transaction.
        """
        pass

    async def get(self, transaction_id):
        """
        Get transaction by its id.

        Arguments:
            transaction_id (string, required): transaction id

        Returns:
            Transaction.
        """
        pass
