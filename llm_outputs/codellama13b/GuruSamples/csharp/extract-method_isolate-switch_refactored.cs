class Order
{
  //...

  public double calculateTotal()
  {
    double total = 0;
    foreach (Product product in getProducts())
    {
      total += product.quantity * product.price;
    }

    // Apply regional discounts.
    total *= getDiscountFactor(user.getCountry());

    return total;
  }

  private double getDiscountFactor(string country)
  {
    switch (country)
    {
      case "US": return 0.85;
      case "RU": return 0.75;
      case "CN": return 0.9;
      //...
    }
  }
}