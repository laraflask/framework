import laraflask

# Import app.py bootstrap file
from bootstrap.app import AppBootstrap

# Import service provider
from app.Providers.RouteServiceProvider import RouteServiceProvider

# Import middleware
from laraflask.Http.Middleware.ExcludeCSRF import ExcludeCSRF

# Import Flask
from flask import Flask

# Install necessary packages
from flask_wtf.csrf import CSRFProtect
from laraflask.Helpers.config import Config
from flask import request

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
        
        # Set the app secret key
        self.app.secret_key = self.get_config('app.secret_key')

        # Set the app debug mode
        self.app.debug = self.get_config('app.app_debug')

        # Set the app base url
        self.app.config['BASE_URL'] = self.get_config('app.app_host') + ':' + str(self.get_config('app.app_port'))

        # Create a CSRF protection
        self.csrf = CSRFProtect()

        # Set the app version
        self.version = laraflask.__version__

    # Run the Flask app
    def run(self):
        # Register before request middleware
        @self.app.before_request 
        def exclude_csrf():
            # Register the ExcludeCSRF middleware
            return ExcludeCSRF(
                app=self.app,
                request=request,
                csrf=self.csrf
            ).register()
        
        # Register after request middleware
        @self.app.after_request
        def after_request(response):
            return response

        # Register routes
        self.register_routes()

        # Register CSRF protection
        self.register_csrf()

        # Run the Flask app
        return self.app.run(
            host=self.get_config('app.app_host'),
            port=self.get_config('app.app_port'),
            debug=self.app.debug
        )

    # Register routes
    def register_routes(self):
        return RouteServiceProvider(self.app).boot()
    
    # Register CSRF protection
    def register_csrf(self):
        return self.csrf.init_app(self.app)
    
    # Get the app configuration
    def get_config(self, key):
        return Config().get(key)

    # Call the Flask app
    def __call__(self):
        return self.app