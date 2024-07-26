from flask import Flask, request, jsonify
import pandas as pd
from scripts.trading_logic import determine_trade_signals

app = Flask(__name__)

@app.route('/api/trading_decision', methods=['POST'])
def trading_decision():
    data = request.get_json()
    if not data or 'data' not in data: return jsonify({'error': 'No data provided'}), 400
    
    df = pd.DataFrame(data['data'])
    try:
        signals = determine_trade_signals(df)
        return jsonify(signals.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)