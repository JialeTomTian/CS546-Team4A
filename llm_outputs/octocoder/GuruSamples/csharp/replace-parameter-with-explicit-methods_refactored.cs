void SetValue(string name, int value) 
{
  if (name == "height") 
  {
    height = value;
    return;
  }
  if (name == "width") 
  {
    width = value;
    return;
  }
  Assert.Fail();
}