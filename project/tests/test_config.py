"""
Yo dawg I heard you like tests, so...

test_config.py tests the instance config settings for the different environments:
1. development
2. production
3. testing
"""
from project import create_app


def test_testing_config():
    """
    GIVEN an instance of create_app named "app"
    WHEN app is given TESTING configuration settings from instance/testing.cfg
    THEN app should have the expected config settings
    NOTE: This test also acts as a functional test for the project's create_app function
    """
    app = create_app('testing.cfg')

    # app should have DEBUG configuration
    assert app.config['DEBUG']


def test_development_config():
    """
    GIVEN an instance of create_app named app
    WHEN app is given DEVELOPMENT configuration settings from instance/development.cfg
    THEN app should have the expected config settings
    NOTE: This test also acts as a functional test for the project's create_app function
    """
    app = create_app('development.cfg')
