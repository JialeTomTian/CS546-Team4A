class Range 
{
  private int low, high;
  
  bool Includes(int arg) 
  {
    return low <= arg && arg <= high;
  }
}