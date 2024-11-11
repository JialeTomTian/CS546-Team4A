<?php
function setValue($name, $value) {
  switch ($name) {
    case "height":
      $this->height = $value;
      break;
    case "width":
      $this->width = $value;
      break;
    default:
      assert("Should never reach here");
      break;
  }
}