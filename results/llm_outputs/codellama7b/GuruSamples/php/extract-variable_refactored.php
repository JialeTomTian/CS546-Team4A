<?php
if (strtoupper($platform) === 'MAC' &&
    strtoupper($browser) === 'IE' &&
    $this->wasInitialized() && $this->resize > 0)
{
  // do something
}
