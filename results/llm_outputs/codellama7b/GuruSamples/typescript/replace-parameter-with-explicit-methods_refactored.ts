setValue(name: string, value: number): void {
  switch (name) {
    case "height":
      height = value;
      break;
    case "width":
      width = value;
      break;
    default:
      break;
  }
}
