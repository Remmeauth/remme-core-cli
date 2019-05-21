"""
Provide implementation of the masternode interfaces.
"""


class MasternodeInterface:
    """
    Implements masternode interface.
    """

    def open(self, amount):
        """
        Open the masternode with starting amount.
        """
        pass

    def set_bet(self, bet):
        """
        Set masternode betting behaviour.

        Arguments:
            bet (string or integer, required): type of bet to set to the masternode account.
        """
        pass
