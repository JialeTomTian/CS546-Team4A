withdraw(amount: number): number {
  if (amount > _balance) {
    return -1;
  }
  else {
    _balance -= amount;
    return 0;
  }
}