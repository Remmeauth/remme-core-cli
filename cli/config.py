"""
Provide implementation of the Remme Core CLI checking configurations manipulating.
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
    Implementation of Remme Core CLI configuration file.
    """

    @property
    def path(self):
        """
        Get path pointing to the user's home directory.
        """
        return str(pathlib.Path.home())

    @private
    def read(self, name=CLI_CONFIG_FILE_NAME):
        """
        Read configuration file.

        Return dictionary.
        """
        with open(self.path + '/.' + name + '.yml') as f:
            return yaml.safe_load(f)

    def parse(self):
        """
        Parse configuration file.
        """
        config_as_dict = self.read()

        return ConfigParameters(node_url=config_as_dict.get('node').get('url'))
