class Order {
  //...

  calculateTotal(): number {
    let total = 0;
    for (const product of this.getProducts()) {
      total += product.quantity * product.price;
    }

    // Apply regional discounts.
    switch (this.user.getCountry()) {
      case "US":
        total *= 0.85;
        break;
      case "RU":
        total *= 0.75;
        break;
      case "CN":
        total *= 0.9;
        break;
      //...
    }

    return total;
  }
}