void setValue(String name, int value) {
  switch (name) {
    case "height":
      height = value;
      break;
    case "width":
      width = value;
      break;
    default:
      Assert.shouldNeverReachHere();
      break;
  }
}