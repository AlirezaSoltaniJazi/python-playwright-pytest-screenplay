from utils.logger_formatter import LOGGER


def validate_config(config_data: dict):
    supported_browsers = ['firefox', 'chrome', 'webkit']
    browser = config_data.get('browser')
    headed_mode_statue = config_data.get('active_headed_mode')
    LOGGER.info(
        '',
        extra={
            'Supported browsers': supported_browsers,
            'Browser': browser,
            'Headed mode statue': headed_mode_statue,
        },
    )
    # Check key missing
    if browser is None:
        raise ValueError('The "browser" key is missing!')
    if headed_mode_statue is None:
        raise ValueError('The "active_headed_mode" key is missing!')
    # Check key type
    if not isinstance(browser, str):
        raise TypeError(
            f'Browser type is invalid, It must be str. current type: {type(browser)}'
        )
    if not isinstance(headed_mode_statue, bool):
        raise TypeError(
            f'Active headed mode type is invalid, It must be boolean. current type: {type(headed_mode_statue)}'
        )
    # Check key value
    if len(browser) <= 0:
        raise ValueError('Browser value is invalid, It cannot be empty')
    if browser not in supported_browsers:
        raise ValueError(
            f'Browser {browser} is not supported, It must be one of: {supported_browsers}'
        )
