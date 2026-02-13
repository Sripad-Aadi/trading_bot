import os
import time
import hmac
import hashlib
import logging
from urllib.parse import urlencode
from dotenv import load_dotenv
import requests

load_dotenv()


def get_base_url():
    return os.getenv("BASE_URL", "https://testnet.binancefuture.com")


def get_api_credentials():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    
    if not api_key or not api_secret:
        raise ValueError("API_KEY and API_SECRET must be set in .env")
    
    return api_key, api_secret


def get_server_time():
    #Fetching current server time from binance
    base_url = get_base_url()
    try:
        resp = requests.get(f"{base_url}/fapi/v1/time")
        resp.raise_for_status()
        return int(resp.json().get("serverTime"))
    except Exception as e:
        logging.error(f"Failed to fetch server time: {e}")
        #If failed to fetch server time, use local time
        return int(time.time() * 1000)


def _sign_request(params, api_secret):
    query = urlencode(params)
    signature = hmac.new(
        api_secret.encode("utf-8"),
        query.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()
    return f"{query}&signature={signature}"


def _send_signed_request(method, path, params, api_key, api_secret):
    base_url = get_base_url()
    url = base_url.rstrip("/") + path
    signed_query = _sign_request(params, api_secret)
    headers = {"X-MBX-APIKEY": api_key}
    
    try:
        if method.upper() == "POST":
            resp = requests.post(url, params=signed_query, headers=headers)
        else:
            resp = requests.get(url, params=signed_query, headers=headers)
        
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        try:
            error_data = e.response.json()
            raise Exception(f"API error: {error_data}")
        except Exception:
            raise Exception(f"Request failed: {e}")


def place_market_order(symbol, side, quantity):
    api_key, api_secret = get_api_credentials()
    timestamp = get_server_time()
    
    params = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity,
        "timestamp": timestamp,
        "recvWindow": 60000,
    }
    
    logging.info(f"Placing MARKET order: {params}")
    result = _send_signed_request("POST", "/fapi/v1/order", params, api_key, api_secret)
    logging.info(f"Order response: {result}")
    return result


def place_limit_order(symbol, side, quantity, price):
    api_key, api_secret = get_api_credentials()
    timestamp = get_server_time()
    
    params = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": quantity,
        "price": price,
        "timestamp": timestamp,
        "recvWindow": 60000,
    }
    
    logging.info(f"Placing LIMIT order: {params}")
    result = _send_signed_request("POST", "/fapi/v1/order", params, api_key, api_secret)
    logging.info(f"Order response: {result}")
    return result
