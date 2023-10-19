import json
from contextlib import contextmanager
from os import path

from pytest import fixture

from utils.config_validator import validate_config
from utils.logger_formatter import LOGGER
from utils.project_directory_finder import get_project_directory


@contextmanager
@fixture(scope='session')
def config():
    """
    Fixture to load the configuration data from a JSON file.

    :return: The configuration data as a dictionary.
    """
    directory = get_project_directory()
    LOGGER.info('Directory', extra={'Directory': directory})
    file_address = path.join(directory, 'config.json')
    LOGGER.info('File address', extra={'File address': file_address})
    with open(file_address, encoding='utf-8') as file_name:
        config_data = json.load(file_name)
        LOGGER.info('Config data', extra={'Config File Data': config_data})
    validate_config(config_data)
    return config_data
