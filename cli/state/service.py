"""
Provide implementation of the state.
"""
import asyncio

from accessify import implements
from aiohttp_json_rpc import RpcGenericServerDefinedError

from cli.state.interfaces import StateInterface

loop = asyncio.get_event_loop()


@implements(StateInterface)
class State:
    """
    Implements state.
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
        Get a state by its address.
        """
        try:
            state = loop.run_until_complete(
                self.service.blockchain_info.get_state_by_address(address=address),
            )

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return {
            'state': state,
        }, None
