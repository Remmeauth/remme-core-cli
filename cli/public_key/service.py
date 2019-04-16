"""
Provide implementation of the public key.
"""
from accessify import implements

from cli.public_key.interfaces import PublicKeyInterface


@implements(PublicKeyInterface)
class PublicKey:
    """
    Implements public key.
    """

    def __init__(self, service):
        """
        Constructor.

        Arguments:
            service: object to interact with Remme core API.
        """
        self.service = service

    async def get_account_public_keys(self, address):
        """
        Get account public keys by account address.
        """
        return await self.service.public_key_storage.get_account_public_keys(address=address)

    async def get(self, address):
        """
        Get public key by account address.
        """
        return await self.service.public_key_storage.get_info(address=address)
