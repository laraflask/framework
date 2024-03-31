import click

# Import driver
from laraflask.Drivers.Cli.Driver import Driver
from laraflask.Drivers.Cli.Check import Check as CheckDriver

class LaraflaskCli:

    def __init__(self, app):
        self.driver = Driver(app, click)
        self.check_driver = CheckDriver(app, click)
        return
    
    # Register the CLI commands
    def register(self):
        self.check_version()
        return
        
    # Check the something inside the app
    def check_version(self):
        self.driver.command_can_run_in(['development', 'local'])

        @click.command()
        @click.option(
            '--check', 
            help='Check the something inside the app', 
            type=click.Choice([
                    'version', 
                    'environment', 
                    'base_url', 
                    'base_path', 
                    'filesystem'
                ]
            ))
        def check(check):

            # Check the version of the app  
            if check == 'version':
                self.check_driver.check_laraflask_version()

            # Check the application environment
            elif check == 'environment':
                self.check_driver.check_laraflask_environment()

            # Check the app base url
            elif check == 'base_url':
                self.check_driver.check_laraflask_base_url()

            # Check the app base path
            elif check == 'base_path':
                self.check_driver.check_laraflask_base_path()

            # Check the app filesystem configuration
            elif check == 'filesystem':
                self.check_driver.check_laraflask_filesystem()

            return 

        return check()

# EOF