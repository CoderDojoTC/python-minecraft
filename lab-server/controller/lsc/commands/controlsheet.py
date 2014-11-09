'''Command line handlers for managing the Control Sheet.'''

import logging
import os

from cliff.lister import Lister

import lsc.config as config
import lsc.model.sheet as sheet


class Show(Lister):
    '''Dumps the information from the Control Sheet to the screen
    '''

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        '''Method invoked by the Cliff framework'''

        # Obtain the data from the Google Sheet
        data = sheet.Data(email=config.email,
                          password=config.password,
                          sheetname=config.spreadsheet,
                          tabname=config.worksheet)

        return (data.headers,
                data.raw_contents())
