# Utils
import configparser
import os
import logging
import datetime
import shared.core as core

SETTINGS = configparser.ConfigParser()
SETTINGS.read('app/settings.ini')
SETTINGS.sections()
LOGGER = SETTINGS['LOGGER']

def setup_custom_logger(name: str, log_file_name: str, subfolder: str) -> logging.Logger:
    '''
    Setea un custom logger en el modulo que lo necesite
    name : str nombre instancia log (__name__)
    log_file_name : str nombre que tendra el archivo log
    subfolder: subcarpeta de la carpeta log en la que se guardara este log en particular
    '''
    this_log_root_path = os.path.join(LOGGER['LOG_ROOT'], subfolder)    
    core.create_directory(this_log_root_path)
    formatter = logging.Formatter(fmt='%(asctime)s [%(levelname)s][%(name)s] %(message)s')
    log_date = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S') 
    
    log_file = this_log_root_path + f'/{log_file_name}-{log_date}.log'

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger