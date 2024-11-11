class Soldier
{
    private int _health;
    private int _damage;
    private int _weaponStatus;

    public int Health
    {
        get => _health;
        set => _health = value;
    }

    public int Damage
    {
        get => _damage;
        set => _damage = value;
    }

    public int WeaponStatus
    {
        get => _weaponStatus;
        set => _weaponStatus = value;
    }

    public int GetDamage()
    {
        //...
    }

    public void Attack()
    {
        //...
    }
}