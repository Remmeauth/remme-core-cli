"""
Provide implementation of the account.
"""
import asyncio

loop = asyncio.get_event_loop()


class Account:
    """
    Implements account.
    """

    def __init__(self, service):
        """
        Constructor.

        Arguments:
            service: object to interact with Remme core API.
        """
        self.service = service

    def get_balance(self, address):
        """
        Get balance of the account by its address.
        """
        return loop.run_until_complete(self.service.token.get_balance(address=address))
