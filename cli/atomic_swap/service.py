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

    async def get_info(self, swap_id):
        """
        Get information about atomic swap by swap identifier.
        """
        return await self.service.swap.get_info(swap_id=swap_id)
