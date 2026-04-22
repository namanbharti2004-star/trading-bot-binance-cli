import random
import time
import threading
import logging

# ===== LIVE PRICE =====
live_price = 60000
running = True

def simulate_live_price():
    global live_price, running
    while running:
        change = random.uniform(-50, 50)
        live_price = round(live_price + change, 2)
        arrow = "⬆" if change > 0 else "⬇"
        print(f"\r📈 BTCUSDT Price: {live_price} {arrow}", end="")
        time.sleep(1)

# ===== ORDER LOGIC =====
USE_REAL_API = False

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        time.sleep(1)

        if order_type == "LIMIT" and price is None:
            raise ValueError("Price required for LIMIT order")

        # MOCK RESPONSE
        order = {
            "orderId": random.randint(100000, 999999),
            "status": "FILLED" if order_type == "MARKET" else "NEW",
            "executedQty": quantity if order_type == "MARKET" else 0,
            "avgPrice": round(random.uniform(50000, 70000), 2) if order_type == "MARKET" else price
        }

        logging.info(f"Order placed: {order}")
        return order

    except Exception as e:
        logging.error(str(e))
        return {"error": str(e)}
