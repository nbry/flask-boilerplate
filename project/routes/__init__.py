from flask import Blueprint

# List Blueprints Here:
general_api_blueprint = Blueprint('general_api', __name__)

# THIS LINE MUST BE BELOW BLUEPRINTS TO PROVIDE CONTEXT TO ROUTE FILES:
from project.routes import general_routes
