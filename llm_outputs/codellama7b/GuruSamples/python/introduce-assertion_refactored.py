def getExpenseLimit(self):
    if self.expenseLimit!= NULL_EXPENSE:
        return self.expenseLimit
    elif self.primaryProject:
        return self.primaryProject.getMemberExpenseLimit()
    else:
        return NULL_EXPENSE