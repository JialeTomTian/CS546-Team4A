<?php
class Rectangle {
  public $height;
  public $width;

  public function __construct($height, $width) {
    $this->height = $height;
    $this->width = $width;
  }

  public function setHeight($height) {
    $this->height = $height;
  }

  public function setWidth($width) {
    $this->width = $width;
  }
}