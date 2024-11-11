<?php
function withdraw($amount) {
  if ($amount > $this->balance) {
    return -1;
  }
  $this->balance -= $amount;
  return 0;
}