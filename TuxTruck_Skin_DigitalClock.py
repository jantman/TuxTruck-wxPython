# TuxTruck Skin Manager
# Time-stamp: "2008-05-08 20:50:44 jantman"
# $Id: TuxTruck_Skin_DigitalClock.py,v 1.2 2008-05-09 01:22:06 jantman Exp $
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

        skinTree = ElementTree.parse(file).getroot()
        digitalClockTree = skinTree.find('digitalClock')

        self.day_fgColor = utility.str2tuple(digitalClockTree.findtext("day_fgColor"), "digitalClock.day_fgColor")
        self.day_bgColor = utility.str2tuple(digitalClockTree.findtext("day_bgColor"), "digitalClock.day_bgColor")
        self.day_fadeColor = utility.str2tuple(digitalClockTree.findtext("day_fadeColor"), "digitalClock.day_fadeColor")
        self.night_fgColor = utility.str2tuple(digitalClockTree.findtext("night_fgColor"), "digitalClock.night_fgColor")
        self.night_bgColor = utility.str2tuple(digitalClockTree.findtext("night_bgColor"), "digitalClock.night_bgColor")
        self.night_fadeColor = utility.str2tuple(digitalClockTree.findtext("night_fadeColor"), "digitalClock.night_fadeColor")
        self.fadeFactor = int(digitalClockTree.findtext("fadeFactor"))

    def __init__(self, parent, file):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """
        self.loadSkin(file)
