'''Config object for the lsc project'''

import ConfigParser
import os.path

CONFIG_FILENAME = 'lsc.ini'
CONFIG_SEARCH_PATH = ['.']

# Try and read in the configuration file and set the necessary
# variables

_config = ConfigParser.SafeConfigParser()

_config.read([os.path.join(dirname, CONFIG_FILENAME)
              for dirname in CONFIG_SEARCH_PATH])

# These are the values we expect to find
email       = _config.get('Lab Config Sheet', 'email')
password    = _config.get('Lab Config Sheet', 'password')
spreadsheet = _config.get('Lab Config Sheet', 'spreadsheet')
worksheet   = _config.get('Lab Config Sheet', 'worksheet')

instance_data_dir  = _config.get('Instances', 'instance_data_dir')
docker_control_url = _config.get('Instances', 'docker_control_url')
sourcecode_repo    = _config.get('Instances', 'sourcecode_repo')
docker_image       = _config.get('Instances', 'docker_image')
