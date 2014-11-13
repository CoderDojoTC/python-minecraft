'''Command line handlers for managing the Lab.'''

from itertools import chain

import logging
import os

from cliff.command import Command
from cliff.lister import Lister

import lsc.config as config
import lsc.model.controlsheet as controlsheet
import lsc.model.instance as instance


class Show(Lister):
    '''Show the current state of the lab, from the Control Sheet
    '''

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        '''Method invoked by the Cliff framework'''

        # Obtain the data from the Google Sheet
        cs = controlsheet.Data(email=config.email,
                               password=config.password,
                               sheetname=config.spreadsheet,
                               tabname=config.worksheet)

        return (cs.headers,
                # Get only the column tuples from each Record
                [rec.cols for rec in cs.records()])


class ProcessCommands(Lister):
    '''Walks through the Control Sheet and attempts to act on each command

    It also checks the current state of each instance and updates the
    appropriate columns in the Control Sheet.

    '''

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        '''Method invoked by the Cliff framework'''

        # Obtain the data from the Google Sheet
        cs = controlsheet.Data(email=config.email,
                               password=config.password,
                               sheetname=config.spreadsheet,
                               tabname=config.worksheet)

        # Work through each record in the control sheet
        ret_val = []
        for rec in cs.records():
            # Update the record with state we can determine
            inst = instance.Instance(rec)
            inst.gather_status()

            # Process the commands we know
            inst.dispatch()

            # Write the record if needed
            #cs.update(rec)

            # Save it, temp, so we can list it
            ret_val.append(rec.cols)

        return (cs.headers, ret_val)
