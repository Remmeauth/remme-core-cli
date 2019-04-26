"""
Provide implementation of the public key interfaces.
"""


class PublicKeyInterface:
    """
    Implements public key interface.
    """

    def get(self, address):
        """
        Get information about public key by its address.
        """
        pass

    def get_list(self, address):
        """
        Get a list of the addresses of the public keys by account address.
        """
        pass
