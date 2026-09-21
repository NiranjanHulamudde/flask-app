import pytest
from app import app

@pytest.fixture
def client():
    # Set up the Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    """Verify that the homepage loads with an HTTP 200 status code"""
    response = client.get('/')
    assert response.status_code == 200

def test_homepage_content(client):
    """Verify that the page contains our DevOps project title"""
    response = client.get('/')
    assert b"DevOps Portfolio Project" in response.data

