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
            block_information = loop.run_until_complete(
                self.service.blockchain_info.get_block_by_id(block_id=identifier),
            )

        except RpcGenericServerDefinedError as error:
            return None, error.message

        except Exception as error:
            return None, str(error)

        return block_information.get('data'), None
