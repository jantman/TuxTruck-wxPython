# TuxTruck Skin Manager
# Time-stamp: "2008-05-12 21:14:58 jantman"
# $Id: TuxTruck_Skin_InternalThermo.py,v 1.1 2008-05-13 01:16:14 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

from elementtree import ElementTree

# application-wide utilities
import TuxTruck_Utility as utility

# TODO: EVERYTHING!!!

class TuxTruck_Skin_InternalThermo:
    """
    This class handles skin settings for the internal thermometer
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
        internalThermoTree = skinTree.find('internalThermo')

        self.day_fgColor = utility.str2tuple(internalThermoTree.findtext("day_fgColor"), "internalThermo.day_fgColor")
        self.day_bgColor = utility.str2tuple(internalThermoTree.findtext("day_bgColor"), "internalThermo.day_bgColor")
        self.day_fadeColor = utility.str2tuple(internalThermoTree.findtext("day_fadeColor"), "internalThermo.day_fadeColor")
        self.night_fgColor = utility.str2tuple(internalThermoTree.findtext("night_fgColor"), "internalThermo.night_fgColor")
        self.night_bgColor = utility.str2tuple(internalThermoTree.findtext("night_bgColor"), "internalThermo.night_bgColor")
        self.night_fadeColor = utility.str2tuple(internalThermoTree.findtext("night_fadeColor"), "internalThermo.night_fadeColor")
        self.fadeFactor = int(internalThermoTree.findtext("fadeFactor"))

    def __init__(self, parent, file):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """
        self.loadSkin(file)
