'''Abstraction model for our lab containers managed in Docker'''

from datetime import datetime

import logging
import os
import os.path

from docker import Client
from docker import errors

import lsc.config as config


class Instance(object):
    '''Wraps all operations on Lab instances

    Each instance is defined by a record from the Lab Control
    Sheet. The instance can have a Docker container and an external
    directory, passed to the container as a volume.
    '''

    log = logging.getLogger(__name__)

    docker_api = None

    def __init__(self, rec):
        self.rec = rec

    # ------------------------------------------------------------------------
    # Properties

    def safe_name(self):
        '''Unique name for the instance, based on instance number'''
        return "instance_{0}".format(int(self.rec.cols.inst_nmbr))

    def instance_dir(self):
        '''Path to the instance directory'''
        return os.path.join(config.instance_data_dir, self.safe_name())

    def notebook_dir(self):
        '''Path to the instance's IPython notebook directory'''
        return os.path.join(self.instance_dir(), 'notebooks')

    def world_dir(self):
        '''Path to the instance's Minecraft world directory'''
        return os.path.join(self.instance_dir(), 'server-files', 'worlds')

    def ensure_docker_api(self):
        if not self.docker_api:
            '''Connect to Docker and gets access to the Client API'''
            self.docker_api = Client(base_url=config.docker_control_url)


    # ------------------------------------------------------------------------
    # Status methods

    def server_status(self):
        self.ensure_docker_api()
        try:
            cd = self.docker_api.inspect_container(self.safe_name())
            if cd['State']['Paused']:
                return "Paused"
            elif cd['State']['Running']:
                return "Running"
            else:
                return "Stopped"
        except errors.APIError, ae:
            return "None"
        pass

    def world_status(self):
        if os.path.isdir(self.world_dir()):
            return 'Available'
        else:
            return 'Unavailable'

    def notebooks_status(self):
        if os.path.isdir(self.notebook_dir()):
            return 'Available'
        else:
            return 'Unavailable'

    def container_ids(self):
        self.ensure_docker_api()
        try:
            cd = self.docker_api.inspect_container(self.safe_name())
            return cd['Id']
        except errors.APIError, ae:
            return "None"

    def gather_status(self):
        ''' Gather status from the parts managed by the LSC '''
        self.rec.replace_cols(servers=self.server_status(),
                              world=self.world_status(),
                              notebooks=self.notebooks_status(),
                              status_as_of=str(datetime.now()),
                              container_ids=self.container_ids() )


    def lsc_message(self, message):
        ''' Convenience method to set the LSC Message '''
        self.rec.replace_cols(lsc_message=message.format(r=self.rec.cols))


    # ------------------------------------------------------------------------
    # Dispatch and its commands

    def unimplemented(self):
        ''' Invoked command has not yet been implemented
        '''
        self.lsc_message("Unimplemented command '{r.command}'")


    def noop(self):
        ''' Take no action on the record
        '''
        pass

    def run(self):
        ''' Run the instance according to the settings in the LSC
        '''
        self.log.info("Preparing to launch instance {0.inst_nmbr}".format(self.rec.cols))
        self.ensure_docker_api()

        if self.server_status() == 'Running':
            self.lsc_message("Already running")
        elif self.server_status() == 'Paused':
            self.docker_api.unpause(self.safe_name())
            self.lsc_message("Unpaused")
        elif self.server_status() == 'Stopped':
            self.docker_api.restart(self.safe_name())
            self.lsc_message("Restarted")
        else:
            # Prepare to run the instance

            # Create the instance directory, if needed
            if not os.path.isdir(self.instance_dir()):
                os.mkdir(self.instance_dir())

            # Create the container
            container = self.docker_api.create_container(
                name=self.safe_name(),
                image='coderdojotc.org/python-minecraft-student',
                detach=True,
                volumes=['/home/student/minecraft-lab'],
                environment = {
                    'MOJANG_ACCOUNTS': self.rec.cols.mojang_accounts,
                    'STUDENT_PASSWORD': self.rec.cols.student_password,
                    'CODERDOJO_REPO': config.sourcecode_repo,
                },
                ports = [8888, 25565],
            )

            # Then start it
            response = self.docker_api.start(
                container=container.get('Id'),
                binds={
                    self.instance_dir(): {
                        'bind': '/home/student/minecraft-lab',
                        'ro': False,
                    },
                },
                port_bindings={
                    8888: self.rec.cols.ipython_port,
                    25565: self.rec.cols.minecraft_port,
                },
            )
            self.lsc_message("Run response {0}".format(response))

    def down(self):
        ''' Down the instance
        '''
        self.log.info("Preparing to down instance {0.inst_nmbr}".format(self.rec.cols))
        self.ensure_docker_api()

        if self.server_status() == 'Running':
            self.docker_api.stop(container=self.safe_name(), timeout=15)
            self.lsc_message("Stopped")
        elif self.server_status() == 'Paused':
            self.docker_api.unpause(self.safe_name())
            self.docker_api.stop(container=self.safe_name(), timeout=15)
            self.lsc_message("Stopped")
        else:
            self.lsc_message("Not running")


    COMMAND_PLACEHOLDER = '_______'
    COMMANDS = {
        'RUN': run,
        'DOWN': down,
        'RESETWORLD': unimplemented,
        'RESETNOTEBOOKS': unimplemented,
        'DESTROY': unimplemented,
        '': noop,
        COMMAND_PLACEHOLDER: noop,
    }

    def dispatch(self):
        ''' Invoke the appropriate method, based on the command in the record
        '''
        self.gather_status()
        if self.rec.cols.command in self.COMMANDS:
            try:
                self.COMMANDS[self.rec.cols.command](self)
                self.gather_status()
            except Exception, e:
                self.lsc_message("Exception occurred: {e}".format(e=e))
            self.rec.replace_cols(command=self.COMMAND_PLACEHOLDER)
        else:
            self.lsc_message("Unrecognized command '{r.command}'")
