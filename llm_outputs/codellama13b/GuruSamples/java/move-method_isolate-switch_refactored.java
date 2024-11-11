class Order {
  //...

  public double calculateTotal() {
    double total = 0;
    for (Product product : getProducts()) {
      total += product.quantity * product.price;
    }
    total = applyRegionalDiscounts(total);
    return total;
  }

  public double applyRegionalDiscounts(double total) {
    double result = total;
    switch (user.getCountry()) {
      case "US": result *= 0.85; break;
      case "RU": result *= 0.75; break;
      case "CN": result *= 0.9; break;
      //...
    }
    return result;
  }

  private double getDiscountFactor(String country) {
    switch (country) {
      case "US": return 0.85;
      case "RU": return 0.75;
      case "CN": return 0.9;
      //...
    }
    return 1;
  }

  public double calculateTotalWithDiscounts() {
    double total = 0;
    for (Product product : getProducts()) {
      total += product.quantity * product.price;
    }
    return total * getDiscountFactor(user.getCountry());
  }
}