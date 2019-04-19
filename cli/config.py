"""
Provide implementation of the CLI configurations file.
"""
import pathlib

import yaml
from accessify import private

from cli.constants import CLI_CONFIG_FILE_NAME


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

        Return dictionary.
        """
        with open(self.path + '/.' + name + '.yml') as config_file:
            return yaml.safe_load(config_file)

    def parse(self, name=CLI_CONFIG_FILE_NAME):
        """
        Parse configuration file.
        """
        config_as_dict = self.read(name=name)

        if config_as_dict is None:
            return ConfigParameters(node_url=None)

        node_url = config_as_dict.get('node-url')

        return ConfigParameters(node_url=node_url)
