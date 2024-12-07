<?php
function foundPerson(array $people){
  foreach ($people as $person) {
    if ($person === "Don" || $person === "John" || $person === "Kent") {
      return $person;
    }
  }
  return "";
}
