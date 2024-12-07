setValue(name: string, value: number): void {
  if (name === "height") {
    height = value;
    return;
  }
  if (name === "width") {
    width = value;
    return;
  }
}
