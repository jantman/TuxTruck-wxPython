# TuxTruck Skin Manager
# Time-stamp: "2008-05-12 20:58:02 jantman"
# $Id: TuxTruck_Skin_ExternalThermo.py,v 1.1 2008-05-13 01:16:14 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

from elementtree import ElementTree

# application-wide utilities
import TuxTruck_Utility as utility

# TODO: EVERYTHING!!!

class TuxTruck_Skin_ExternalThermo:
    """
    This class handles skin settings for the external thermometer
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
        externalThermoTree = skinTree.find('externalThermo')

        self.day_fgColor = utility.str2tuple(externalThermoTree.findtext("day_fgColor"), "externalThermo.day_fgColor")
        self.day_bgColor = utility.str2tuple(externalThermoTree.findtext("day_bgColor"), "externalThermo.day_bgColor")
        self.day_fadeColor = utility.str2tuple(externalThermoTree.findtext("day_fadeColor"), "externalThermo.day_fadeColor")
        self.night_fgColor = utility.str2tuple(externalThermoTree.findtext("night_fgColor"), "externalThermo.night_fgColor")
        self.night_bgColor = utility.str2tuple(externalThermoTree.findtext("night_bgColor"), "externalThermo.night_bgColor")
        self.night_fadeColor = utility.str2tuple(externalThermoTree.findtext("night_fadeColor"), "externalThermo.night_fadeColor")
        self.fadeFactor = int(externalThermoTree.findtext("fadeFactor"))

    def __init__(self, parent, file):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """
        self.loadSkin(file)
