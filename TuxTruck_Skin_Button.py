# TuxTruck Skin Manager
# Time-stamp: "2008-05-08 20:03:25 jantman"
# $Id: TuxTruck_Skin_Button.py,v 1.1 2008-05-09 00:21:28 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

# NOTE: This depends on elementtree from <http://effbot.org/zone/element-index.htm>
from elementtree import ElementTree

class TuxTruck_Skin_Button:
    """
    This handles all of the skin parsing and variables for the buttons.
    It is instantiated in TuxTruck_SkinManager and all calls should be from there.
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
        buttonTree = skinTree.find('button_images')

        self.day_home = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_home"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_gps = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_gps"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_audio = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_audio"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_phone = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_phone"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_weather = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_weather"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_obd = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_obd"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_tools = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_tools"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_home_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_home_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_audio_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_audio_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_phone_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_phone_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_weather_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_weather_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_obd_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_obd_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.day_tools_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("day_tools_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_home = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_home"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_gps = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_gps"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_audio = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_audio"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_phone = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_phone"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_weather = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_weather"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_obd = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_obd"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_tools = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_tools"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_home_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_home_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_audio_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_audio_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_phone_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_phone_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_weather_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_weather_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_obd_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_obd_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.night_tools_active = wx.Image(parent.buttonImagePath+buttonTree.findtext("night_tools_active"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # TODO: add the centered part

    def __init__(self, parent, file):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """

        self.loadSkin(parent, file) # load the file
