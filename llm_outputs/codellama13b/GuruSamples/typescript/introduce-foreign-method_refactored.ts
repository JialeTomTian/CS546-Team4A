class Report {
  //...
  sendReport(): void {
    const nextDay = new Date(previousEnd.getYear(),
      previousEnd.getMonth(), previousEnd.getDate() + 1);
    //...
  }
}