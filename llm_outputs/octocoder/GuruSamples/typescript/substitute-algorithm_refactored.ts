function foundPerson(people: string[]): string {
  for (let person of people) {
    if (person === "Don") {
      return "Don";
    }
    if (person === "John") {
      return "John";
    }
    if (person === "Kent") {
      return "Kent";
    }
  }
  return "";
}