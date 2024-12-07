class Order {
  //...

  public double calculateTotal() {
    double total = 0;
    for (Product product : getProducts()) {
      total += product.quantity * product.price;
    }

    // Apply regional discounts.
    total *= getDiscountFactor(user.getCountry());

    return total;
  }

  private double getDiscountFactor(String country) {
    switch (country) {
      case "US": return 0.85;
      case "RU": return 0.75;
      case "CN": return 0.9;
      //...
      default: return 1.0;
    }
  }
}
