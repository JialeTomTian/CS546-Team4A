<?php
function getExpenseLimit() {
  return $this->expenseLimit?? $this->primaryProject->getMemberExpenseLimit();
}
