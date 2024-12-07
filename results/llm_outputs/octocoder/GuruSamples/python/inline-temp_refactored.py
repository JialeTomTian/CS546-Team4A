def has_discount(order):
    base_price = order.base_price()
    return base_price > 1000
