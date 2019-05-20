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

    def get_status(self, id):
        """
        Get a batch status by its identifier.

        Arguments:
            id (string, required): batch identifier.
        """
        try:
            batch_status = loop.run_until_complete(self.service.blockchain_info.get_batch_status(batch_id=id))

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return batch_status, None

    def get_list(self, ids, start, limit, head, reverse):
        """
        Get a list of batches.

        Arguments:
            ids (list, optional): identifiers to get a list of batches by.
            start (string, optional): batch identifier to get a list of batches starting from.
            limit (int, optional): maximum amount of batches to return.
            head (string, optional): block identifier to get a list of batches from.
            reverse (bool, optional): parameter to reverse result.
        """
        try:
            batches = loop.run_until_complete(
                self.service.blockchain_info.get_batches(query={
                    'ids': ids,
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

        return batches.get('data'), None

    def get_list_ids(self, ids, start, limit, head, reverse):
        """
        Get a list of batches' identifiers.

        Arguments:
            ids (list, optional): identifiers to get a list of batches by.
            start (string, optional): batch identifier to get a list of batches starting from.
            limit (int, optional): maximum amount of batches to return.
            head (string, optional): block identifier to get a list of batches from.
            reverse (bool, optional): parameter to reverse result.
        """
        batches, errors = self.get_list(ids=ids, start=start, head=head, limit=limit, reverse=reverse)

        if errors is not None:
            return None, errors

        batch_identifiers = []

        for batch in batches:
            batch_identifier = batch.get('header_signature')
            batch_identifiers.append(batch_identifier)

        return batch_identifiers, None
