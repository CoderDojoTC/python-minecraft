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
email       = _config.get('Lab Config Data', 'email')
password    = _config.get('Lab Config Data', 'password')
spreadsheet = _config.get('Lab Config Data', 'spreadsheet')
worksheet   = _config.get('Lab Config Data', 'worksheet')
