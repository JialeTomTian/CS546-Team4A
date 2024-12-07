base_price = quantity * item_price
seasonal_discount = self.get_seasonal_discount()
fees = self.get_fees()
final_price = discounted_price(base_price, seasonal_discount, fees)
