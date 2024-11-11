<?php

class Rectangle
{
    private $height;
    private $width;

    public function __construct(int $height, int $width)
    {
        $this->height = $height;
        $this->width = $width;
    }

    public function getArea(): int
    {
        return $this->height * $this->width;
    }

    public function getPerimeter(): int
    {
        return 2 * ($this->height + $this->width);
    }
}