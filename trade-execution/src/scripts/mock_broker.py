import random

def place_order(sym, qtd, type):
    """Simulate placing an order at a brokerage."""
    print(f"Placing {'buy' if type == 'buy' else 'sell'} order for {qtd} shares of {sym}.")
    
    if random.choice([True, False]):
        return {
            'status': 'success',
            'order_id': f"{random.randint(100000, 999999)}",
            'messsage': f"Order to {'buy' if type == 'buy' else 'sell'} {qtd} shares of {sym} has been placed successfully."
        }
    else:
        return {
            'status': 'failed',
            'order_id': None,
            'message:': 'Failed to place order due to a technical issue.'
        }

def check_order_status(order_id):
    """Simulate checking the status of an order."""
    return{
        'order_id': order_id,
        'status': 'completed',
        'details': 'The order has been successfully executed.'
    }