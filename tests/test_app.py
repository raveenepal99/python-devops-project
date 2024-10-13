import sys
import os

# Append the parent directory to the system path so that `app.py` can be imported.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app  # Now this should work without ModuleNotFoundError

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_increment(client):
    client.post('/increment')
    response = client.get('/')
    assert b'Counter Value: 1' in response.data

def test_decrement(client):
    client.post('/increment')  # Set counter to 1
    client.post('/decrement')
    response = client.get('/')
    assert b'Counter Value: 0' in response.data

def test_reset(client):
    client.post('/increment')  # Set counter to 1
    client.post('/reset')
    response = client.get('/')
    assert b'Counter Value: 0' in response.data
