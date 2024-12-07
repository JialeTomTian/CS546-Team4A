void SetValue(string name, int value)
{
  switch (name)
  {
    case "height":
      height = value;
      break;
    case "width":
      width = value;
      break;
    default:
      Assert.Fail();
      break;
  }
}
