<?php
class Order {
  //...

  public function calculateTotal() {
    $total = 0;
    foreach ($this->getProducts() as $product) {
      $total += $product->quantity * $product->price;
    }
    $total = $this->applyRegionalDiscounts($total);
    return $total;
  }

  public function applyRegionalDiscounts($total) {
    $discounts = [
      "US" => 0.85,
      "RU" => 0.75,
      "CN" => 0.9,
      //...
    ];
    return $total * $discounts[$this->user->getCountry()];
  }