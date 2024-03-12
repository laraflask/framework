# Import the ExcludeCSRF middleware from application
from app.Http.Middleware.excludeCsrf import ExcludeCSRFMiddleware

class ExcludeCSRF:
    def __init__(self, app, request, csrf):
        self.app = app
        self.request = request
        self.csrf = csrf
        return

    # Register the middleware
    def register(self):
        # Get the exclude routes
        exclude_csrf_array = ExcludeCSRFMiddleware().exclude_routes

        # Get current route from app
        current_route = self.request.path

        # Register the before request middleware
        for route in exclude_csrf_array:
            # List all blueprints routes
            for blueprint in self.app.url_map.iter_rules():
                # Check if the route is in the exclude routes
                if (route['route'] == str(blueprint)) and (route['function'] == blueprint.endpoint):
                    # Disable CSRF protection for the route
                    self.csrf.exempt(self.app.view_functions[blueprint.endpoint])
        return        