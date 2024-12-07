public double GetPayAmount()
{
    if (isDead)
        return DeadAmount();
    else if (isSeparated)
        return SeparatedAmount();
    else if (isRetired)
        return RetiredAmount();
    else
        return NormalPayAmount();
}
