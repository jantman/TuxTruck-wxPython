# TuxTruck Skin Manager
# Time-stamp: "2008-05-08 21:07:31 jantman"
# $Id: TuxTruck_Skin_AnalogClock.py,v 1.2 2008-05-09 01:22:06 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

from elementtree import ElementTree

# application-wide utilities
import TuxTruck_Utility as utility

class TuxTruck_Skin_AnalogClock:
    """
    This class handles skin settings for the analog clock
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
        analogClockTree = skinTree.find('analogClock')

        # analog clock settings
        self.day_handColor_h = utility.str2tuple(analogClockTree.findtext("day_handColor_h"), "analogClock.day_handColor_h")
        self.day_handColor_m = utility.str2tuple(analogClockTree.findtext("day_handColor_m"), "analogClock.day_handColor_m")
        self.day_handColor_s = utility.str2tuple(analogClockTree.findtext("day_handColor_s"), "analogClock.day_handColor_s")
        self.day_shadowColor = utility.str2tuple(analogClockTree.findtext("day_shadowColor"), "analogClock.day_shadowColor")
        self.day_bgColor = utility.str2tuple(analogClockTree.findtext("day_bgColor"), "analogClock.day_bgColor")
        self.night_handColor_h = utility.str2tuple(analogClockTree.findtext("night_handColor_h"), "analogClock.night_handColor_h")
        self.night_handColor_m = utility.str2tuple(analogClockTree.findtext("night_handColor_m"), "analogClock.night_handColor_m")
        self.night_handColor_s = utility.str2tuple(analogClockTree.findtext("night_handColor_s"), "analogClock.night_handColor_s")
        self.night_shadowColor = utility.str2tuple(analogClockTree.findtext("night_shadowColor"), "analogClock.night_shadowColor")
        self.night_bgColor = utility.str2tuple(analogClockTree.findtext("night_bgColor"), "analogClock.night_bgColor")

    def __init__(self, parent, file):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """

        self.loadSkin(file) # DEBUG - everything else
