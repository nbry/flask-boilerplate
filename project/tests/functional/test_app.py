"""
Testing factory pattern function: create_app()
and the default ping route.
"""

from project import create_app


def test_create_app():
    """
    GIVEN the create_app factory function
    WHEN the '/ping' page is requested (GET)
    THEN check that the response is valid
    """

    flask_app = create_app('testing.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/ping')
        assert response.status_code == 200
