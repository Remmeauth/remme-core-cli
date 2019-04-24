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

    async def get(self, address):
        """
        Get information about public key address by public key address.
        """
        return await self.service.public_key_storage.get_info(public_key_address=address)

    def get_list(self, address):
        """
        Get a list of the addresses of the public keys by account address.
        """
        try:
            public_key_addresses = loop.run_until_complete(
                self.service.public_key_storage.get_account_public_keys(address=address),
            )

        except Exception as error:
            return None, str(error)

        return {
                   'public_key_addresses': public_key_addresses,
               }, None
