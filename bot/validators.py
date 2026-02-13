def validate_symbol(symbol):
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a valid symbol in string (e.g., BTCUSDT)")
    return symbol.upper()


def validate_side(side):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_order_type(order_type):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type


def validate_quantity(quantity):
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0")
        return qty
    except (ValueError, TypeError):
        raise ValueError("Quantity must be a valid positive number")


def validate_price(price):
    try:
        p = float(price)
        if p <= 0:
            raise ValueError("Price must be greater than 0")
        return p
    except (ValueError, TypeError):
        raise ValueError("Price must be a valid positive number")
