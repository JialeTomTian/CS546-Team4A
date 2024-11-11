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
    double discount = 1;
    switch (user.getCountry()) {
      case "US": discount = 0.85; break;
      case "RU": discount = 0.75; break;
      case "CN": discount = 0.9; break;
      //...
    }
    return total * discount;
  }