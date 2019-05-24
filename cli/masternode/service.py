"""
Provide implementation of the masternode.
"""
import asyncio

from accessify import implements

from cli.errors import NotSupportedBetError
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

    def close(self):
        """
        Close the masternode.
        """
        try:
            close_masternode = loop.run_until_complete(
                self.service.node_management.close_master_node(),
            )

        except Exception as error:
            return None, str(error)

        return {
            'batch_id': close_masternode.batch_id,
        }, None

    def set_bet(self, bet):
        """
        Set the masternode betting behavior.

        Arguments:
            bet (string or integer, required): type of bet to set to the masternode account. Valid bet is
                                               `min` or `max` as strings, or an integer value (e.g. 20).
        """
        if isinstance(bet, str):
            bet = bet.upper()

        if isinstance(bet, int):
            if bet == 0:
                raise NotSupportedBetError(
                    f'The following bet `{bet}` is not supported, the minimum bet is integer 1.',
                )

        try:
            masternode_bet = loop.run_until_complete(
                self.service.node_management.set_bet(bet_type=bet),
            )

        except Exception as error:
            return None, str(error)

        return {
            'batch_id': masternode_bet.batch_id,
        }, None
