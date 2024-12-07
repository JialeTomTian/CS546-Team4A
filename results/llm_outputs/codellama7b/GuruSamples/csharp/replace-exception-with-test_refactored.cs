double GetValueForPeriod(int periodNumber)
{
  return values.TryGetValue(periodNumber, out var value)? value : 0;
}
