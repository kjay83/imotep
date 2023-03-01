import pytest

from src.app import app


@pytest.fixture
def client():
    #app = create_app({"TESTING": True})
    #app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client