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

    def set_bet(self, bet):
        """
        Set the masternode betting behaviour.

        Arguments:
            bet (string or integer, required): type of bet to set to the masternode account. Valid bet is
            `min` or `max` as strings, or an integer value (e.g. 15000).
        """
        if isinstance(bet, str):
            bet = bet.upper()

        try:
            masternode_bet = loop.run_until_complete(self.service.node_management.set_bet(bet_type=bet))

        except Exception as error:
            return None, str(error)

        return {
            'batch_id': masternode_bet.batch_id,
        }, None
