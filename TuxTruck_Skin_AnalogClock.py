# TuxTruck Skin Manager
# Time-stamp: "2008-05-12 12:02:19 jantman"
# $Id: TuxTruck_Skin_AnalogClock.py,v 1.4 2008-05-12 16:34:40 jantman Exp $
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
        self.day_handColor = utility.str2tuple(analogClockTree.findtext("day_handColor"), "analogClock.day_handColor")
        self.day_shadowColor = utility.str2tuple(analogClockTree.findtext("day_shadowColor"), "analogClock.day_shadowColor")
        self.day_bgColor = utility.str2tuple(analogClockTree.findtext("day_bgColor"), "analogClock.day_bgColor")
        self.day_tickColor = utility.str2tuple(analogClockTree.findtext("day_tickColor"), "analogClock.day_tickColor")
        self.day_faceColor = utility.str2tuple(analogClockTree.findtext("day_faceColor"), "analogClock.day_faceColor")
        self.day_faceBorderColor = utility.str2tuple(analogClockTree.findtext("day_faceBorderColor"), "analogClock.day_faceBorderColor")

        self.night_handColor = utility.str2tuple(analogClockTree.findtext("night_handColor"), "analogClock.night_handColor")
        self.night_shadowColor = utility.str2tuple(analogClockTree.findtext("night_shadowColor"), "analogClock.night_shadowColor")
        self.night_bgColor = utility.str2tuple(analogClockTree.findtext("night_bgColor"), "analogClock.night_bgColor")
        self.night_tickColor = utility.str2tuple(analogClockTree.findtext("night_tickColor"), "analogClock.night_tickColor")
        self.night_faceColor = utility.str2tuple(analogClockTree.findtext("night_faceColor"), "analogClock.night_faceColor")
        self.night_faceBorderColor = utility.str2tuple(analogClockTree.findtext("night_faceBorderColor"), "analogClock.night_faceBorderColor")

    def __init__(self, parent, file):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """

        self.loadSkin(file) # DEBUG - everything else
