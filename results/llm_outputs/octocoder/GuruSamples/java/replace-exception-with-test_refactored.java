double getValueForPeriod(int periodNumber) {
  if (periodNumber < 0 || periodNumber >= values.length) {
    return 0;
  }
  return values[periodNumber];
}
