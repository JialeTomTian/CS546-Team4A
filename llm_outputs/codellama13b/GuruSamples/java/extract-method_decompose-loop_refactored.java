void printProperties(List users) {
  for (User user : users) {
    String result = user.getName() + " " + user.getAge();
    System.out.println(result);
  }
}