"""
Provide implementation of the public key.
"""
import asyncio

from accessify import implements

from cli.public_key.interfaces import PublicKeyInterface

loop = asyncio.get_event_loop()


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

    async def get_info(self, address):
        """
        Get information about public key by public key address.
        """
        public_key_info = loop.run_until_complete(self.service.public_key_storage.get_info(public_key_address=address))

        return {
            'result': public_key_info,
        }, None
