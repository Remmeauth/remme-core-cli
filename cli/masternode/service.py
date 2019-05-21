"""
Provide implementation of the masternode.
"""
import asyncio

from accessify import implements

from cli.masternode.interfaces import MasternodeInterface

loop = asyncio.get_event_loop()


@implements(MasternodeInterface)
class Masternode:
    """
    Implements masternode.
    """

    def __init__(self, service):
        """
        Constructor.

        Arguments:
            service: object to interact with Remme core API.
        """
        self.service = service

    def open(self, amount):
        """
        Open the masternode with starting amount.
        """
        try:
            open_masternode = loop.run_until_complete(
                self.service.node_management.open_master_node(amount=amount),
            )

        except Exception as error:
            return None, str(error)

        return {
            'batch_id': open_masternode.batch_id,
        }, None
