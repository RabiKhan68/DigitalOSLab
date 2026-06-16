import logging
import os

# CREATE LOG DIRECTORY

LOG_FOLDER = "logs"

if not os.path.exists(LOG_FOLDER):

    os.makedirs(LOG_FOLDER)


# LOG FILE CONFIGURATION

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "os_simulator.log"
)


# LOGGER CONFIGURATION

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    ),
    datefmt="%Y-%m-%d %H:%M:%S"
)


# INFO LOGGING

def log_event(message):
    """
    Log normal system events.
    """

    logging.info(message)


# WARNING LOGGING

def log_warning(message):
    """
    Log warning messages.
    """

    logging.warning(message)


# ERROR LOGGING

def log_error(message):
    """
    Log error messages.
    """

    logging.error(message)


# CRITICAL LOGGING

def log_critical(message):
    """
    Log critical system failures.
    """

    logging.critical(message)
