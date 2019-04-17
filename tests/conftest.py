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
