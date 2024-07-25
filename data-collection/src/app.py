from flask import Flask, jsonify
from scripts.data_collector import get_realtime_data, get_historical_data

app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to the Jamfinance Data Collection Service!'

@app.route('/api/realtime/<sym>', methods=['GET'])
def realtime_data(sym):
  """
  Endpoint to get real-time data for a specific stock symbol.
  :param sym: String, ticker symbol of the action.
  :return: JSON, real-time data of the specified action.
  """
  return jsonify(get_realtime_data(sym))
  
@app.route('/api/historical/<sym>', methods=['GET'])
def historical_data(sym):
  """
  Endpoint to get historical data for a specific stock symbol.
  :param sym: String, ticker symbol of the action.
  :return: JSON, historical data of the specified action in JSON format.
  """
  data = get_historical_data(sym)
  json_data = data.to_json(date_format='iso', orient='split')
  return json_data  
  
@app.errorhandler(Exception)
def handle_exception(e):
  """Handle general exceptions."""
  return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')