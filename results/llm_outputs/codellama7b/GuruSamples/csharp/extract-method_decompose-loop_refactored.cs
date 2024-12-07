void printProperties(IList users)
{
  for (int i = 0; i < users.size(); i++)
  {
    string result = users.get(i).getName() + " " + users.get(i).getAge();
    Console.WriteLine(result);

    //...
  }
}
