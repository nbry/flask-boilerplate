from flask import Flask

# Blueprints (for routes)
from project.routes import general_api_blueprint


# *****************************
# APPLICATION FACTORY
# *****************************

def create_app(config_file=None):
    """
    Create instance of a Flask app with configurations based on a provided
    file as an argument. Returns the app.
    """

    # Create Flask App Instance
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_file)

    # Bind blueprints
    register_blueprints(app)

    return app


# *****************************
# REGISTERING BLUEPRINTS
# *****************************
def register_blueprints(app):
    """
    Register all blueprints to an instantiated Flask application.
    NOTE!! This function must be updated if new blueprints are to be implemented!!
    """

    app.register_blueprint(general_api_blueprint)
