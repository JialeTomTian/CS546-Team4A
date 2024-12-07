String foundPerson(String[] people) {
    for (String person : people) {
        if ("Don".equals(person)) {
            return "Don";
        }
        if ("John".equals(person)) {
            return "John";
        }
        if ("Kent".equals(person)) {
            return "Kent";
        }
    }
    return "";
}
