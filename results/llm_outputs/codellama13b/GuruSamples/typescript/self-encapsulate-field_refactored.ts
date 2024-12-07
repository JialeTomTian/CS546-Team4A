class Range {
  private low: number;
  private high: number;

  constructor(low: number, high: number) {
    this.low = low;
    this.high = high;
  }

  includes(arg: number): boolean {
    return arg >= this.low && arg <= this.high;
  }
}
