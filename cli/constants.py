"""
Provide constants for command line interface.
"""
from remme.models.utils.family_name import RemmeFamilyName

ADDRESS_REGEXP = r'^[0-9a-f]{70}$'
BATCH_ID_REGEXP = r'^[0-9a-f]{128}$'
PUBLIC_KEY_REGEXP = r'^[0-9a-f]{66}$'
PRIVATE_KEY_REGEXP = r'^[a-f0-9]{64}$'
PUBLIC_KEY_ADDRESS_REGEXP = r'^[0-9a-f]{70}$'
HEADER_SIGNATURE_REGEXP = r'^[0-9a-f]{128}$'
SWAP_IDENTIFIER_REGEXP = r'^[a-f0-9]{64}$'
TRANSACTION_HEADER_SIGNATURE_REGEXP = r'^[0-9a-f]{128}$'
DOMAIN_NAME_REGEXP = r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]'

PASSED_EXIT_FROM_COMMAND_CODE = 0
FAILED_EXIT_FROM_COMMAND_CODE = -1
INCORRECT_ENTERED_COMMAND_CODE = 2

NODE_URL_ARGUMENT_HELP_MESSAGE = 'Node URL to apply a command to.'

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
NODE_27_IN_TESTNET_ADDRESS = 'node-27-testnet.remme.io'

PRIVATE_KEY_FOR_TESTING = 'b03e31d2f310305eab249133b53b5fb3270090fc1692c9b022b81c6b9bb6029b'

LINUX_NODE_PRIVATE_KEY_FILE_PATH = '/var/lib/docker/volumes/remme_validator_keys/_data/validator.priv'

SUPPORTED_OS_TO_EXECUTE_NODE_MANAGEMENT_COMMANDS = (
    'Linux'
)
