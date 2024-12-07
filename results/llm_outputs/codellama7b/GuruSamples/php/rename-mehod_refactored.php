<?php
class Customer {
  private $name;
  private $lastName;

  public function __construct($name, $lastName) {
    $this->name = $name;
    $this->lastName = $lastName;
  }

  public function getLastName() {
    return $this->lastName;
  }

  // other methods...
}
