class Bird {
  //...
  getSpeed(): number {
    switch (this.type) {
      case BirdType.EUROPEAN:
        return this.getBaseSpeed();
      case BirdType.AFRICAN:
        return this.getBaseSpeed() - this.getLoadFactor() * this.numberOfCoconuts;
      case BirdType.NORWEGIAN_BLUE:
        return (this.isNailed)? 0 : this.getBaseSpeed(this.voltage);
    }
    throw new Error("Should be unreachable");
  }
}
