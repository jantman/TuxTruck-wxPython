# TuxTruck Skin Manager
# Time-stamp: "2008-05-08 20:14:49 jantman"
# $Id: TuxTruck_SkinManager.py,v 1.11 2008-05-09 00:16:45 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

# NOTE: This depends on elementtree from <http://effbot.org/zone/element-index.htm>
from elementtree import ElementTree

# application-wide utilities
import TuxTruck_Utility as utility

# sub-classes
from TuxTruck_Skin_Button import *

class TuxTruck_SkinManager:
    """
    This class provides an interface to all visual (skin) related information.
    It holds variables with all of the information needed to customize the GUI,
    and provides methods to update those variables from external files.
    This class should be instantiated at the start of the application. It will 
    then read in a skin data file, update the variables, and they'll be available 
    to the main program.
    NOTE: This is instantiated by the TuxTruck_Settings class, which provides an accessor
    and modifiers for all settings (easy access, like settings.skin.currentSkinFile).
    WARNING: Skin files should be static, i.e. the program should *not* modify them.
    Skin files are stored in ~/.tuxtruck/skins/
    A few very common values, such as skin name, file, and primary skin colors are stored
    locally. Everything else is subclassed - ex. there's a analogclock class that handles
    settings for the analog clock, which can then be references like: settings.skin.analogclock.day_bgColor
    """

    # General information on the current skin
    # leave these as empty strings until we put something in them
    currentSkinName = "" # name of the current skin
    currentSkinFile = "" # filename of the current skin, 
    buttonImagePath = "" # path, relative to ~/.tuxtruck/skins/ to the images for this skin

    def loadSkin(self, file):
        """
        This parses your skin file for global settings, such as name,
        background and foreground colors, size, button info, etc.
        """
        
        skinTree = ElementTree.parse(file).getroot()

        # parse the window information
        windowTree = skinTree.find('window')
        self.topWindowSize = wx.Size(int(windowTree.findtext("width")), int(windowTree.findtext("height")))
        self.topWindowPos = wx.Point(int(windowTree.findtext("pos_X")), int(windowTree.findtext("pos_Y")))
        # TODO: add the centered part

        # parse the main colors
        self.day_bgColor = utility.str2tuple(windowTree.findtext("day_bgColor"), "window.day_bgColor")
        self.day_fgColor = utility.str2tuple(windowTree.findtext("day_fgColor"), "window.day_fgColor")
        self.day_toolbarColor = utility.str2tuple(windowTree.findtext("day_toolbarColor"), "window.day_toolbarColor")
        self.day_textColor = utility.str2tuple(windowTree.findtext("day_textColor"), "window.day_textColor")
        self.day_highlightColor = utility.str2tuple(windowTree.findtext("day_highlightColor"), "window.day_highlightColor")
        self.night_bgColor = utility.str2tuple(windowTree.findtext("night_bgColor"), "window.night_bgColor")
        self.night_fgColor = utility.str2tuple(windowTree.findtext("night_fgColor"), "window.night_fgColor")
        self.night_toolbarColor = utility.str2tuple(windowTree.findtext("night_toolbarColor"), "window.night_toolbarColor")
        self.night_textColor = utility.str2tuple(windowTree.findtext("night_textColor"), "window.night_textColor")
        self.night_highlightColor = utility.str2tuple(windowTree.findtext("night_highlightColor"), "window.night_highlightColor")

        # parse global information
        globalTree = skinTree.find('globalSkin')
        self.currentSkinName = globalTree.findtext("skinName")
        self.currentSkinFile = file
        self.buttonImagePath = globalTree.findtext("buttonPath")


    def __init__(self, parent):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """
        #get the default skin name and file from settings
        #load the skin file. make changes to default, anything not specified stays default
        # TODO: get the skin file from settings (parent)
        skinFile = "defaultSkin.xml"

        self.loadSkin(skinFile) # Load MY MAIN skin
        self.butn = TuxTruck_Skin_Button(self, skinFile) # load the buttons information
