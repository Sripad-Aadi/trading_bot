# Binance Futures Testnet Trading Bot (Python)

## Overview

This is a command-line trading bot built in Python that places **Market** and **Limit** orders on **Binance Futures Testnet (USDT-M)**.

The project demonstrates:

- Structured code organization
- Manual HMAC request signing
- Input validation
- Logging to file
- Exception handling
- Clean CLI interface

All orders are placed on Binance Futures **Testnet (Demo Trading)** — no real funds are used.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Support both BUY and SELL
- CLI-based input using Click
- Validation for symbol, side, order type, quantity, and price
- Logs API requests and responses
- Handles API and network errors

---

## Project Structure

trading_bot/
│
├── bot/
│   ├── api.py          # Binance API interaction (signed requests)
│   ├── config.py       # Logging configuration
│   ├── validators.py   # Input validation
│
├── cli.py              # CLI entry point
├── requirements.txt
├── README.md
└── logs/

---

## Requirements

- Python 3.8+
- Binance Futures Testnet account
- API Key and Secret (Futures permission enabled)

---

## Setup Instructions

### 1. Clone or Download Repository

git clone <your-repo-link>
cd trading_bot


### 2. Create Virtual Environment

    python -m venv venv


### 3. Activate Virtual Environment

    Windows:
    venv\Scripts\activate

Linux/Mac:
    source venv/bin/activate


### 4. Install Dependencies

    pip install -r requirements.txt


    .env

Create a file named `.env` in the project root:

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

## Example Output

Placing BUY MARKET order for 0.001 BTCUSDT

ORDER PLACED SUCCESSFULLY
Order ID: 123456789
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Status: FILLED
Quantity: 0.001
Executed Qty: 0.001
Average Price: 64998


---

## Logging

Logs are written to:

    logs/app.log


The log file contains:
- Order request parameters
- API responses
- Validation errors
- Network/API failures

---

## Assumptions

- User has a Binance Futures Testnet account
- API keys are valid and have Futures trading permission enabled
- Quantity and price respect Binance lot size rules
- Internet connection is available

---

## Design Notes

- Synchronous REST implementation
- Manual request signing using HMAC SHA256
- Time synchronization with Binance server
- Modular code structure (API layer separated from CLI layer)
- Built for evaluation and learning purposes

---

## Author

Python Developer Internship Assignment Submission
