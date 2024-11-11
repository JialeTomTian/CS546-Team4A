<?php
function discount($inputVal, $quantity) {
  $discount = 0;
  if ($quantity > 50) {
    $discount = 2;
  }
  return $inputVal - $discount;
}