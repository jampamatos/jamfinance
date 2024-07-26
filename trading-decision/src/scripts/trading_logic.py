import pandas as pd

def calculate_moving_average(data, window_size):
    """
    Calculates moving average of closing values.
    """
    return data['close'].rolling(window=window_size).mean()

def calculate_rsi(data, window_size=14):
    """
    Calculates RSI (Relative Strenght Index).
    """
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window_size).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window_size).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

import pandas as pd

def calculate_moving_average(data, window_size):
    """
    Calculates moving average of closing values.
    """
    return data['Close'].rolling(window=window_size).mean()

def calculate_rsi(data, window_size=14):
    """
    Calculates RSI (Relative Strenght Index).
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window_size).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window_size).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

def determine_trade_signals(data, short_window=1, long_window=2):
    """
    Determines trade signals based on moving averages and RSI.
    """
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    
    # Moving averages
    signals['short_mavg'] = calculate_moving_average(data, short_window)
    signals['long_mavg'] = calculate_moving_average(data, long_window)
    
    # RSI
    signals['rsi'] = calculate_rsi(data)
    
    # Buy signal when the short moving average crosses above the long one and RSI < 30
    buy_signals = (signals['short_mavg'] > signals['long_mavg']) & (signals['rsi'] < 30)
    signals.loc[buy_signals, 'signal'] = 1.0
    
    # Sell signal when the short moving average crosses below the long one and RSI > 70
    sell_signals = (signals['short_mavg'] < signals['long_mavg']) & (signals['rsi'] > 70)
    signals.loc[sell_signals, 'signal'] = -1.0
    
    # Generate positions based on signals
    signals['positions'] = signals['signal'].diff()
    
    return signals
