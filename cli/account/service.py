"""
Provide implementation of the account.
"""
import asyncio

from accessify import implements

from cli.account.interfaces import AccountInterface

loop = asyncio.get_event_loop()


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

    def get_balance(self, address):
        """
        Get balance of the account by its address.
        """
        try:
            balance = loop.run_until_complete(self.service.token.get_balance(address=address))

        except Exception as error:
            return None, str(error)

        return {
            'balance': balance,
        }, None

    def transfer_tokens(self, address_to, amount):
        """
        Transfer tokens to address.
        """
        try:
            transaction = loop.run_until_complete(self.service.token.transfer(address_to=address_to, amount=amount))

        except Exception as error:
            return None, str(error)

        return {
            'batch_identifier': transaction.batch_id,
        }, None
