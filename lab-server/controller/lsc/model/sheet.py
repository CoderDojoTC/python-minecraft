'''Data model abstraction over the Control Sheet'''

import itertools

import gspread


# Give easier names to the column headings in the Sheet
INST_NMBR="Inst #"
STUDENTS_NAME="Student's Name"
MOJANG_ACCOUNTS="Mojang Accounts"
MINECRAFT_PORT="Minecraft Port"
IPYTHON_PORT="IPython Port"
IPYTHON_PASSWORD="IPython Password"
INSTANCE_TYPE="Instance Type"
WORLD_SEED="World Seed"
DESIRED_INSTANCE_STATE="Desired Instance State"
CURRENT_INSTANCE_STATE="Current Instance State"
STATE_AS_OF="State As Of"
CONTAINER_IDS="Container IDs"
LSC_MESSAGE="LSC Message"
S3_BUCKET="S3 Bucket"


class Data(object):
    '''Wraps all operations on the Control Sheet'''

    def __init__(self, email, password, sheetname, tabname):
        '''Connect to Google and gets access to the Sheet'''

        # Login with a Google account
        gc = gspread.login(email, password)

        # Open the spreadsheet and worksheet
        spreadsheet = gc.open(sheetname)
        self.wks = spreadsheet.worksheet(tabname)

        # Save a copy of the headers
        self.headers = self.wks.row_values(1)

        # Save a copy of the items
        self.raw_items = itertools.islice(self.wks.get_all_values(), 1, None)


    def raw_contents(self):
        '''Generator that returns the original contents of the Sheet'''
        for row in self.raw_items:
            yield row

    def scrubbed_contents(self):
        '''Return the contents of the Sheet as dicts, cleansed and ready for output'''

        # Create a clean dict from each row
        results = {}
        for idx, row_contents in enumerate(self.raw_items):
            # Build the initial dict from the stripped contents
            rdict = dict(zip(self.headers, [v.strip() for v in row_contents]))
            rdict['row_number'] = idx - 2

            # Remove the entry with no key
            del rdict[None]

            # Save the results by Instance Number, so we replace with
            # later rows that happen to have the same value
            results[rdict[INSTANCE_NMBR]] = rdict

        # Loop through each result
        for rdict in results.values():
            yield rdict


    def replace(self):
        '''Replace a single row from the current Sheet with new contents'''
        pass


    def append(self):
        '''Append a single row to the current Sheet'''
        pass
