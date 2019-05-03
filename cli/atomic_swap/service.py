"""
Provide implementation of the atomic swap.
"""
import asyncio

from accessify import implements

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
        Get public key of atomic swap.
        """
        try:
            public_key = loop.run_until_complete(self.service.swap.get_public_key())

        except Exception as error:
            return None, str(error)

        return {
            'public_key': public_key,
        }, None
