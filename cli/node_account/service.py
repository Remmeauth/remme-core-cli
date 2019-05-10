"""
Provide implementation of the node account.
"""
import asyncio

from accessify import implements
from aiohttp_json_rpc import RpcGenericServerDefinedError

from cli.node_account.interfaces import NodeAccountInterface

loop = asyncio.get_event_loop()


@implements(NodeAccountInterface)
class NodeAccount:
    """
    Implements node account.
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
        Get information about the node account by its address.

        Arguments:
            address (str, required): node account address to get information about node account by.
        """
        try:
            node_account_information = loop.run_until_complete(
                self.service.node_management.get_node_account(node_account_address=address),
            )

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return node_account_information.node_account_response, None
