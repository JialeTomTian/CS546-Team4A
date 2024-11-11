class Order {
  //...

  calculateTotal(): number {
    let total = 0;
    for (let product : getProducts()) {
      total += product.quantity * product.price;
    }

    // Apply regional discounts.
    total *= getDiscountFactor(user.getCountry());

    return total;
  }

  private getDiscountFactor(country: string): number {
    switch (country) {
      case "US": return 0.85;
      case "RU": return 0.75;
      case "CN": return 0.9;
      //...
    }
  }
}