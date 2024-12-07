<?php
function disabilityAmount() {
  if ($this->isEligibleForDisability()) {
    // compute the disability amount
  }
  return 0;
}

function isEligibleForDisability() {
  return $this->seniority >= 2 && $this->monthsDisabled <= 12 &&!$this->isPartTime;
}
