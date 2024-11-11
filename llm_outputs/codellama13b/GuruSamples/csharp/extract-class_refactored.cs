class Soldier 
{
  public int Health { get; set; }
  public int Damage { get; set; }
  public int WeaponStatus { get; set; }
  
  public int GetDamage() 
  {
    return Damage;
  }
  public void Attack() 
  {
    Health -= GetDamage();
  }
}