from flask import Flask, request, jsonify
from scripts.mock_broker import place_order, check_order_status

app = Flask(__name__)

@app.route('/execute_order', methods=['POST'])
def execute_order():
    data = request.get_json()
    if not data or 'order_type' not in data or 'quantity' not in data or 'stock_symbol' not in data:
        return jsonify({'error': 'Missing data in request'}), 400
    
    result = place_order(data['stock_symbol'], data['quantity'], data['order_type'])
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5002)