string FoundPerson(string[] people)
{
  return people.FirstOrDefault(p => p.Equals("Don") || p.Equals("John") || p.Equals("Kent"));
}