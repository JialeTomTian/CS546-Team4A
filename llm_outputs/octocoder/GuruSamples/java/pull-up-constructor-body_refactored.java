 Here is the refactored code:

class Manager extends Employee {
  public Manager(String name, String id, int grade) {
    super(name, id, grade);
  }
  //...
}

The code has been refactored to use the super keyword to call the constructor of the parent class. This improves readability and maintainability by eliminating the need to repeat the name, id, and grade parameters in the constructor. It also improves performance by eliminating the need to call the parent class constructor multiple times.