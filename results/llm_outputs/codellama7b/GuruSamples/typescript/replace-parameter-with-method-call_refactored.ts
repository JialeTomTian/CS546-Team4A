let basePrice = quantity * itemPrice;
const seasonDiscount = this.getSeasonalDiscount();
const fees = this.getFees();
const finalPrice = basePrice * (1 - seasonDiscount) * (1 - fees);
