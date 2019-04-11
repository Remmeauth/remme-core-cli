"""
Provide implementation of the blockchain info interfaces.
"""


class TransactionInterfaces:
    """
    Implements transaction interface.
    """

    async def list_transactions(self, query):
        """
        Get list transactions by: ids, start, head, limit, reverse.

        Arguments:
            query (dict, optional): dictionary with specific parameters
        Returns:
            List of transactions.
        """
        pass

    async def single_transaction(self, transaction_id):
        """
        Get transactions by its id.

        Arguments:
            transaction_id (string, required): transaction id
        Returns:
            Transaction.
        """
        pass
