string FoundPerson(string[] people)
{
    foreach (string person in people)
    {
        if (person == "Don")
        {
            return "Don";
        }
        if (person == "John")
        {
            return "John";
        }
        if (person == "Kent")
        {
            return "Kent";
        }
    }
    return string.Empty;
}