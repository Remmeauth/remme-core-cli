"""
Provide implementation of the receipt.
"""
import asyncio

from accessify import implements
from aiohttp_json_rpc import RpcGenericServerDefinedError

from cli.receipt.interfaces import ReceiptInterface

loop = asyncio.get_event_loop()


@implements(ReceiptInterface)
class Receipt:
    """
    Implements receipt.
    """

    def __init__(self, service):
        """
        Constructor.

        Arguments:
            service: object to interact with Remme core API.
        """
        self.service = service

    def get(self, identifiers):
        """
        Get a list of the transaction's receipts by identifiers.
        """
        try:
            receipts = loop.run_until_complete(self.service.blockchain_info.get_receipts(ids=identifiers))

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return receipts, None
