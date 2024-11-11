discount(inputVal: number, quantity: number): number {
  const discountAmount = quantity > 50? 2 : 0;
  return inputVal - discountAmount;
}