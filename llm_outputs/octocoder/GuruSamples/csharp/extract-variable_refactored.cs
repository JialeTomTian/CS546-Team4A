void RenderBanner() 
{
  if (IsMacIE() && wasInitialized() && resize > 0 )
  {
    // do something
  }
}

bool IsMacIE()
{
  return (platform.ToUpper().IndexOf("MAC") > -1) &&
         (browser.ToUpper().IndexOf("IE") > -1);
}