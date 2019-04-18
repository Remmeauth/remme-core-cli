"""
Provide implementation of the transaction.
"""
from accessify import implements

from cli.transaction.interfaces import TransactionInterfaces


@implements(TransactionInterfaces)
class Transaction:
    """
    Implements transaction.
    """

    def __init__(self, service):
        """
        Constructor.

        Arguments:
            service: object to interact with Remme core API.
        """
        self.service = service

    async def get_list(self, query):
        """
        Get list transaction by: ids, start, head, limit, reverse.
        """
        return await self.service.blockchain_info.get_transactions(query=query)

    async def get(self, transaction_id):
        """
        Fetch transaction by its id.
        """
        return await self.service.blockchain_info.get_transaction_by_id(transaction_id=transaction_id)
