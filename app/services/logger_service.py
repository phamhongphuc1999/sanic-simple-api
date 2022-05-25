import logging
from logging.handlers import RotatingFileHandler

FORMATTER = logging.Formatter(fmt='[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s(%(pathname)s:%(lineno)d)',
                              datefmt='%m-%d-%Y %H:%M:%S %Z')


def get_console_handler():
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = RotatingFileHandler('logging.log', maxBytes=2000)
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    return logger


app_logger = get_logger("bridge_logger")
