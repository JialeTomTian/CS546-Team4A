int basePrice = quantity * itemPrice;
double seasonDiscount = getSeasonalDiscount();
double fees = getFees();
double finalPrice = discountedPrice(basePrice, seasonDiscount, fees);