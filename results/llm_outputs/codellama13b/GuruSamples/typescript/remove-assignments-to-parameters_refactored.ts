discount(inputVal: number, quantity: number): number {
  return inputVal - (quantity > 50? 2 : 0);
}
