double getExpenseLimit() {
  return expenseLimit!= NULL_EXPENSE? expenseLimit : primaryProject.getMemberExpenseLimit();
}