"""
Provide implementation of the account.
"""
from accessify import implements

from cli.account.interfaces import AccountInterface


@implements(AccountInterface)
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

    async def get_balance(self, address):
        """
        Get balance of the account by its address.
        """
        return await self.service.token.get_balance(address=address)
