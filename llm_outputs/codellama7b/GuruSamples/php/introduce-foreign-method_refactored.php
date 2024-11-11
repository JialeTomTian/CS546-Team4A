<?php
class Report {
  //...
  public function sendReport() {
    $paymentDate = $this->previousDate->modify("+7 days");
    //...
  }
}