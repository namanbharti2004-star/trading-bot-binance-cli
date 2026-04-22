# Trading Bot – Binance Futures (Simulated)

## Overview
A CLI-based trading bot that simulates placing MARKET and LIMIT orders on Binance Futures.

The application is designed with a clean, modular architecture including logging, validation, and an interactive terminal UI.

---

## Features
- Place MARKET and LIMIT orders  
- Supports BUY and SELL  
- CLI-based interface (argparse)  
- Interactive terminal menu UI  
- Live price simulation 📈  
- Colored output for better UX  
- Logging of requests and responses  
- Input validation and error handling  

---

## Setup
```bash
pip install -r requirements.txt
```

---

## Run

### Interactive Mode
```bash
python cli.py
```

### MARKET Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## Logs
Check `bot.log` file for request/response details.

---

## Project Structure
```bash
trading-bot/
│── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── __init__.py
│
│── cli.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## Note
Orders are simulated due to testnet restrictions.  
The code is structured to support real Binance API integration with minimal changes.

---

## Future Improvements
- Connect to Binance Futures Testnet API  
- Add stop-loss / take-profit  
- Add strategy-based trading  
- Add web dashboard (Flask/React)  
