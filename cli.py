#CLI for placing orders
import click
import logging

from bot.config import setup_logger
from bot.validators import (
    validate_symbol, validate_side, validate_order_type,
    validate_quantity, validate_price
)

from bot.api import place_market_order, place_limit_order

setup_logger()

def format_order_response(response):
    lines = [
        "ORDER PLACED SUCCESSFULLY",
        f"Order ID:        {response.get('orderId')}",
        f"Symbol:          {response.get('symbol')}",
        f"Side:            {response.get('side')}",
        f"Type:            {response.get('type')}",
        f"Status:          {response.get('status')}",
        f"Quantity:        {response.get('origQty')}",
        f"Executed Qty:    {response.get('executedQty')}",
        f"Average Price:   {response.get('avgPrice')}",
        "\n",
    ]
    return "\n".join(lines)


@click.command()
@click.option("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
@click.option("--side", required=True, help="Order side: BUY or SELL")
@click.option("--order_type", required=True, help="Order type: MARKET or LIMIT")
@click.option("--quantity", required=True, type=float, help="Order quantity")
@click.option("--price", required=False, type=float, help="Price (required for LIMIT orders)")

def main(symbol, side, order_type, quantity, price):
    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        
        #order validation
        if order_type == "LIMIT" and price is None:
            raise ValueError("Price is required for LIMIT orders")
        
        if order_type == "LIMIT":
            price = validate_price(price)
        
        #log request summary
        logging.info(f"Order request: symbol={symbol}, side={side}, type={order_type}, qty={quantity}, price={price if order_type == 'LIMIT' else 'N/A'}")
        print(f"\nPlacing {side} {order_type} order for {quantity} {symbol}" + (f" at {price}" if order_type == "LIMIT" else ""))
        
        #place order
        if order_type == "MARKET":
            response = place_market_order(symbol, side, quantity)
        else:
            response = place_limit_order(symbol, side, quantity, price)
        
        print(format_order_response(response))
        logging.info(f"Order placed successfully: {response}")
        
    except ValueError as e:
        msg = f"Input validation error: {e}"
        logging.error(msg)
        print(f"{msg}\n")
        raise SystemExit(1)
    except Exception as e:
        msg = f"Order placement failed: {e}"
        logging.error(msg)
        print(f"{msg}\n")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
