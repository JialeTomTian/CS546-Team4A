<?php
$basePrice = $this->quantity * $this->itemPrice;
return $basePrice * (($basePrice > 1000)? 0.95 : 0.98);
