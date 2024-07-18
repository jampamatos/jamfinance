import pytest
from scripts.data_collector import get_realtime_data, get_historical_data

def test_get_realtime_data_valid():
    """Test the realtime data collection from Alpha Vantage with valid symbol."""
    data = get_realtime_data('AAPL')
    assert 'Time Series (5min)' in data, "Data should contain 'Time Series (5min)' key"

def test_get_realtime_data_invalid():
    """Test the realtime data collection from Alpha Vantage with invalid symbol."""
    with pytest.raises(ValueError):
        get_realtime_data('123')

def test_get_historical_data_valid():
    """Test the historical data collection from yfinance with valid symbol."""
    data = get_historical_data('AAPL')
    assert not data.empty, 'The dataframe should not be empty'

def test_get_historical_data_invalid():
    """Test the historical data collection from yfinance with invalid symbol."""
    with pytest.raises(ValueError):
        get_historical_data('123')

if __name__ == '__main__':
    pytest.main()
