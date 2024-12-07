class Order {
  //...
  price(): number {
    const primaryBasePrice = this.computeBasePrice();
    const secondaryBasePrice = this.computeBasePrice();
    const tertiaryBasePrice = this.computeBasePrice();
    // Perform long computation.
  }

  private computeBasePrice(): number {
    // Perform long computation.
  }
}
