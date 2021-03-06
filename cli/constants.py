"""
Provide constants for command line interface.
"""
from remme.models.general.patterns import RemmePatterns
from remme.models.utils.family_name import RemmeFamilyName

ADDRESS_REGEXP = RemmePatterns.ADDRESS.value
BATCH_IDENTIFIER_REGEXP = RemmePatterns.HEADER_SIGNATURE.value
BLOCK_IDENTIFIER_REGEXP = RemmePatterns.HEADER_SIGNATURE.value
DOMAIN_NAME_REGEXP = r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]'
PRIVATE_KEY_REGEXP = RemmePatterns.PRIVATE_KEY.value
PUBLIC_KEY_ADDRESS_REGEXP = RemmePatterns.ADDRESS.value
PUBLIC_KEY_REGEXP = RemmePatterns.PUBLIC_KEY.value
SWAP_IDENTIFIER_REGEXP = RemmePatterns.SWAP_ID.value
TRANSACTION_IDENTIFIER_REGEXP = RemmePatterns.HEADER_SIGNATURE.value

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

BET_TYPES = ['max', 'min']

DEV_CONSENSUS_GENESIS_NODE_IP_ADDRESS_FOR_TESTING = '142.93.161.195'
DEV_CONSENSUS_GENESIS_NODE_ACCOUNT_ADDRESS = '1168292465adcaffeea284f89330dcc013533c8c285089b75466a958733f4f3fc9174d'
DEV_CONSENSUS_GENESIS_ACCOUNT_ADDRESS = '1120072465adcaffeea284f89330dcc013533c8c285089b75466a958733f4f3fc9174d'

DEV_BRANCH_NODE_IP_ADDRESS_FOR_TESTING = '165.22.90.175'
DEV_BRANCH_NODE_PRIVATE_KEY_WITH_MONEY = 'e07a89fdf89209dbf20c17388673943f0458a3565211cbc0f077386f6f6d21b0'

LINUX_NODE_PRIVATE_KEY_FILE_PATH = '/var/lib/docker/volumes/remme_validator_keys/_data/validator.priv'

SUPPORTED_OS_TO_EXECUTE_NODE_MANAGEMENT_COMMANDS = (
    'Linux'
)
