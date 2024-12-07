class PizzaDelivery {
  //...
  getRating(): number {
    return this.numberOfLateDeliveries > 5? 2 : 1;
  }
}
