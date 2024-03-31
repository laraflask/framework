# This file is responsible for handling the Check CLI commands
class Database: 
    def __init__(self, app, click):
        self.app = app
        self.click = click
        return
    
    # Check the version of the app
    def new_sqlite_database(self):
        self.click.echo('Creating new SQLite database')
        return
    
    