class PizzaDelivery:
    # ...
    def getRating(self):
        return 2 if self.numberOfLateDeliveries > 5 else 1

    def moreThanFiveLateDeliveries(self):
        return self.numberOfLateDeliveries > 5
