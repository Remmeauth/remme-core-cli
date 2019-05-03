"""
Provide implementation of the transaction.
"""
import asyncio

from accessify import implements
from aiohttp_json_rpc import RpcGenericServerDefinedError

from cli.transaction.interfaces import TransactionInterface

loop = asyncio.get_event_loop()


@implements(TransactionInterface)
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

    def get_list(self, transaction_ids, start, limit, head, reverse, family_name):
        """
        Get a list of transactions.

        Arguments:
            transaction_ids (list, optional): identifiers to get a list of transactions by.
            start (string, optional): transaction identifier to get a list transaction starting from.
            limit (int, optional): maximum amount of transactions to return.
            head (string, optional): block identifier to get a list of transactions from.
            reverse (string, optional): parameter to reverse result.
            family_name (string, optional): list of a transactions by its family name.
        """
        reverse = '' if reverse else 'false'

        try:
            transactions = loop.run_until_complete(
                self.service.blockchain_info.get_transactions(query={
                    'ids': transaction_ids,
                    'start': start,
                    'limit': limit,
                    'head': head,
                    'family_name': family_name,
                    'reverse': reverse,
                }),
            )

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return transactions, None

    def get(self, transaction_id):
        """
        Get a transaction.

        Arguments:
            transaction_id (string, required): transaction identifier.
        """
        try:
            transaction = loop.run_until_complete(
                self.service.blockchain_info.get_transaction_by_id(transaction_id=transaction_id),
            )

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return transaction, None
