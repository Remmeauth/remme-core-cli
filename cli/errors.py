"""
Provide errors for command line interface.
"""


class NotSupportedOsToGetNodePrivateKeyError(Exception):
    """
    Operating system is not supported to get the node's private key error.
    """

    def __init__(self, message):
        self.message = message
