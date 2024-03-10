
# Import app configuration class
from config.app import AppConfiguration

# Import app.py bootstrap file
from bootstrap.app import AppBootstrap

# Import service provider
from app.Providers.RouteServiceProvider import RouteServiceProvider

# Import Flask
from flask import Flask

# Create a Core class
class Core:

    # Initialize the Core class
    def __init__(self):
        # Create a Flask app
        self.app = Flask(__name__, 
                        template_folder=AppBootstrap().app_templates_path,
                        static_folder=AppBootstrap().app_static_path,
                        root_path=AppBootstrap().app_base_path
                    )

    # Run the Flask app
    def run(self):
        # Register routes
        self.register_routes()

        # Run the Flask app
        return self.app.run(
            host=AppConfiguration().app_host,
            port=AppConfiguration().app_port,
            debug=AppConfiguration().app_debug
        )

    # Register routes
    def register_routes(self):
        return RouteServiceProvider(self.app).boot()
    