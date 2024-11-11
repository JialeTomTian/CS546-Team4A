String foundPerson(String[] people){
  for (String person : people) {
    if (person.equals("Don") || person.equals("John") || person.equals("Kent")){
      return person;
    }
  }
  return "";
}