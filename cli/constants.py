"""
Provide constants for command line interface.
"""
ADDRESS_REGEXP = '^[0-9a-f]{70}$'
HEADER_SIGNATURE_REGEXP = '^[0-9a-f]{128}$'
DOMAIN_NAME_REGEXP = r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]'

PASSED_EXIT_FROM_COMMAND_CODE = 0
FAILED_EXIT_FROM_COMMAND_CODE = -1

NODE_URL_ARGUMENT_HELP_MESSAGE = 'Apply the command to the specified node by its URL.'

CLI_CONFIG_FILE_NAME = 'remme-core-cli'

FAMILY_NAMES = ['account', 'node_account', 'pub_key', 'AtomicSwap']

NODE_IP_ADDRESS_FOR_TESTING = '159.89.104.9'
