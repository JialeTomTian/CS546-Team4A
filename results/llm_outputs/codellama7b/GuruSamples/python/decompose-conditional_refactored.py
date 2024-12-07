if date.between(SUMMER_START, SUMMER_END):
    charge = quantity * summerRate
else:
    charge = quantity * winterRate + winterServiceCharge
