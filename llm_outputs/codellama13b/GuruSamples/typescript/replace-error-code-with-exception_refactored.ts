withdraw(amount: number): number {
  if (amount > _balance) {
    return -1;
  }
  balance -= amount;
  return 0;
}