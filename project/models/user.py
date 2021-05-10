"""
Sample User model using SQL Alchemy.

To be used with SQL database of your choice.
"""

from datetime import datetime
from project.all_extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # *****************************
    # METHODS:
    # *****************************

    @property
    def identity(self):
        """
        Provides unique id of the user instance.
        """
        return self.id
