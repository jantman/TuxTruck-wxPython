# TuxTruck Skin Manager
# Time-stamp: "2008-05-07 23:19:06 jantman"
# $Id: TuxTruck_SkinManager.py,v 1.10 2008-05-08 05:23:15 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

# NOTE: This depends on elementtree from <http://effbot.org/zone/element-index.htm>
from elementtree import ElementTree

# TODO: all var names should be of form {day|night}_propertyName

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

    # primary (day) color scheme
    day_bgColor = (0,0,0) # background color for the day mode skin
    day_fgColor = (0,0,0) # foreground color for the day mode skin
    day_toolbarColor = (0,0,0) # toolbar color for the day mode skin
    day_textColor = (0,0,0) # main text color for the day mode skin
    day_highlightColor = (0,0,0) # highlighted text color for the day mode skin

    # secondary (night) color scheme
    night_bgColor = (0,0,0) # background color for the night mode skin
    night_fgColor = (0,0,0) # foreground color for the night mode skin
    night_toolbarColor = (0,0,0) # toolbar color for the night mode skin
    night_textColor = (0,0,0) # main text color for the night mode skin
    night_highlightColor = (0,0,0) # highlighted text color for the night mode skin

    # main window settings
    topWindowSize = 0 # size of the main program window/frame
    topWindowPos = 0 # top-left position of the main program window/frame
    topWindowCentered = 0 # whether main window is centered or not - 0 no 1 yes

    def loadSkin(self, file):
        """
        This function loads a new skin by reading and parsing the file, and then
        updating the variables in this class. The skin is specified by a file, in the
        path specified in the class documentation. It only updates the variables here,
        and doesn't make any changes to the GUI.
        NOTE: The size of buttons is exactly the size of the image used for the button.
        """

        # TODO: parse the XML and read the values

        # DEBUG: all image sizes are currently 106wX58h
        self.butn_home_pos = (29, 422)
        self.butn_gps_pos = (135, 422)
        self.butn_audio_pos = (241, 422)
        self.butn_phone_pos = (347, 422)
        self.butn_weather_pos = (453, 422)
        self.butn_obd_pos = (559, 422)
        self.butn_tools_pos = (665, 422)

        # digital clock settings
        self.digiclock_day_fgColor = wx.Colour(0,0,255)
        self.digiclock_day_bgColor = wx.Colour(204,204,204)
        self.digiclock_day_FadeColor = wx.Colour(51,153,255)
        self.digiclock_night_fgColor = wx.Colour(255,0,0)
        self.digiclock_night_bgColor = wx.Colour(51,51,51)
        self.digiclock_night_FadeColor = wx.Colour(51,153,255)
        self.digiclock_fadeFactor = 25

        # analog clock settings
        self.analogclock_day_handColor_h = wx.Colour(255,255,255)
        self.analogclock_day_handColor_m = wx.Colour(255,255,255)
        self.analogclock_day_handColor_s = wx.Colour(255,255,255)
        self.analogclock_day_shadowColor = wx.Colour(200,200,200)
        self.analogclock_day_bgColor = wx.Colour(51,51,51)
        self.analogclock_night_handColor_h = wx.Colour(0,0,0)
        self.analogclock_night_handColor_m = wx.Colour(0,0,0)
        self.analogclock_night_handColor_s = wx.Colour(0,0,0)
        self.analogclock_night_shadowColor = wx.Colour(100,100,100)
        self.analogclock_night_bgColor = wx.Colour(204,204,204)

    def loadMainSkin(self, file):
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
        self.day_bgColor = self.str2tuple(windowTree.findtext("day_bgColor"), "window.day_bgColor")
        self.day_fgColor = self.str2tuple(windowTree.findtext("day_fgColor"), "window.day_fgColor")
        self.day_toolbarColor = self.str2tuple(windowTree.findtext("day_toolbarColor"), "window.day_toolbarColor")
        self.day_textColor = self.str2tuple(windowTree.findtext("day_textColor"), "window.day_textColor")
        self.day_highlightColor = self.str2tuple(windowTree.findtext("day_highlightColor"), "window.day_highlightColor")
        self.night_bgColor = self.str2tuple(windowTree.findtext("night_bgColor"), "window.night_bgColor")
        self.night_fgColor = self.str2tuple(windowTree.findtext("night_fgColor"), "window.night_fgColor")
        self.night_toolbarColor = self.str2tuple(windowTree.findtext("night_toolbarColor"), "window.night_toolbarColor")
        self.night_textColor = self.str2tuple(windowTree.findtext("night_textColor"), "window.night_textColor")
        self.night_highlightColor = self.str2tuple(windowTree.findtext("night_highlightColor"), "window.night_highlightColor")

        # parse global information
        globalTree = skinTree.find('globalSkin')
        self.currentSkinName = globalTree.findtext("skinName")
        self.currentSkinFile = file
        self.buttonImagePath = globalTree.findtext("buttonPath")

    def str2tuple(self, s, fieldName):
        """
        Convert tuple-like strings to real tuples.
        eg '(1,2,3,4)' -> (1, 2, 3, 4)
        s is the string to parse

        This is used to parse the XML skin data.
        Got it from Steven D'Aprano, posted to python-list@python.org 2005-07-19
        TODO: this needs better error checking
        """
        if s[0] + s[-1] != "()":
            raise ValueError("Badly formatted string (missing brackets) in skin field "+fieldName+".")
        items = s[1:-1]  # removes the leading and trailing brackets
        items = items.split(',')
        L = [int(x.strip()) for x in items] # clean up spaces, convert to ints
        return tuple(L) 


    def __init__(self, parent):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """
        #get the default skin name and file from settings
        #load the skin file. make changes to default, anything not specified stays default
        self.loadMainSkin("defaultSkin.xml")

        self.loadSkin("defaultSkin.xml") # DEBUG - everything else
