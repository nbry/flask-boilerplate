"""
GENERAL ROUTES:

Code for routes should be expressive.
Functions, logic, algorithms etc. should be in a separate file.
"""

from flask import jsonify
from . import general_api_blueprint


@general_api_blueprint.route('/ping')
def check_api_status():
    """
    Default PING route that checks if API is running.
    If API is running, this route will ALWAYS return:
    "success": true.
    """

    return jsonify({"success": True})
