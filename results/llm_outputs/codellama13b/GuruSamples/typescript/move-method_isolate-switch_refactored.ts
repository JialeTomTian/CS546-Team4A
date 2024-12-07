class Order {
  //...

  calculateTotal(): number {
    let total = 0;
    for (let product : getProducts()) {
      total += product.quantity * product.price;
    }
    total = applyRegionalDiscounts(total);
    return total;
  }

  applyRegionalDiscounts(total: number): number {
    let discount = 0;
    switch (user.getCountry()) {
      case "US": discount = 0.85; break;
      case "RU": discount = 0.75; break;
      case "CN": discount = 0.9; break;
      //...
    }
    return total * (1 - discount);
  }
}
