import pandas as pd
import pytest
import sys
sys.path.append('/home/jampamatos/jamfinance/trading-decision/src/scripts')
from datetime import datetime
from trading_logic import determine_trade_signals, calculate_moving_average, calculate_rsi

@pytest.fixture
def sample_data():
    """Generates sample data to test trading logic"""
    dates = pd.date_range(start='2022-01-01', periods=100, freq='D')
    prices = [100 + (i * 0.5 if i < 50 else 50 * 0.5 - (i - 50) * 0.5) for i in range(100)]  # Preços sobem e depois descem
    data = pd.DataFrame(data={'Close': prices}, index=dates)
    return data

def test_calculate_moving_average(sample_data):
    """Tests if moving averages is working as intended."""
    moving_avg = calculate_moving_average(sample_data, 10)
    assert moving_avg.iloc[9] == pytest.approx(102.25)  # Corrigido para o valor correto
    
def test_calculate_rsi(sample_data):
    """Tests if RSI is woring as intended."""
    rsi = calculate_rsi(sample_data)
    assert rsi.iloc[14] > 0 # Check if RSI starts being generated correctly after startingf period.
    
def test_determine_trade_signals(sample_data):
    """Tests if trading signals are being generated correctly."""
    signals = determine_trade_signals(sample_data)
    print("RSI:\n", signals['rsi'])
    print("Short MAVG:\n", signals['short_mavg'])
    print("Long MAVG:\n", signals['long_mavg'])
    print("Signals:\n", signals['signal'])
    assert any(signals['signal'] != 0)

