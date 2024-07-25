import pytest
from flask import json

from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app
    
@pytest.fixture
def client(app):
    return app.test_client()

def test_realtime_data(client):
    """Test the realtime data endpoint with a valid symbol."""
    response = client.get('/api/realtime/AAPL')
    assert response.status_code == 200
    assert 'Time Series (5min)' in json.loads(response.data)
    
def test_historical_data(client):
    """Test the historical data endpoint with a valid symbol."""
    response = client.get('/api/historical/AAPL')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data
    
def test_realtime_data_invalid(client):
    """Test the realtime data endpoint with an invalid symbol."""
    response = client.get('/api/realtime/INVALID')
    assert response.status_code == 500

def test_historical_data_invalid(client):
    """Test the historical data endpoint with an invalid symbol."""
    response = client.get('/api/historical/INVALID')
    assert response.status_code == 500