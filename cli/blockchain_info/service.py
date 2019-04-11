"""
Provide implementation of the blockchain info.
"""
from accessify import implements

from cli.blockchain_info.interfaces import TransactionInterfaces


@implements(TransactionInterfaces)
class Transactions:
    """
    Implements transaction info.
    """

    def __init__(self, service):
        """
        Constructor.
        Arguments:
            service: object to interact with Remme core API.
        """
        self.service = service

    async def list_transactions(self, query):
        """
        Get list transactions by: ids, start, head, limit, reverse.
        """
        return await self.service.blockchain_info.get_transactions(query=query)

    async def single_transaction(self, transaction_id):
        """
        Fetch transaction by its id.
        """
        return await self.service.blockchain_info.get_transaction_by_id(transaction_id=transaction_id)
