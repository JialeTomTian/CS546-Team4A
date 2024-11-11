<?php
$charge = $quantity * ($date->before(SUMMER_START) || $date->after(SUMMER_END)? $winterRate : $summerRate) + ($date->before(SUMMER_START) || $date->after(SUMMER_END)? $winterServiceCharge : 0);