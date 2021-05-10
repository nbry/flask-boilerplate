"""
Use this file to create accessible instance of Flask extensions.
e.g. SQLAlchemy, Flask Praetorian etc.

IMPORTANT: Imports into project/__init__.py need to be manual.
Extensions can vary on the initialization process.

e.g. for SQLAlchemy -> db.init_app(<FLASK APP>)
for Flask Praetorain -> guard.init_app(<FLASK APP>, <USER MODEL>)

For this reason, we cannot just put all the extensions in a list.

INSTRUCTIONS FOR USING A NEW EXTENSION:
1. Initialize here
2. Import the extension into project/__init__.py
3. Find the initialize_extensions() method
4. Write corresponding logic to initialize
"""

from flask_sqlalchemy import SQLAlchemy

# INSTANCES:
db = SQLAlchemy()
