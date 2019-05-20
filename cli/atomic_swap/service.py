"""
Provide implementation of the atomic swap.
"""
import asyncio

from accessify import implements
from aiohttp_json_rpc import RpcGenericServerDefinedError

from cli.atomic_swap.interfaces import AtomicSwapInterface

loop = asyncio.get_event_loop()


@implements(AtomicSwapInterface)
class AtomicSwap:
    """
    Implements atomic swap.
    """

    def __init__(self, service):
        """
        Constructor.

        Arguments:
            service: object to interact with Remme core API.
        """
        self.service = service

    def get_public_key(self):
        """
        Get the public key of atomic swap.
        """
        try:
            public_key = loop.run_until_complete(self.service.swap.get_public_key())

        except Exception as error:
            return None, str(error)

        return {
            'public_key': public_key,
        }, None

    def get(self, swap_id):
        """
        Get information about atomic swap by its identifier.
        """
        try:
            swap_info = loop.run_until_complete(self.service.swap.get_info(swap_id=swap_id))

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return {
            'information': swap_info.data,
        }, None
