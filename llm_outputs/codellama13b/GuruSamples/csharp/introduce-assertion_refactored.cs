double GetExpenseLimit() 
{
  return expenseLimit?? primaryProject.GetMemberExpenseLimit();
}