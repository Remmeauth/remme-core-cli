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
        """
        return '37809770b004dcbc7dae116fd9f17428255ddddee3304c9b3d14609d2792e78f' \
               '08f5308af03fd4aa18ff1d868f043b12dd7b0a792e141f000a2505acd4b7a956'


class PublicKeyInfo:
    """
    Impose public key information data transfer object.
    """

    @property
    def data(self):
        """
        Get data of public key information.
        """
        return {
            'address': 'a23be1ae97d605bcbe61c312d9a443c010dbe7e6a0761e24b10d5368829ab0a7d36acc',
            'entity_hash': '13517cee1694346b584c08f5d84cc584b407043ef6a682942b1e18f0466cf1e2'
                           'dede1756499ac8a2ee495cba258c609ea6147b4daa15225ba60ec5ffca419bd6',
            'entity_hash_signature': '6e081607aac18e63a44265e0054fb3e60d3791ac2292925c56d54df216396a3af42e96557a0da09b'
                                     '236cdb5970ca5272473dcc9d71f16978e09a26bfb5e96562d8002473cfdf29b4c04dcc97cd4fa9d7'
                                     '68ea13bd04b7479fe2f5965cfb0f944848511c9f597eacd4a23a1fd66aabfa95f45130fae1ae2507'
                                     'e8ed8d8ee308c77a042c86bbc476e2d3ed46c4b3c2a86c87470bb94c6e266cfd44bc513d04e5523c'
                                     '7faf08887df4e37f2e31bda1bf403cb7bb3145602cd56dea7965e6e417d86620704a68013e95bbda'
                                     '6a81e3dfb86aa489fa060e78bf9edfc4329ffc1f8484ecc610fccb5302499e1f18d0e2584db9c23c'
                                     'db4b0485ccda7cab17896b8fec28c851',
            'is_revoked': False,
            'is_valid': True,
            'owner_public_key': '03738df3f4ac3621ba8e89413d3ff4ad036c3a0a4dbb164b695885aab6aab614ad',
            'public_key': '30820122300d06092a864886f70d01010105000382010f003082010a028201010098ed61c659566b05d4017a0b5'
                          '9b7ce15f6be8432a470713cf3f0ac40b9ded6b65c227704c9bbde4f41a81a380c1ebadb771d1295418805eb16d5'
                          '14c0eb8a8747d08bb1cb5269d5ecb1152d64a8d8bb14836589f6babce22c2deac7dc6b80fcf285c74b67c5ccaf7'
                          '464df47d10dccecf02d8c4ed9924a8f4ee0df8661d9378fdb0a42355eda8128e88f7871ac5ea7c2605afa1b2b40'
                          '0e1a13b9f9fcf037aa7defcfe2abdcc4b9635d8601d1755660c0838fb2e10c35a88e7b9c1fc89db58cb6fa701a8'
                          'a80f3dbbf587c1af43e7029e4bc79a26012cb9534d66a818c68acb9707a1a1a7c02b781df4928540053693696fb'
                          '058d1935fed35cf307c362e7f601710b0203010001',
            'type': 'rsa',
            'valid_from': 1554753277,
            'valid_to': 1585857277,
        }


@pytest.fixture()
def sent_transaction():
    """
    Get sent transaction fixture.
    """
    return SentTransaction()


@pytest.fixture()
def public_key_info():
    """
    Get public key information fixture.
    """
    return PublicKeyInfo()
