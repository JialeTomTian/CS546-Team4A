double GetValueForPeriod(int periodNumber)
{
    if (periodNumber < 0 || periodNumber >= values.Length)
    {
        return 0;
    }

    return values[periodNumber];
}
