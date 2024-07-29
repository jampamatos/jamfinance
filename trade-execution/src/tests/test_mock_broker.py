import pytest
import sys
sys.path.append('/home/jampamatos/jamfinance/trade-execution/src/scripts')
from mock_broker import place_order, check_order_status

def test_place_order():
    """Test placing an order. As the success is randomly determined, this test may need to handle both outcomes"""
    response = place_order('AAPL', 100, 'buy')
    assert response['status'] in ['success', 'failed'], "The order should either succeed or fail."

def test_check_order_status():
    """Test checking the status of an order."""
    order_id = '123456'
    status = check_order_status(order_id)
    assert status['status'] == 'completed', "The order status should be completed."
    assert status['order_id'] == order_id, "The order ID should match the requested ID."