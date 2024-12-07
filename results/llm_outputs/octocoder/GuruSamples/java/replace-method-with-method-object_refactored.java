class Order {
  //...
  public double price() {
    double primaryBasePrice = computePrimaryBasePrice();
    double secondaryBasePrice = computeSecondaryBasePrice();
    double tertiaryBasePrice = computeTertiaryBasePrice();
    // Perform long computation.
  }

  private double computePrimaryBasePrice() {
    //...
  }

  private double computeSecondaryBasePrice() {
    //...
  }

  private double computeTertiaryBasePrice() {
    //...
  }
}
