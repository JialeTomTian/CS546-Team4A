def calculateTotal():
    basePrice = quantity * itemPrice
    discount = 0.95 if basePrice > 1000 else 0.98
    return basePrice * discount
