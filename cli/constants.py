"""
Provide constants for command line interface.
"""
ADDRESS_REGEXP = '^[0-9a-f]{70}$'
HEADER_SIGNATURE_REGEXP = '^[0-9a-f]{128}$'

FAILED_EXIT_FROM_COMMAND = -1

NODE_URL_ARGUMENT_HELP_MESSAGE = 'Apply the command to the specified node by its URL.'

CLI_CONFIG_FILE_NAME = 'remme-core-cli'

FAMILY_NAMES = ['account', 'node_account', 'pub_key', 'AtomicSwap']
