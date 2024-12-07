
class Report {
  //...
  sendReport(): void {
    const nextDay = new Date(
      previousEnd.getFullYear(),
      previousEnd.getMonth(),
      previousEnd.getDate() + 1,
    );
    //...
  }
}
