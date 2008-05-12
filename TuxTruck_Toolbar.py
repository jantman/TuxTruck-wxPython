#! /usr/bin/env python
# TuxTruck Main Frame Toolbar
# Time-stamp: "2008-05-12 10:46:22 jantman"
# $Id: TuxTruck_Toolbar.py,v 1.1 2008-05-12 14:46:39 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

class TuxTruck_Toolbar(wx.Panel):
    """
    This is the main toolbar for TuxTruck, appearing on every screen.
    """

    _currentButton = "" # reference to the currently selected button

    def __init__(self, parent, id):
        """
        Init the toolbar, set size and position, set it visible, call reSkin to setup the skin,
        finally bind all buttons to methods in parent (TuxTruck_Main)
        """
        wx.Panel.__init__(self, parent, id) # init the panel

        # setup the main frame
        self.SetPosition(wx.Point(0,0)) # set the main window position
        self.SetSize(wx.Size(800,420)) # set the main window size TODO: use settings

        # create each of the buttons individually
        # NOTE: buttons must be explicitly added to SetButtonImages
        b_width = parent.settings.skin.butn.width # button width
        b_height = parent.settings.skin.butn.height # button height
        self.butn_home = wx.BitmapButton(self, size = (b_width, b_height))
        self.butn_gps = wx.BitmapButton(self, size = (b_width, b_height))
        self.butn_audio = wx.BitmapButton(self, size = (b_width, b_height))
        self.butn_obd = wx.BitmapButton(self, size = (b_width, b_height))
        self.butn_phone = wx.BitmapButton(self, size = (b_width, b_height))
        self.butn_tools = wx.BitmapButton(self, size = (b_width, b_height))
        self.butn_weather = wx.BitmapButton(self, size = (b_width, b_height))

        # set button images
        self.SetButtonImages(parent, parent._currentColorScheme)

        self.box = wx.BoxSizer(wx.HORIZONTAL) # TODO: give this a meaningful name
        self.box.Add(self.butn_home, proportion=0)
        self.box.Add(self.butn_gps, proportion=0)
        self.box.Add(self.butn_audio, proportion=0)
        self.box.Add(self.butn_obd, proportion=0)
        self.box.Add(self.butn_phone, proportion=0)
        self.box.Add(self.butn_tools, proportion=0)
        self.box.Add(self.butn_weather, proportion=0)

        self.SetAutoLayout(True)
        self.SetSizer(self.box)
        self.Layout()

        # bind each of the buttons to its' click handler
        self.butn_home.Bind(wx.EVT_BUTTON, parent.OnClick_home)
        self.butn_gps.Bind(wx.EVT_BUTTON, parent.OnClick_gps)
        self.butn_audio.Bind(wx.EVT_BUTTON, parent.OnClick_audio)
        self.butn_obd.Bind(wx.EVT_BUTTON, parent.OnClick_obd)
        self.butn_phone.Bind(wx.EVT_BUTTON, parent.OnClick_phone)
        self.butn_tools.Bind(wx.EVT_BUTTON, parent.OnClick_tools)
        self.butn_weather.Bind(wx.EVT_BUTTON, parent.OnClick_weather)

        self._currentButton = self.butn_home # set butn_home to be our initial button

        self.reSkin(parent, parent._currentColorScheme)
        self.Show()

    def SetButtonImages(self, parent, colorSchemeName):
        """
        This method sets the images of all of the buttons to the correct images
        for the selected color scheme (day/night within a specific skin). 
        """
        if colorSchemeName == "day":
            print "setting day button images" # DEBUG
            self.butn_home.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.day_home, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_gps.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.day_gps, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_audio.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.day_audio, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_obd.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.day_obd, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_phone.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.day_phone, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_tools.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.day_tools, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_weather.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.day_weather, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
        else:
            # set night images
            print "setting night button images" # DEBUG
            self.butn_home.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.night_home, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_gps.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.night_gps, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_audio.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.night_audio, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_obd.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.night_obd, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_phone.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.night_phone, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_tools.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.night_tools, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_weather.SetBitmapLabel(wx.Image(parent.settings.skin.buttonImagePath+parent.settings.skin.butn.night_weather, wx.BITMAP_TYPE_ANY).ConvertToBitmap())



    def reSkin(self, parent, colorSchemeName):
        """
        Re-load skin information for specified colorSchemeName (day|night)
        """
        self.SetButtonImages(parent, colorSchemeName)
