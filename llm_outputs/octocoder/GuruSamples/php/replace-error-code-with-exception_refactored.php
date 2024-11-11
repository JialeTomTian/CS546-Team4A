<?php

class Account
{
    private $balance;

    public function __construct($balance)
    {
        $this->balance = $balance;
    }

    public function withdraw($amount)
    {
        if ($amount > $this->balance) {
            return -1;
        } else {
            $this->balance -= $amount;
            return 0;
        }
    }
}