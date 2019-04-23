"""
Provide configurations for testing.
"""
import os
import pathlib
import shutil
import sys

import pytest


def pytest_configure():
    """
    Add root folder to the `sys.path`.

    Root folder if a folder that contains all source code.

    `sys.path` is basically a variable that determines where on the file system Python will look for modules to import.
    So, if you run import `whatever`, Python will first search the current directory, and then start looking
    through every directory in `sys.path` until it finds a module named `whatever`.

    References:
        - https://docs.pytest.org/en/latest/goodpractices.html
        - https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code
    """
    sys.path.insert(0, str(pathlib.Path(__file__).parents[1]))


@pytest.yield_fixture()
def create_config_file():
    """
    Create configuration file for testing.

    The example of the configuration file is located in the tests fixture folder.
    """
    fixture_file_path = os.getcwd() + '/tests/fixtures/.remme-core-cli.yml'
    path_to_copy_fixture_file_to = str(pathlib.Path.home()) + '/.remme-core-cli.yml'

    shutil.copyfile(fixture_file_path, path_to_copy_fixture_file_to)

    yield

    os.remove(path_to_copy_fixture_file_to)


@pytest.yield_fixture()
def create_config_file_without_node_url():
    """
    Create configuration file without node url for testing.

    The example of the configuration file is located in the tests fixture folder.
    """
    fixture_file_path = os.getcwd() + '/tests/fixtures/.remme-core-cli-without-url.yml'
    path_to_copy_fixture_file_to = str(pathlib.Path.home()) + '/.remme-core-cli-without-url.yml'

    shutil.copyfile(fixture_file_path, path_to_copy_fixture_file_to)

    yield

    os.remove(path_to_copy_fixture_file_to)


@pytest.yield_fixture()
def create_empty_config_file():
    """
    Create empty configuration file for testing.

    The example of the configuration file is located in the tests fixture folder.
    """
    fixture_file_path = os.getcwd() + '/tests/fixtures/.remme-core-cli-empty-file.yml'
    path_to_copy_fixture_file_to = str(pathlib.Path.home()) + '/.remme-core-cli-empty-file.yml'

    shutil.copyfile(fixture_file_path, path_to_copy_fixture_file_to)

    yield

    os.remove(path_to_copy_fixture_file_to)


class SentTransaction:
    """
    Impose transaction data transfer object.
    """

    @property
    def batch_id(self):
        """
        Get batch identifier of the sent transaction.
        :return:
        """
        return '37809770b004dcbc7dae116fd9f17428255ddddee3304c9b3d14609d2792e78f' \
               '08f5308af03fd4aa18ff1d868f043b12dd7b0a792e141f000a2505acd4b7a956'


@pytest.fixture()
def sent_transaction():
    """
    Get sent transaction fixture.
    """
    return SentTransaction()
