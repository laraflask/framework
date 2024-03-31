# This file is responsible for handling the Check CLI commands
class Check: 
    def __init__(self, app, click):
        self.app = app
        self.click = click
        return
    
    # Check the version of the app
    def check_laraflask_version(self):
        self.click.echo('Laraflask version: ' + self.app.version)
        return
    
    # Check the application environment
    def check_laraflask_environment(self):
        self.click.echo('Laraflask environment: ' + self.app.get_config('app.app_environment'))
        return
    
    # Check the app base url
    def check_laraflask_base_url(self):
        self.click.echo('Laraflask base url: ' + self.app.app.config['BASE_URL'])
        return
    
    # Check the app base path
    def check_laraflask_base_path(self):
        self.click.echo('Laraflask base path: ' + self.app.app.root_path)
        return
    
    # Check the app filesystem configuration
    def check_laraflask_filesystem(self):
        self.click.echo('Laraflask filesystem configuration: ' + self.app.get_config('filesystem.default'))
        return