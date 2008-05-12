# TuxTruck Skin Manager
# Time-stamp: "2008-05-12 14:58:13 jantman"
# $Id: TuxTruck_Settings_Audio.py,v 1.1 2008-05-12 19:01:44 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

# NOTE: This depends on elementtree from <http://effbot.org/zone/element-index.htm>
from elementtree import ElementTree

# TODO: write out settings

class TuxTruck_Settings_Audio:
    """
    This class handles reading and writing all of the settings related to audio playing.
    """

    def loadSkin(self, parent, file):
        """
        This function loads a new skin by reading and parsing the file, and then
        updating the variables in this class. The skin is specified by a file, in the
        path specified in the class documentation. It only updates the variables here,
        and doesn't make any changes to the GUI.
        NOTE: The size of buttons is exactly the size of the image used for the button.
        """

        # TODO: parse the XML and read the values
        skinTree = ElementTree.parse(file).getroot()

        # parse the window information
        audioSettings = skinTree.find('button_images')

        self.width = int(buttonTree.findtext("image_width"))
        self.height = int(buttonTree.findtext("image_height"))
        self.day_home = buttonTree.findtext("day_home")
        self.day_gps = buttonTree.findtext("day_gps")
        self.day_audio = buttonTree.findtext("day_audio")
        self.day_phone = buttonTree.findtext("day_phone")
        self.day_weather = buttonTree.findtext("day_weather")
        self.day_obd = buttonTree.findtext("day_obd")
        self.day_tools = buttonTree.findtext("day_tools")
        self.day_home_active = buttonTree.findtext("day_home_active")
        self.day_audio_active = buttonTree.findtext("day_audio_active")
        self.day_phone_active = buttonTree.findtext("day_phone_active")
        self.day_weather_active = buttonTree.findtext("day_weather_active")
        self.day_obd_active = buttonTree.findtext("day_obd_active")
        self.day_tools_active = buttonTree.findtext("day_tools_active")
        self.night_home = buttonTree.findtext("night_home")
        self.night_gps = buttonTree.findtext("night_gps")
        self.night_audio = buttonTree.findtext("night_audio")
        self.night_phone = buttonTree.findtext("night_phone")
        self.night_weather = buttonTree.findtext("night_weather")
        self.night_obd = buttonTree.findtext("night_obd")
        self.night_tools = buttonTree.findtext("night_tools")
        self.night_home_active = buttonTree.findtext("night_home_active")
        self.night_audio_active = buttonTree.findtext("night_audio_active")
        self.night_phone_active = buttonTree.findtext("night_phone_active")
        self.night_weather_active = buttonTree.findtext("night_weather_active")
        self.night_obd_active = buttonTree.findtext("night_obd_active")
        self.night_tools_active = buttonTree.findtext("night_tools_active")

    def __init__(self, parent, file):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """
        # TODO: Get audio settings file from parent (settings)
        file = "audio.xml"

        self.loadSkin(parent, file) # load the file
