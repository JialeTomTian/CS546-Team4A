$charge = $quantity * ($date->before(SUMMER_START) || $date->after(SUMMER_END)? $winterRate + $winterServiceCharge : $summerRate);
