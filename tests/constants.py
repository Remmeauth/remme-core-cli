"""
Provide constants for testing a command line interface.
"""
import pathlib

NODE_PRIVATE_KEY_DIRECTORY_PATH = str(pathlib.Path.home()) + '/docker/volumes/remme_validator_keys/_data/'
NODE_PRIVATE_KEY_FILE_PATH_IN_TESTING = NODE_PRIVATE_KEY_DIRECTORY_PATH + 'validator.priv'
