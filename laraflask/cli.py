import click

# Import driver
from laraflask.Drivers.Cli.Driver import Driver
from laraflask.Drivers.Cli.Check import Check as CheckDriver
from laraflask.Drivers.Cli.Database import Database as DatabaseDriver

class LaraflaskCli:

    def __init__(self, app):
        self.driver = Driver(app, click)

        self.check_driver = CheckDriver(app, click)
        self.database_driver = DatabaseDriver(app, click)
        return
    
    # Register the CLI commands
    def register(self):
        @click.group()
        def cli():
            """ 
            Laraflask Framework Application
            """            
            pass

        # 1. Check the something inside the app
        @cli.command()
        @click.argument('check', type=click.Choice([
                'version', 
                'environment', 
                'base_url', 
                'base_path', 
                'filesystem'
            ]))
        def check(check):
            # Protect the command from running in the wrong environment
            self.driver.command_can_run_in(['development', 'local'])

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
        
        # 2. Manage the database
        @cli.command()
        @click.argument('command', type=click.Choice([
                'new_sqlite_database'
            ]))
        
        def manage_database(command):
            # Protect the command from running in the wrong environment
            self.driver.command_can_run_in(['development', 'local'])

            # Create a something inside the app
            if command == 'new_sqlite_database':
                self.database_driver.new_sqlite_database()

        return cli()

# EOF