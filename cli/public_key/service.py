"""
Provide implementation of the public key.
"""
import asyncio

from accessify import implements
from aiohttp_json_rpc import RpcGenericServerDefinedError

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

    def get(self, address):
        """
        Get information about public key by its address.
        """
        try:
            public_key_info = loop.run_until_complete(
                self.service.public_key_storage.get_info(public_key_address=address),
            )

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return {
            'information': public_key_info.data,
        }, None

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
            'addresses': public_key_addresses,
        }, None
