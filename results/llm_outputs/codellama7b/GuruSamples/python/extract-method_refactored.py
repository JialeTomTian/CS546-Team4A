def printOwing(self):
    self.printBanner()

    # print details
    print("name:", self.name)
    print("amount:", self.getOutstanding())

    # print owing
    print("owing:", self.getOutstanding())
