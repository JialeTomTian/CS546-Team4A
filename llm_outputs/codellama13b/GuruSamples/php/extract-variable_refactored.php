<?php
if (strpos(strtoupper($platform), "MAC")!== false &&
    strpos(strtoupper($browser), "IE")!== false &&
    $this->wasInitialized() && $this->resize > 0)
{
  // do something
}