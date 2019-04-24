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

    def get_list(self, address):
        """
        Get list of the public keys by account address.
        """
        public_keys = loop.run_until_complete(self.service.public_key_storage.get_account_public_keys(address=address))

        return {
            'public_keys': public_keys,
        }, None
