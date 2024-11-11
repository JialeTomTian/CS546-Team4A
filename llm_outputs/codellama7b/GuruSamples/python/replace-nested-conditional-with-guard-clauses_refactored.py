def getPayAmount(self):
    if self.isDead:
        return deadAmount()
    elif self.isSeparated:
        return separatedAmount()
    elif self.isRetired:
        return retiredAmount()
    else:
        return normalPayAmount()