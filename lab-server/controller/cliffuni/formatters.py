"""Output formatters that support unicode.
"""

import csv

from cliff.formatters.base import ListFormatter, SingleFormatter
import csvkit.unicsv


class UniCsvFormatter(ListFormatter):
    """Unicode CSV file"""


    QUOTE_MODES = {
        'all': csv.QUOTE_ALL,
        'minimal': csv.QUOTE_MINIMAL,
        'nonnumeric': csv.QUOTE_NONNUMERIC,
        'none': csv.QUOTE_NONE,
    }

    def add_argument_group(self, parser):
        group = parser.add_argument_group('Unicode CSV Formatter')
        group.add_argument(
            '--uquote',
            choices=sorted(self.QUOTE_MODES.keys()),
            dest='quote_mode',
            default='nonnumeric',
            help='when to include quotes, defaults to nonnumeric',
        )

    def emit_list(self, column_names, data, stdout, parsed_args):
        writer = csvkit.unicsv.UnicodeCSVWriter(stdout,
                            quoting=self.QUOTE_MODES[parsed_args.quote_mode],
                            )
        writer.writerow(column_names)
        for row in data:
            writer.writerow(row)
        return
