# TuxTruck Skin Manager
# Time-stamp: "2008-05-06 19:58:53 jantman"
# $Id: TuxTruck_Settings.py,v 1.2 2008-05-07 00:24:56 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

from TuxTruck_SkinManager import *

class TuxTruck_Settings:
    """"
    This class should be instantiated at the beginning of the main application. It provides
    an interface to all program setting-related data. Child classes handle reading, writing,
    and accessing setting data. I.e., to get the current skin file, we have a child class "skin",
    which is an instance of TuxTruck_SkinManager, as access that value as settings.skin.currentSkinFile.
    Child classes should read in the current (or default) settings at start.
    NOTE: Programmers should *NOT* modify variables directly. If it doesn't have a set() method,
    leave it alone.
    WARNING: Setting changes are not atomic. After running a set() method, you should run settings.writeSettings()
    which writes out the current settings from all child classes to their respective files. NOTE that this is 
    another reason not to modify variables directly. ALL variables are written to config files (i.e. on writeSettings(),
    every config file is totally re-written). If things get inadvertently changed (i.e. using = instead of ==), those 
    changes WILL be permanently written to the config files.
    This should have a child class for every category of settings, i.e. skins, navigation, phone, podcasts, etc.
    NOTE: ALL config files are stored in ~/.tuxtruck/
    """
    
    def __init__(self):
        "We instantiate all child classes, which will load in all settings and make them available."

        # load all settings related to the skin/GUI, from the TuxTruck_SkinManager class
        self.skin = TuxTruck_SkinManager(self)
