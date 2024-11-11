<?php
function printProperties($users) {
  foreach ($users as $user) {
    $result = $user->getName(). " ". $user->getAge();
    echo $result;
  }
}