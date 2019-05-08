"""
Provide implementation of the batch.
"""
import asyncio

from accessify import implements
from aiohttp_json_rpc import RpcGenericServerDefinedError

from cli.batch.interfaces import BatchInterface

loop = asyncio.get_event_loop()


@implements(BatchInterface)
class Batch:
    """
    Implements batch.
    """

    def __init__(self, service):
        """
        Constructor.

        Arguments:
            service: object to interact with Remme core API.
        """
        self.service = service

    def get_list(self, batch_ids, start, limit, head, reverse):
        """
        Get a list of batches.

        Arguments:
            batch_ids (list, optional): identifiers to get a list of batches by.
            start (string, optional): batch identifier to get a list of batches starting from.
            limit (int, optional): maximum amount of batches to return.
            head (string, optional): block identifier to get a list of batches from.
            reverse (string, optional): parameter to reverse result.
        """
        reverse = '' if reverse else 'false'

        try:
            batches = loop.run_until_complete(
                self.service.blockchain_info.get_batches(query={
                    'ids': batch_ids,
                    'start': start,
                    'limit': limit,
                    'head': head,
                    'reverse': reverse,
                }),
            )

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return batches, None
