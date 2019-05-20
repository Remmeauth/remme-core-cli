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

    def get_list(self, address, start, limit, head, reverse):
        """
        Get a list of states.

        A list of states could be filtered by account address, start address, limit, head identifier, reverse.

        Arguments:
            address (string, optional): account address to get a state by.
            start (string, optional): account address to get a list of states starting from.
            limit (int, optional): maximum amount of states to return.
            head (string, optional): block identifier to get a list of states to.
            reverse (bool, optional): parameter to reverse result.
        """
        try:
            states = loop.run_until_complete(
                self.service.blockchain_info.get_states(query={
                    'address': address,
                    'start': start,
                    'limit': limit,
                    'head': head,
                    'reverse': reverse,
                }),
            )

        except RpcGenericServerDefinedError as error:
            return None, str(error.message)

        except Exception as error:
            return None, str(error)

        return states.get('data'), None
