"""
Provide implementation of the atomic swap interfaces.
"""


class AtomicSwapInterface:
    """
    Implements atomic swap interface.
    """

    def get_public_key(self):
        """
        Get the public key of atomic swap.
        """
        pass

    def get(self, swap_id):
        """
        Get information about atomic swap by its identifier.
        """
        pass
