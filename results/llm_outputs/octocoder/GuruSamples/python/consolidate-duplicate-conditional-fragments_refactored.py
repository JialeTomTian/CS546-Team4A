def send_discounted_price(price):
    if is_special_deal():
        total = price * 0.95
        send()
    else:
        total = price * 0.98
        send()
