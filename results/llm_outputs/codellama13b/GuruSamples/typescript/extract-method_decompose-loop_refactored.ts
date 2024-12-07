printProperties(users: User[]): void {
  for (let user of users) {
    console.log(`${user.getName()} ${user.getAge()}`);
  }
}
