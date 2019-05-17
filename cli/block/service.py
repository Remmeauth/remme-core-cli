"""
Provide implementation of the block.
"""
import asyncio

from accessify import implements
from aiohttp_json_rpc import RpcGenericServerDefinedError

from cli.block.interfaces import BlockInterface

loop = asyncio.get_event_loop()


@implements(BlockInterface)
class Block:
    """
    Implements block.
    """

    def __init__(self, service):
        """
        Constructor.

        Arguments:
            service: object to interact with Remme core API.
        """
        self.service = service

    def get(self, identifier):
        """
        Get a block by its identifier.
        """
        try:
            block = loop.run_until_complete(
                self.service.blockchain_info.get_block_by_id(block_id=identifier),
            )

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return block.get('data'), None

    def get_list(self, ids, head, limit, reverse):
        """
        Get a list of blocks.

        A list of blocks could be filtered by blocks identifiers, limit, head, reverse.

        Arguments:
            ids (list, optional): identifiers to get a list of blocks by.
            limit (int, optional): maximum amount of blocks to return.
            head (string, optional): block identifier to get a list of transactions to.
            reverse (bool, optional): parameter to reverse result.
        """
        try:
            blocks = loop.run_until_complete(
                self.service.blockchain_info.get_blocks(query={
                    'ids': ids,
                    'limit': limit,
                    'head': head,
                    'reverse': reverse,
                }),
            )

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return blocks.get('data'), None

    def get_list_ids(self, ids, head, limit, reverse):
        """
        Get a list of blocks identifiers.

        A list of blocks identifiers could be filtered by blocks identifiers, limit, head, reverse.

        Arguments:
            ids (list, optional): identifiers to get a list of blocks by.
            limit (int, optional): maximum amount of blocks to return.
            head (string, optional): block identifier to get a list of transactions to.
            reverse (bool, optional): parameter to reverse result.
        """
        blocks, errors = self.get_list(ids=ids, head=head, limit=limit, reverse=reverse)

        if errors is not None:
            return None, errors

        blocks_identifiers = []

        for block in blocks:
            block_identifier = block.get('header_signature')
            blocks_identifiers.append(block_identifier)

        return blocks_identifiers, None
