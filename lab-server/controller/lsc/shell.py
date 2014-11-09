'''The Lab Server Controller is a command line tool that helps manage
the lab server used for teaching the CoderDojo TC's Python-Minecraft
code group.

'''

# This script uses the Cliff framework. It is installed and configured
# through the package's setup.py file, so check the entry_points defined
# there.


import logging
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager
#import lsc


class LabServerControllerApp(App):

    CONSOLE_MESSAGE_FORMAT = '%(levelname)s: %(name)s %(message)s'

    log = logging.getLogger(__name__)

    def __init__(self):
        super(LabServerControllerApp, self).__init__(
            description=__doc__.strip(),
#            version=lsc.__version__,
            version='0.1',
            command_manager=CommandManager('lsc.commands'),
            )


    def initialize_app(self, argv):
        """ Application initialization code
        """

        # Pick up any default initializations
        super(LabServerControllerApp, self).initialize_app(argv)

        if self.options.debug:
            self.dump_stack_trace = True
        else:
            self.dump_stack_trace = False

        self.log.debug('initialize_app')


    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)


    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    return LabServerControllerApp().run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
