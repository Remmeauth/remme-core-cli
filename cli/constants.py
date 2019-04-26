"""
Provide constants for command line interface.
"""
from remme.models.utils.family_name import RemmeFamilyName

ADDRESS_REGEXP = r'^[0-9a-f]{70}$'
BATCH_ID_REGEXP = r'^[0-9a-f]{128}$'
PRIVATE_KEY_REGEXP = r'^[a-f0-9]{64}$'
TRANSACTION_SIGNATURE_REGEXP = r'^[0-9a-f]{128}$'
DOMAIN_NAME_REGEXP = r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]'

PASSED_EXIT_FROM_COMMAND_CODE = 0
FAILED_EXIT_FROM_COMMAND_CODE = -1
INCORRECT_ENTERED_COMMAND_CODE = 2

NODE_URL_ARGUMENT_HELP_MESSAGE = 'Apply the command to the specified node by its URL.'

CLI_CONFIG_FILE_NAME = 'remme-core-cli'

FAMILY_NAMES = [
    RemmeFamilyName.ACCOUNT.value,
    RemmeFamilyName.NODE_ACCOUNT.value,
    RemmeFamilyName.PUBLIC_KEY.value,
    RemmeFamilyName.SWAP.value,
]

NODE_IP_ADDRESS_FOR_TESTING = '159.89.104.9'
LATEST_RELEASE_NODE_IP_ADDRESS_FOR_TESTING = '165.22.75.163'
RELEASE_0_9_0_ALPHA_NODE_ADDRESS = '165.227.169.119'

PRIVATE_KEY_FOR_TESTING = 'b03e31d2f310305eab249133b53b5fb3270090fc1692c9b022b81c6b9bb6029b'
