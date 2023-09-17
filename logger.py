import json
import logging


# Function to read configuration from the JSON file
def read_config(filename):
    try:
        with open(filename, 'r') as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        return None

# Function to configure the logging system
def configure_logging(config_param):
    if config_param and 'log_level' in config_param:
        log_level = config_param['log_level']

        # Define the log file name here
        log_filename = 'app.log'

        # Create a logger
        logger = logging.getLogger()
        logger.setLevel(getattr(logging, log_level))

        # Create a file handler and set the log file name
        file_handler = logging.FileHandler(log_filename)

        # Create a formatter and set the format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

# JSON configuration file name
config_filename = 'config/config.json'

# Read configuration from the JSON file
config = read_config(config_filename)

# Configure the logging system based on the configuration
configure_logging(config['logging'])

log = logging
