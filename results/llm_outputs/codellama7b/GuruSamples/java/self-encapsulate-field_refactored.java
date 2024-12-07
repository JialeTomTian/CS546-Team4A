class Range {
  private int low, high;
  boolean includes(int arg) {
    return low <= arg && arg <= high;
  }
}
