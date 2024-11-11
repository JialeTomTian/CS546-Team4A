class Bird:
    #...
    def getSpeed(self):
        if self.type == EUROPEAN:
            return self.getBaseSpeed()
        elif self.type == AFRICAN:
            return self.getBaseSpeed() - self.getLoadFactor() * self.numberOfCoconuts
        elif self.type == NORWEGIAN_BLUE:
            return self.getBaseSpeed(self.voltage) if not self.isNailed else 0
        else:
            raise Exception("Should be unreachable")