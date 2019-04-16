"""
Provide implementation of the public key interfaces.
"""


class PublicKeyInterface:
    """
    Implements public key interface.
    """

    async def get_account_public_keys(self, address):
        """
        Get account public keys by account address.
        """
        pass

    async def get(self, address):
        """
        Get public key by account address.
        """
        pass
