#  Trading Bot – Binance Futures (Simulated)

##  Overview
A CLI-based trading bot that simulates placing MARKET and LIMIT orders on Binance Futures.

---

## Features
- MARKET & LIMIT orders
- BUY / SELL support
- CLI + Menu UI
- Live price simulation
- Logging & error handling

---

## ⚙ Setup

pip install -r requirements.txt

---

## ▶ Run

### Interactive mode
python cli.py

### MARKET order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

---

## 📊 Logs
Check bot.log file

---

##  Note
Orders are simulated due to testnet restrictions. The code is structured to support real Binance API integration with minimal changes.
