function getValueForPeriod($periodNumber) {
  if (!isset($this->values[$periodNumber])) {
    return 0;
  }

  return $this->values[$periodNumber];
}