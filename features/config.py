import json
from contextlib import contextmanager

from pytest import fixture

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
    file_address = directory + '/config.json'
    with open(file_address, encoding='utf-8') as file_name:
        config_data = json.load(file_name)
        LOGGER.info('Config data', extra={'Config File Data': config_data})
    config_data['browser'] = config_data['browser'].lower()
    browser_name = config_data['browser']
    supported_browsers = ['firefox', 'chrome', 'webkit']
    if browser_name not in supported_browsers:
        raise TypeError(
            f'Browser {browser_name} is not supported, It must be one of: {supported_browsers}'
        )
    return config_data
