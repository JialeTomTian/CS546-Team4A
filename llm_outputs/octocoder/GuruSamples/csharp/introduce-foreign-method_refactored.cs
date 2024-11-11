 Here is the refactored code:

class Report 
{
  //...
  void SendReport() 
  {
    DateTime nextDay = previousEnd.AddDays(1);
    //...
  }
}