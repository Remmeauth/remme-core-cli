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

    async def get(self, address):
        """
        Get information about public key by public key address.
        """
        return await self.service.public_key_storage.get_info(public_key_address=address)
