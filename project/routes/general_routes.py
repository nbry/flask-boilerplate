"""
GENERAL ROUTES:

Code for routes should be expressive.
Functions, logic, algorithms etc. should be in a separate file.
"""

from flask import Blueprint, jsonify
from project.helpers import General

# Create a blueprint. Import this into project.routes.__init__.py
general_api_blueprint = Blueprint('general_api', __name__)


@general_api_blueprint.route('/ping')
def check_api_status():
    """
    Default PING route that checks if API is running.
    If API is running, this route will ALWAYS return:
    "success": true.
    """

    return jsonify({"success": True})


@general_api_blueprint.route('/helper')
def check_helper_import():
    """
    Default HELPER route that imports the default general
    helper class, and returns a message.
    """
    message = General.sample_helper()
    return jsonify({"message": message})
