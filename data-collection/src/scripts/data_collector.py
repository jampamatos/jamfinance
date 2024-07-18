import os
import requests
import yfinance as yf

def is_valid_symbol(sym):
    """Check if the stock symbol is valid (non-empty and uppercase)."""
    return isinstance(sym, str) and sym.isalpha() and sym == sym.upper()

def get_realtime_data(sym):
    """Fetch real-time data from Alpha Vantage."""
    if not is_valid_symbol(sym):
        raise ValueError(f"Invalid stock symbol: {sym}")
    
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={sym}&interval=5min&apikey={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError(f"API request failed with status {response.status_code}")
    
    data = response.json()
    if "Time Series (5min)" not in data:
        raise ValueError("Data format from API is unexpected or empty")
    
    return data

def get_historical_data(sym):
    """Fetch historical data from yfinance."""
    if not is_valid_symbol(sym):
        raise ValueError(f"Invalid stock symbol: {sym}")
    
    stock = yf.Ticker(sym)
    hist = stock.history(period='max')
    if hist.empty:
        raise ValueError("Received empty dataframe for historical data.")
    
    return hist
