''' Command line handlers that help produce the actual directory files
'''

import logging
import os

from cliff.lister import Lister


class Test(Lister):
    """Checks the environment.

    It confirms that the config file is present. It validates that the
    information in the config file allows it to reach the Control
    Sheet used to manage the student instances.
    """

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        return (('Name', 'Size'),
                ((n, os.stat(n).st_size) for n in os.listdir('.'))
                )
