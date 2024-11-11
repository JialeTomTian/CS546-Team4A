<?php
class Order {
  //...

  public function calculateTotal() {
    $total = 0;
    foreach ($this->getProducts() as $product) {
      $total += $product->quantity * $product->price;
    }

    // Apply regional discounts.
    $total *= $this->getDiscountFactor();

    return $total;
  }

  private function getDiscountFactor() {
    switch ($this->user->getCountry()) {
      case "US": return 0.85;
      case "RU": return 0.75;
      case "CN": return 0.9;
      //...
    }
  }
}