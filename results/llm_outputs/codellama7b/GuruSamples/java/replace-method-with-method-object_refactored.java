class Order {
  //...
  public double price() {
    double primaryBasePrice = computeBasePrice(primary);
    double secondaryBasePrice = computeBasePrice(secondary);
    double tertiaryBasePrice = computeBasePrice(tertiary);
    // Perform long computation.
  }

  private double computeBasePrice(Product product) {
    // Perform long computation.
  }
}
