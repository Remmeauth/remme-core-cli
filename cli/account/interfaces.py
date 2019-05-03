"""
Provide implementation of the account interfaces.
"""


class AccountInterface:
    """
    Implements account interface.
    """

    def get_balance(self, address):
        """
        Get balance of the account by its address.
        """
        pass

    def transfer_tokens(self, address_to, amount):
        """
        Transfer tokens to address.
        """
        pass
