 The following is a refactored version of the code provided:

<?php
class Manager extends Employee {
  public function __construct($name, $id, $grade) {
    $this->name = $name;
    $this->id = $id;
    $this->grade = $grade;
  }

  public function getGrade() {
    return $this->grade;
  }
}

The refactored code improves readability, maintainability, and performance without changing functionality. The Manager class now has a getGrade() method that returns the grade of the manager.