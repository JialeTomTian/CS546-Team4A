double DisabilityAmount() 
{
  if (seniority < 2 || monthsDisabled > 12 || isPartTime) 
  {
    return 0;
  }
  // Compute the disability amount.
  //...
}