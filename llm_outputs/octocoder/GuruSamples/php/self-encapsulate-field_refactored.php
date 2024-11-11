<?php

class Range
{
    private $low;
    private $high;

    public function __construct(int $low, int $high)
    {
        $this->low = $low;
        $this->high = $high;
    }

    public function includes(int $arg): bool
    {
        return $arg >= $this->low && $arg <= $this->high;
    }
}