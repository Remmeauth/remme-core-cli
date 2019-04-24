"""
Provide implementation of the CLI configurations file.
"""
import pathlib
import platform

import yaml
from accessify import private

from cli.constants import (
    CLI_CONFIG_FILE_NAME,
    LINUX_NODE_PRIVATE_KEY_FILE_PATH,
    SUPPORTED_OS_TO_EXECUTE_NODE_MANAGEMENT_COMMANDS,
)
from cli.errors import NotSupportedOsToGetNodePrivateKeyError


class ConfigParameters:
    """
    Configuration parameters data transfer object.
    """

    def __init__(self, node_url):
        self._node_url = node_url

    @property
    def node_url(self):
        """
        Get configuration file's node url.
        """
        return self._node_url


class ConfigFile:
    """
    Implementation of command line interface configuration file.
    """

    @property
    def path(self):
        """
        Get path pointing to the user's home directory.
        """
        return str(pathlib.Path.home())

    @private
    def read(self, name):
        """
        Read configuration file.

        Return dictionary if configurations are presented, else None.
        """
        try:
            with open(self.path + '/.' + name + '.yml') as config_file:
                return yaml.safe_load(config_file)

        except FileNotFoundError:
            return

    def parse(self, name=CLI_CONFIG_FILE_NAME):
        """
        Parse configuration file.
        """
        config_as_dict = self.read(name=name)

        if config_as_dict is None:
            return ConfigParameters(node_url=None)

        node_url = config_as_dict.get('node-url')

        return ConfigParameters(node_url=node_url)


class NodePrivateKey:
    """
    Implementation of the node's private key.
    """

    @staticmethod
    def get(file_path=LINUX_NODE_PRIVATE_KEY_FILE_PATH):
        """
        Get the node's private key.

        Supported operating systems to get the private key are: Linux.
        Not supported operating systems to get the private key are: Darwin (aka MacOS), Windows.
        """
        if platform.system() not in SUPPORTED_OS_TO_EXECUTE_NODE_MANAGEMENT_COMMANDS:
            raise NotSupportedOsToGetNodePrivateKeyError(
                'The current operating system is not supported to get the node\'s private key.',
            )

        try:
            with open(file_path) as private_key_file:
                return private_key_file.readline().rstrip()

        except FileNotFoundError:
            raise FileNotFoundError('Private key hasn\'t been founded on the machine.')
