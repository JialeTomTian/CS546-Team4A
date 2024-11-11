def renderBanner(self):
    if (self.platform.upper().startswith("MAC") and \
       (self.browser.upper().startswith("IE") and \
       self.wasInitialized() and (self.resize > 0)):
        # do something