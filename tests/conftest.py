"""
Provide configurations for testing.
"""
import os
import pathlib
import shutil
import sys

import pytest

NODE_PRIVATE_KEY_DIRECTORY_PATH = str(pathlib.Path.home()) + '/docker/volumes/remme_validator_keys/_data/'
NODE_PRIVATE_KEY_FILE_PATH_IN_TESTING = NODE_PRIVATE_KEY_DIRECTORY_PATH + 'validator.priv'


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


@pytest.fixture()
def node_private_key_file_path():
    """
    Get node's private key file path.
    """
    return NODE_PRIVATE_KEY_FILE_PATH_IN_TESTING


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


@pytest.yield_fixture()
def create_node_private_key_file():
    """
    Create the node's private key file.

    The example of the configuration file is located in the tests fixture folder.
    """
    fixture_file_path = os.getcwd() + '/tests/fixtures/validator.priv'

    pathlib.Path(NODE_PRIVATE_KEY_DIRECTORY_PATH).mkdir(parents=True, exist_ok=True)
    shutil.copyfile(fixture_file_path, NODE_PRIVATE_KEY_FILE_PATH_IN_TESTING)

    yield

    os.remove(NODE_PRIVATE_KEY_FILE_PATH_IN_TESTING)


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


class PublicKeyInformation:
    """
    Impose public key information data transfer object.
    """

    @property
    def data(self):
        """
        Get public key information.
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


class AtomicSwapInformation:
    """
    Impose atomic swap information data transfer object.
    """

    @property
    def data(self):
        """
        Get atomic swap information.
        """
        return {
            'sender_address': '112007be95c8bb240396446ec359d0d7f04d257b72aeb4ab1ecfe50cf36e400a96ab9c',
            'receiver_address': '112007484def48e1c6b77cf784aeabcac51222e48ae14f3821697f4040247ba01558b1',
            'amount': '10.0000',
            'swap_id': '033402fe1346742486b15a3a9966eb5249271025fc7fb0b37ed3fdb4bcce6808',
            'secret_lock': '0728356568862f9da0825aa45ae9d3642d64a6a732ad70b8857b2823dbf2a0b8',
            'created_at': 1555943451,
            'sender_address_non_local': '0xe6ca0e7c974f06471759e9a05d18b538c5ced11e',
            'state': 'OPENED',
            'email_address_encrypted_optional': '',
            'secret_key': '',
            'is_initiator': False,
        }


class NodeConfigurations:
    """
    Impose node configurations data transfer object.
    """

    @property
    def data(self):
        """
        Get node configurations.
        """
        return {
            'node_address': '116829f18683f6c30146559c9cb8d5d302545019ff00f2ab72500df99bceb7b81a1dad',
            'node_public_key': '0350e9cf23966ad404dc56438fd01ec11a913446cfd7c4fb8d95586a58718431e7',
        }


class NodeInformation:
    """
    Impose node information data transfer object.
    """

    @property
    def data(self):
        """
        Get node information.
        """
        return {
            'is_synced': True,
            'peer_count': 3,
        }


class NodeAccountInformation:
    """
    Impose node account information data transfer object.
    """

    @property
    def node_account_response(self):
        """
        Get node account information.
        """
        return {
            'balance': '0.0000',
            'last_defrost_timestamp': '0',
            'min': True,
            'node_state': 'OPENED',
            'reputation': {
                'frozen': '250000.4100',
                'unfrozen': '51071032.5900',
            },
            'shares': [
                {
                    'block_num': '552',
                    'block_timestamp': '1556178213',
                    'defrost_months': 0,
                    'frozen_share': '5440',
                    'reward': '0',
                },
            ],
        }


class OpenNodeTransaction:
    """
    Impose open node transaction's data transfer object.
    """

    @property
    def batch_id(self):
        """
        Get batch identifier of the open node transaction.
        """
        return '37809770b004dcbc7dae116fd9f17428255ddddee3304c9b3d14609d2792e78f' \
               '08f5308af03fd4aa18ff1d868f043b12dd7b0a792e141f000a2505acd4b7a956'


class OpenMasternodeTransaction:
    """
    Impose open masternode transaction's data transfer object.
    """

    @property
    def batch_id(self):
        """
        Get batch identifier of the open masternode transaction.
        """
        return '37809770b004dcbc7dae116fd9f17428255ddddee3304c9b3d14609d2792e78f' \
               '08f5308af03fd4aa18ff1d868f043b12dd7b0a792e141f000a2505acd4b7a956'


class CloseMasternodeTransaction:
    """
    Impose close masternode transaction's data transfer object.
    """

    @property
    def batch_id(self):
        """
        Get batch identifier of the close masternode transaction.
        """
        return 'ae0ad8d5379beb28211cdc3f4d70a7ef66852eb815241cb201425897fc470e72' \
               '7c34e67ea77525ac696633afd27cca88227df52493889edcbb6fb840b4c93326'


class Transaction:
    """
    Impose transaction's data transfer object.
    """

    @property
    def batch_id(self):
        """
        Get batch identifier of the transaction.
        """
        return '37809770b004dcbc7dae116fd9f17428255ddddee3304c9b3d14609d2792e78f' \
               '08f5308af03fd4aa18ff1d868f043b12dd7b0a792e141f000a2505acd4b7a956'


class UnfrozenToOperationalTransaction:
    """
    Impose unfrozen to opetational balance transaction's data transfer object.
    """

    @property
    def batch_id(self):
        """
        Get batch identifier of the transaction.
        """
        return '37809770b004dcbc7dae116fd9f17428255ddddee3304c9b3d14609d2792e78f' \
               '08f5308af03fd4aa18ff1d868f043b12dd7b0a792e141f000a2505acd4b7a956'


@pytest.fixture()
def sent_transaction():
    """
    Get sent transaction fixture.
    """
    return SentTransaction()


@pytest.fixture()
def public_key_information():
    """
    Get public key information fixture.
    """
    return PublicKeyInformation()


@pytest.fixture()
def swap_info():
    """
    Get atomic swap information fixture.
    """
    return AtomicSwapInformation()


@pytest.fixture()
def node_configurations():
    """
    Get node configurations fixture.
    """
    return NodeConfigurations()


@pytest.fixture()
def node_information():
    """
    Get node information fixture.
    """
    return NodeInformation()


@pytest.fixture()
def node_account_information():
    """
    Get node account information fixture.
    """
    return NodeAccountInformation()


@pytest.fixture()
def open_node_transaction():
    """
    Get the open node transaction fixture.
    """
    return OpenNodeTransaction()


@pytest.fixture()
def open_masternode_transaction():
    """
    Get the open masternode transaction fixture.
    """
    return OpenMasternodeTransaction()


@pytest.fixture()
def close_masternode_transaction():
    """
    Get the close masternode transaction fixture.
    """
    return CloseMasternodeTransaction()


@pytest.fixture()
def transaction():
    """
    Get the transaction fixture.
    """
    return Transaction()


@pytest.fixture()
def unfrozen_to_operational_transaction():
    """
    Get the transaction fixture.
    """
    return UnfrozenToOperationalTransaction()
