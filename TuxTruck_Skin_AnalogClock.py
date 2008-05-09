# TuxTruck Skin Manager
# Time-stamp: "2008-05-08 20:22:25 jantman"
# $Id: TuxTruck_Skin_AnalogClock.py,v 1.1 2008-05-09 00:21:28 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

from elementtree import ElementTree

# application-wide utilities
import TuxTruck_Utility as utility

# TODO: EVERYTHING!!!

class TuxTruck_Skin_AnalogClock:
    """
    This class handles skin settings for the digital clock
    """

    def loadSkin(self, file):
        """
        This function loads a new skin by reading and parsing the file, and then
        updating the variables in this class. The skin is specified by a file, in the
        path specified in the class documentation. It only updates the variables here,
        and doesn't make any changes to the GUI.
        NOTE: The size of buttons is exactly the size of the image used for the button.
        """

        # TODO: parse the XML and read the values

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

        skinTree = ElementTree.parse(file).getroot()

        # parse the window information
        windowTree = skinTree.find('window')
        #self.topWindowSize = wx.Size(int(windowTree.findtext("width")), int(windowTree.findtext("height")))
        #self.topWindowPos = wx.Point(int(windowTree.findtext("pos_X")), int(windowTree.findtext("pos_Y")))

    def __init__(self, parent):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """

        self.loadSkin("defaultSkin.xml") # DEBUG - everything else
