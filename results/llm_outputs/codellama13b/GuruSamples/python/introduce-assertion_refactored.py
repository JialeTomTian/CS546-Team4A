def getExpenseLimit(self):
    return self.expenseLimit or self.primaryProject.getMemberExpenseLimit()
