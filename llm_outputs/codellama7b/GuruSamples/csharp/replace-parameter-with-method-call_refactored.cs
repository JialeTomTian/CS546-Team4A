int basePrice = quantity * itemPrice;
double seasonDiscount = GetSeasonalDiscount();
double fees = GetFees();
double finalPrice = DiscountedPrice(basePrice, seasonDiscount, fees);