<?php
function printProperties($users) {
  foreach ($users as $user) {
    echo $user->getName(). " ". $user->getAge();

    //...
  }
}