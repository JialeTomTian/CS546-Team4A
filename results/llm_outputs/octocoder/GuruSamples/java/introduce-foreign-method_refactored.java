 Here is the refactored code:

class Report {
  //...
  void sendReport() {
    Date nextDay = new Date(
      previousEnd.getYear(),
      previousEnd.getMonth(),
      previousEnd.getDate() + 1
    );
    //...
  }
}
