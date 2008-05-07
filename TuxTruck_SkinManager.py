# TuxTruck Skin Manager
# Time-stamp: "2008-05-07 19:55:43 jantman"
# $Id: TuxTruck_SkinManager.py,v 1.8 2008-05-07 23:59:38 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

# TODO: get rid of all these variables, have a subclass for each main element in the XML
#     i.e. digiclock.day_bgColor

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
    """

    # General information on the current skin
    # leave these as empty strings until we put something in them
    currentSkinName = "" # name of the current skin
    currentSkinFile = "" # filename of the current skin, 
    buttonImagePath = "" # path, relative to ~/.tuxtruck/skins/ to the images for this skin

    # primary (day) color scheme
    bgColor = "" # background color for the day mode skin
    fgColor = "" # foreground color for the day mode skin
    toolbarColor = "" # toolbar color for the day mode skin
    textColor = "" # main text color for the day mode skin
    highlightColor = "" # highlighted text color for the day mode skin

    # secondary (night) color scheme
    night_bgColor = "" # background color for the night mode skin
    night_fgColor = "" # foreground color for the night mode skin
    night_toolbarColor = "" # toolbar color for the night mode skin
    night_textColor = "" # main text color for the night mode skin
    night_highlightColor = "" # highlighted text color for the night mode skin

    # main window settings
    topWindowSize = 0 # size of the main program window/frame
    topWindowPos = 0 # top-left position of the main program window/frame
    topWindowCentered = 0 # whether main window is centered or not - 0 no 1 yes

    # button positions (top left)
    butn_home_pos = (0, 0)
    butn_gps_pos = (0, 0)
    butn_audio_pos = (0, 0)
    butn_obd_pos = (0, 0)
    butn_phone_pos = (0, 0)
    butn_tools_pos = (0, 0)
    butn_weather_pos = (0, 0)

    # digital clock settings
    digiclock_day_fgColor = wx.Colour(0,0,0)
    digiclock_day_bgColor = wx.Colour(0,0,0)
    digiclock_day_FadeColor = wx.Colour(0,0,0)
    digiclock_night_fgColor = wx.Colour(0,0,0)
    digiclock_night_bgColor = wx.Colour(0,0,0)
    digiclock_night_FadeColor = wx.Colour(0,0,0)
    digiclock_fadeFactor = 0

    # analog clock settings
    analogclock_day_handColor_h = wx.Colour(0,0,0)
    analogclock_day_handColor_m = wx.Colour(0,0,0)
    analogclock_day_handColor_s = wx.Colour(0,0,0)
    analogclock_day_shadowColor = wx.Colour(0,0,0)
    analogclock_day_bgColor = wx.Colour(0,0,0)
    analogclock_night_handColor_h = wx.Colour(0,0,0)
    analogclock_night_handColor_m = wx.Colour(0,0,0)
    analogclock_night_handColor_s = wx.Colour(0,0,0)
    analogclock_night_shadowColor = wx.Colour(0,0,0)
    analogclock_night_bgColor = wx.Colour(0,0,0)

    def loadSkin(self, file):
        """
        This function loads a new skin by reading and parsing the file, and then
        updating the variables in this class. The skin is specified by a file, in the
        path specified in the class documentation. It only updates the variables here,
        and doesn't make any changes to the GUI.
        NOTE: The size of buttons is exactly the size of the image used for the button.
        """

        # TODO: parse the XML and read the values

        # DEBUG TEST SETTINGS
        self.currentSkinName = "skinname"
        self.currentSkinFile = file
        self.buttonImagePath = "/home/jantman/cvs-temp/TuxTruck-wxPython/buttons/"

        self.bgColor = wx.Colour(22,127,230)
        self.fgColor = wx.Colour(3,90,166)
        self.toolbarColor = wx.Colour(22,127,230)
        self.textColor = wx.Colour(0,0,0)
        self.highlightColor = wx.Colour(255,0,0)

        # DEBUG as a test, just swap colors
        self.night_bgColor = wx.Colour(3,90,166)
        self.night_fgColor = wx.Colour(22,127,230)
        self.night_toolbarColor = wx.Colour(3,90,166)
        self.night_textColor = wx.Colour(0,0,0)
        self.night_highlightColor = wx.Colour(255,0,0)

        self.topWindowSize = wx.Size(800, 480)
        self.topWindowPos = wx.Point(100,100)

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

    def __init__(self, parent):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """
        #get the default skin name and file from settings
        #load the skin file. make changes to default, anything not specified stays default
        self.loadSkin("testSkin.nofile")
    
