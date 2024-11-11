<?php
function disabilityAmount() {
  if ($this->seniority < 2 || $this->monthsDisabled > 12 || $this->isPartTime) {
    return 0;
  }
  // compute the disability amount
 ...