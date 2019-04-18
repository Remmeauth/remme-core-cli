"""
Provide implementation of the atomic swap.
"""
from accessify import implements

from cli.atomic_swap.interfaces import AtomicSwapInterface


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

    async def get(self):
        """
        Get public key of atomic swap.
        """
        return await self.service.swap.get_public_key()
