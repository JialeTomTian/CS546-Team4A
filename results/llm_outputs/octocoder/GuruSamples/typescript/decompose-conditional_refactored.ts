if (date.isBefore(SUMMER_START) || date.isAfter(SUMMER_END)) {
  charge = quantity * winterRate + winterServiceCharge;
}
else {
  charge = quantity * summerRate;
}
