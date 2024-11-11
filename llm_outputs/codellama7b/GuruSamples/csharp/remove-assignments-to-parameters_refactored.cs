int Discount(int inputVal, int quantity) 
{
  return inputVal - (quantity > 50? 2 : 0);
}