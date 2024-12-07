void printProperties(List<User> users) {
  for (User user : users) {
    String result = user.getName() + " " + user.getAge();
    System.out.println(result);

    //...
  }
}
