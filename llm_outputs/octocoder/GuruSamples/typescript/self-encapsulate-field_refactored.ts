class Range {
  private _low: number;
  private _high: number;

  constructor(low: number, high: number) {
    this._low = low;
    this._high = high;
  }

  includes(arg: number): boolean {
    return arg >= this._low && arg <= this._high;
  }
}