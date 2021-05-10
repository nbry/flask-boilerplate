from flask import Flask

# Blueprints (for routes)
from project.routes import all_blueprints

# # Extensions (MANUAL ADDITIONS HERE)
# # [USE THE FOLLOWING IF SETTING UP PROJECT WITH A DATABASE]:
# from project.all_extensions import db


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

    # # Initialize extensions and link to app
    # # [USE THE FOLLOWING IF SETTING UP PROJECT WITH A DATABASE]:
    #  initialize_extensions(app)

    return app


# *****************************
# INITIALIZING EXTENSIONS
# *****************************
# # [USE THE FOLLOWING IF SETTING UP PROJECT WITH A DATABASE]:
# def initialize_extensions(app):
#     """
#     Pass Flask extensions to an instantiated Flask app.
#     """

#     db.init_app(app)


# *****************************
# REGISTERING BLUEPRINTS
# *****************************
def register_blueprints(app):
    """
    Register all blueprints to an instantiated Flask application.

    NOTE!! ENSURE project/routes/__init__.py is set up correctly!
    All your blueprints must be imported into that file and put in a
    list named all_blueprints.
    """

    for blueprint in all_blueprints:
        app.register_blueprint(blueprint)
