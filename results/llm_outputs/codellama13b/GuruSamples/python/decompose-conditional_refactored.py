if date.before(SUMMER_START) or date.after(SUMMER_END):
    charge = quantity * winterRate
else:
    charge = quantity * summerRate + winterServiceCharge
