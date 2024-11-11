class Order {
  //...
  public double price() {
    double primaryBasePrice = computeBasePrice();
    double secondaryBasePrice = computeBasePrice();
    double tertiaryBasePrice = computeBasePrice();
    // Perform long computation.
  }

  private double computeBasePrice() {
    // Perform long computation.
    return basePrice;
  }
}