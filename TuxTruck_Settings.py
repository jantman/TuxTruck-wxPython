# settings test

from TuxTruck_SkinManager import *

class TuxTruck_Settings:
    "Class to handle all application-wide settings"
    
    # skin settings
    #skin = "" # declare it empty

    def __init__(self):
        # do the initial load

        # set the initial skin
        self.skin = TuxTruck_SkinManager(self)
