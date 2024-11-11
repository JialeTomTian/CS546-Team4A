<?php

class Customer
{
    private $name;
    private $amount;

    public function __construct($name, $amount)
    {
        $this->name = $name;
        $this->amount = $amount;
    }

    public function printBanner()
    {
        print("*******************************");
        print("**** Customer Account ******");
        print("*******************************");
    }

    public function getOutstanding()
    {
        return $this->amount;
    }
}