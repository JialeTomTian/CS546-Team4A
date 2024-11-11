public class Order 
{
  //...
  public double Price() 
  {
    double primaryBasePrice = ComputeBasePrice(primary);
    double secondaryBasePrice = ComputeBasePrice(secondary);
    double tertiaryBasePrice = ComputeBasePrice(tertiary);
    // Perform long computation.
  }

  private double ComputeBasePrice(OrderItem item)
  {
    // Perform long computation.
  }
}