def print_owing(self):
    self.print_banner()

    # print details
    print("name:", self.name)
    print("amount:", self.get_outstanding())
