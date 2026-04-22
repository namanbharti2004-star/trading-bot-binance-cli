import argparse
import threading
from datetime import datetime
from colorama import Fore, init

from bot.orders import place_order, simulate_live_price, running
from bot.logging_config import setup_logging

init(autoreset=True)


# ===== UI =====
def header():
    print(Fore.CYAN + "=" * 35)
    print(Fore.GREEN + "   📈 TRADING TERMINAL v1.0")
    print(Fore.CYAN + "=" * 35)


def menu():
    print(Fore.YELLOW + "\n1. MARKET ORDER")
    print("2. LIMIT ORDER")
    print("3. EXIT")
    print(Fore.CYAN + "-" * 35)


def print_time():
    print(Fore.MAGENTA + f"\n🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def print_box(symbol, side, order_type, quantity, order):
    print(Fore.GREEN + "\n+-------------------------------+")
    print("|        ORDER RESULT           |")
    print("+-------------------------------+")
    print(f"| Symbol      : {symbol:<14}|")
    print(f"| Side        : {side:<14}|")
    print(f"| Type        : {order_type:<14}|")
    print(f"| Status      : {order.get('status'):<14}|")
    print(f"| Quantity    : {quantity:<14}|")
    print(f"| Avg Price   : {order.get('avgPrice'):<14}|")
    print("+-------------------------------+")


def print_error(msg):
    print(Fore.RED + "\n+-------------------------------+")
    print("|          ERROR ❌             |")
    print("+-------------------------------+")
    print(f"| {msg}")
    print("+-------------------------------+")


# ===== MENU MODE =====
def menu_mode():
    global running

    # start live price thread
    price_thread = threading.Thread(target=simulate_live_price)
    price_thread.daemon = True
    price_thread.start()

    while True:
        print("\n\n")
        header()
        print_time()
        menu()

        choice = input("Select option: ")

        if choice == "1":
            symbol = input("Symbol (BTCUSDT): ")
            side = input("Side (BUY/SELL): ").upper()
            quantity = float(input("Quantity: "))

            order = place_order(symbol, side, "MARKET", quantity)

            if "error" in order:
                print_error(order["error"])
            else:
                print_box(symbol, side, "MARKET", quantity, order)

        elif choice == "2":
            symbol = input("Symbol (BTCUSDT): ")
            side = input("Side (BUY/SELL): ").upper()
            quantity = float(input("Quantity: "))
            price = float(input("Price: "))

            order = place_order(symbol, side, "LIMIT", quantity, price)

            if "error" in order:
                print_error(order["error"])
            else:
                print_box(symbol, side, "LIMIT", quantity, order)

        elif choice == "3":
            running = False
            print(Fore.CYAN + "\n👋 Exiting Terminal")
            break

        else:
            print(Fore.RED + "Invalid choice")


# ===== CLI MODE =====
def cli_mode(args):
    header()
    print_time()

    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    if "error" in order:
        print_error(order["error"])
    else:
        print_box(args.symbol, args.side, args.type, args.quantity, order)


# ===== MAIN =====
def main():
    setup_logging()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol")
    parser.add_argument("--side", choices=["BUY", "SELL"])
    parser.add_argument("--type", choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    if not any(vars(args).values()):
        menu_mode()
    else:
        cli_mode(args)


if __name__ == "__main__":
    main()
