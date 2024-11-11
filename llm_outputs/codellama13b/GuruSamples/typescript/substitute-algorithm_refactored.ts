foundPerson(people: string[]): string{
  for (let person of people) {
    if (person === "Don" || person === "John" || person === "Kent"){
      return person;
    }
  }
  return "";
}