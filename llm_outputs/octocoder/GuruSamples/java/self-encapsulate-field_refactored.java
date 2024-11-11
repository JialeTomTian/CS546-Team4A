class Range {
  private final int low, high;

  Range(int low, int high) {
    this.low = low;
    this.high = high;
  }

  boolean includes(int arg) {
    return arg >= low && arg <= high;
  }
}