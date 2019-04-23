"""
Provide constants for command line interface.
"""
ADDRESS_REGEXP = r'^[0-9a-f]{70}$'
HEADER_SIGNATURE_REGEXP = r'^[0-9a-f]{128}$'
PUBLIC_KEY_REGEXP = r'^[0-9a-f]{66}$'
DOMAIN_NAME_REGEXP = r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]'

PASSED_EXIT_FROM_COMMAND_CODE = 0
FAILED_EXIT_FROM_COMMAND_CODE = -1

NODE_URL_ARGUMENT_HELP_MESSAGE = 'Node URL to apply a command to.'

CLI_CONFIG_FILE_NAME = 'remme-core-cli'

NODE_IP_ADDRESS_FOR_TESTING = '159.89.104.9'
LATEST_RELEASE_NODE_IP_ADDRESS_FOR_TESTING = '165.22.75.163'
