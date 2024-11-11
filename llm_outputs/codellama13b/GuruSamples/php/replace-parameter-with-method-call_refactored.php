<?php
$basePrice = $this->quantity * $this->itemPrice;
$seasonDiscount = $this->getSeasonalDiscount();
$fees = $this->getFees();
$finalPrice = $this->discountedPrice($basePrice, $seasonDiscount, $fees);

function discountedPrice($basePrice, $seasonDiscount, $fees) {
    $discount = $seasonDiscount + $fees;
    return $basePrice - $discount;
}

function getSeasonalDiscount() {
    $season = date('n');
    if ($season >= 1 && $season <= 3) {
        return 0.1;
    } elseif ($season >= 4 && $season <= 6) {
        return 0.2;
    } elseif ($season >= 7 && $season <= 9) {
        return 0.3;
    } elseif ($season >= 10 && $season <= 12) {
        return 0.4;
    } else {
        return 0;
    }
}

function getFees() {
    $fees = 0;
    if ($this->quantity >= 10) {
        $fees += 10;
    }
    if ($this->quantity >= 20) {
        $fees += 20;
    }
    return $fees;
}
?>