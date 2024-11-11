getExpenseLimit(): number {
  return expenseLimit?? primaryProject.getMemberExpenseLimit();
}