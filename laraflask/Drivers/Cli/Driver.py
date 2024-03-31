# This file is responsible for handling the CLI commands
class Driver: 
    def __init__(self, app, click):
        self.app = app
        self.click = click
        return
    
    # Protect command can run when the environment in
    def command_can_run_in(self, env = []):
        # Get the app environment
        app_env = self.app.get_config('app.app_environment')

        # Check if the app environment is in the list
        if app_env in env:
            return True

        raise Exception('Command can only run in ' + ', '.join(env) + ' environment')