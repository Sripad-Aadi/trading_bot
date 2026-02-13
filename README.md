# Binance Futures Testnet Trading Bot (Python)

A simple command-line trading bot built in Python that places Market and Limit orders on Binance Futures Testnet (USDT-M).  
The project demonstrates clean code structure, input validation, logging, and proper error handling.

---

## Features

- Place MARKET and LIMIT orders
- Supports BUY and SELL
- Works on Binance Futures Testnet (USDT-M)
- Command-line interface using Click
- Input validation
- Structured project layout
- Logs API requests, responses, and errors to file
- Handles API and network exceptions

---

## Project Structure

trading_bot/
│
├── bot/
│   ├── api.py
│   ├── config.py
│   ├── validators.py
│
├── cli.py
├── requirements.txt
├── README.md
└── logs/
    ├── app.log

---

## Prerequisites

- Python 3.8 or higher
- Binance Futures Testnet account
- API Key and Secret from Binance Futures Testnet

---

## Setup Steps

1. Clone or download the repository

2. Create virtual environment

python -m venv venv

3. Activate virtual environment

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Create a `.env` file in project root

.env

Add:

API_KEY=your_api_key_here  
API_SECRET=your_api_secret_here  
BASE_URL=https://testnet.binancefuture.com

---

## How to Run

### Place Market Order

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

### Place Limit Order

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 65000

---

## Sample Output

Placing BUY MARKET order for 0.001 BTCUSDT

ORDER PLACED SUCCESSFULLY  
Order ID: 123456  
Symbol: BTCUSDT  
Side: BUY  
Type: MARKET  
Status: FILLED  
Quantity: 0.001  
Executed Qty: 0.001  
Average Price: 64995  

---

## Logs

Logs are written to:

logs/app.log

Includes:

- Order request parameters  
- API responses  
- Validation errors  
- Network errors  

---

## Assumptions

- User already has a Binance Futures Testnet account
- API keys have Futures trading permission enabled
- Quantities and prices follow Binance lot size rules
- Internet connection is available

---

## Notes

- This project uses synchronous REST API calls
- Orders are placed only on testnet (no real funds)
- Intended for educational and evaluation purposes

---
