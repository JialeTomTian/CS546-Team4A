<?php
class Soldier {
  public $health; // int
  public $damage; // int
  public $weaponStatus; // int

  public function getDamage() {
    return $this->damage;
  }

  public function attack() {
    $this->health -= $this->getDamage();
  }
}
