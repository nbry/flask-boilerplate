import pytest
from project import create_app


@pytest.fixture(scope="module")
def app():
    flask_app = create_app('testing.cfg')
    yield flask_app


@pytest.fixture(scope="module")
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client
