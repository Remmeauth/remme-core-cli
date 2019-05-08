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

    def get(self, id):
        """
        Get a batch by its identifier.

        Arguments:
            id (string, required): batch identifier.
        """
        try:
            batch = loop.run_until_complete(
                self.service.blockchain_info.get_batch_by_id(batch_id=id),
            )

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return batch.get('data'), None