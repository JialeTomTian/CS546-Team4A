def withdraw(self, amount):
    if amount > self.balance:
        return -1
    self.balance -= amount
    return 0
