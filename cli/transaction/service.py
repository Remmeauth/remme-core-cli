"""
Provide implementation of the transaction.
"""
import asyncio

from accessify import implements
from aiohttp_json_rpc import RpcGenericServerDefinedError

from cli.transaction.interfaces import TransactionInterfaces

loop = asyncio.get_event_loop()


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

    def get_list(self, query):
        """
        Get a list of transactions by: ids, start, head, limit, reverse.
        """
        try:
            transaction_list = loop.run_until_complete(
                self.service.blockchain_info.get_transactions(query=query),
            )

            return transaction_list, None

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

    def get(self, transaction_id):
        """
        Fetch transaction by its id.
        """
        try:
            single_transaction = loop.run_until_complete(
                self.service.blockchain_info.get_transaction_by_id(transaction_id=transaction_id),
            )

            return single_transaction, None

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)
