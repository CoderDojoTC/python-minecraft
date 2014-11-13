'''Data model abstraction over the Control Sheet'''

import itertools

from collections import namedtuple

import gspread


# Give easier names to the column headings in the Sheet
INST_NMBR="Inst #"
STUDENTS_NAME="Student Name"
MOJANG_ACCOUNTS="Mojang Accounts"
MINECRAFT_PORT="Minecraft Port"
IPYTHON_PORT="IPython Port"
STUDENT_PASSWORD="Student Password"
INSTANCE_TYPE="Instance Type"
COMMAND="Command"
SERVERS="Servers"
WORLD="World"
NOTEBOOKS="Notebooks"
STATUS_AS_OF="Status As Of"
CONTAINER_IDS="Container IDs"
LSC_MESSAGE="LSC Message"
S3_BUCKET="S3 Bucket"

COLUMNS = [ INST_NMBR, STUDENTS_NAME, MOJANG_ACCOUNTS, MINECRAFT_PORT,
            IPYTHON_PORT, STUDENT_PASSWORD, INSTANCE_TYPE, COMMAND,
            SERVERS, WORLD, NOTEBOOKS, STATUS_AS_OF, CONTAINER_IDS,
            LSC_MESSAGE, S3_BUCKET, ]

COLUMN_IDENTIFIERS = [ 'inst_nmbr', 'students_name',
                       'mojang_accounts', 'minecraft_port',
                       'ipython_port', 'student_password',
                       'instance_type', 'command', 'servers', 'world',
                       'notebooks', 'status_as_of', 'container_ids',
                       'lsc_message', 's3_bucket', ]

SheetCols = namedtuple('SheetCols', COLUMN_IDENTIFIERS)


class Record(object):
    '''Record from the sheet, including the values and the original row number'''
    def __init__(self, cols, row_number):
        self.cols = cols
        self.orig_cols = cols

        '''Source-sheet row number, 1-based'''
        self.row_number = row_number

    def replace_cols(self, **kwds):
        '''Replace column values in the tuple

        Call like self.replace_cols(servers="New Status")
        '''
        self.cols = self.cols._replace(**kwds)


class Data(object):
    '''Wraps all operations on the Control Sheet'''

    def __init__(self, email, password, sheetname, tabname):
        # Save the parameters
        self.email = email
        self.password = password
        self.sheetname = sheetname
        self.tabname = tabname

        # Connect to Google and get the contents of the Sheet
        self.connect()
        self.refresh()


    def connect(self):
        ''' Connect to Google '''

        # Login with a Google account
        gc = gspread.login(self.email, self.password)

        # Open the spreadsheet and worksheet
        spreadsheet = gc.open(self.sheetname)
        self.wks = spreadsheet.worksheet(self.tabname)

        # Mark the cache invalid so that it will get refreshed on the
        # next check
        self.cache_valid = False


    def refresh(self):
        ''' Retrieve the contents of the Sheet '''

        if self.cache_valid:
            return

        # Save a copy of the headers
        self.headers = self.wks.row_values(1)

        # Save a copy of the items
        self.raw_items = itertools.islice(self.wks.get_all_values(), 1, None)
        self.cache_valid = True


    def raw_contents(self):
        '''Returns the original contents of the Sheet as a series of namedtuples'''

        self.refresh()

        for row in self.raw_items:
            yield SheetCols._make(row)


    def records(self):
        '''Return the contents of the Sheet as Records, cleansed and ready for processing

        This method skips (as in, does not return them to its caller)
        rows that fail essential validation checks.
        '''

        self.refresh()

        # Make sure the retrieved headers match what this script
        # expects
        for idx, pair in enumerate(zip(COLUMNS, self.headers)):
            if pair[0] != pair[1]:
                raise NameError("Expected '{0}' in column {1}, but found '{2}'".
                                format(pair[0], idx+1, pair[1]))

        # Create the clean Records
        seen_ids = []
        for idx, row_contents in enumerate(self.raw_items):
            # Build the SheetCols from the stripped contents
            sc = SheetCols._make([v.strip() for v in row_contents])

            # Make sure the instance number is a positive integer
            try:
                if int(sc.inst_nmbr) < 0:
                    continue
            except ValueError, ve:
                continue

            # Make sure we only process each Instance Number once
            if sc.inst_nmbr in seen_ids:
                continue
            seen_ids.extend([sc.inst_nmbr])

            # Build the Record from the SheetCols
            yield Record(sc, idx+2)


    def replace(self, record):
        '''Replace a single row from the current Sheet with new contents'''
        self.cache_valid = False
        raise NotImplementedYet()


    def append(self):
        '''Append a single row to the current Sheet'''
        self.cache_valid = False
        raise NotImplementedYet()
