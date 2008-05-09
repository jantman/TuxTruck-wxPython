# TuxTruck Skin Manager
# Time-stamp: "2008-05-08 20:22:35 jantman"
# $Id: TuxTruck_Skin_DigitalClock.py,v 1.1 2008-05-09 00:21:28 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

from elementtree import ElementTree

# application-wide utilities
import TuxTruck_Utility as utility

# TODO: EVERYTHING!!!

class TuxTruck_Skin_DigitalClock:
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

        # digital clock settings
        self.digiclock_day_fgColor = wx.Colour(0,0,255)
        self.digiclock_day_bgColor = wx.Colour(204,204,204)
        self.digiclock_day_FadeColor = wx.Colour(51,153,255)
        self.digiclock_night_fgColor = wx.Colour(255,0,0)
        self.digiclock_night_bgColor = wx.Colour(51,51,51)
        self.digiclock_night_FadeColor = wx.Colour(51,153,255)
        self.digiclock_fadeFactor = 25

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
