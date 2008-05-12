#! /usr/bin/env python
# TuxTruck Main Frame Toolbar
# Time-stamp: "2008-05-12 15:23:15 jantman"
# $Id: TuxTruck_Toolbar.py,v 1.7 2008-05-12 19:22:43 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

class TuxTruck_Toolbar(wx.Panel):
    """
    This is the main toolbar for TuxTruck, appearing on every screen.
    """

    # TODO: what's with that box in the lower right that always has the day BG color?

    _currentButton = "" # reference to the currently selected button

    def __init__(self, parent, id):
        """
        Init the toolbar, set size and position, set it visible, call reSkin to setup the skin,
        finally bind all buttons to methods in parent (TuxTruck_Main)
        """
        wx.Panel.__init__(self, parent, id) # init the panel

        # this is required for the position calculation that centers the toolbar horizontally
        num_buttons = 7 # NOTE: must manually update the number of buttons on the toolbar

        # this is all hard-coded for a display of 800x480px
        pos_x = ((800/2)-((7* parent.settings.skin.butn.width)/2))
        pos_y = 480 - parent.settings.skin.butn.height
        self.SetPosition(wx.Point(pos_x,pos_y)) # set the main window position
        self.SetSize(wx.Size(800,parent.settings.skin.butn.height))

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
            self.butn_home.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.day_home, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_gps.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.day_gps, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_audio.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.day_audio, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_obd.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.day_obd, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_phone.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.day_phone, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_tools.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.day_tools, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_weather.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.day_weather, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
        else:
            # set night images
            print "setting night button images" # DEBUG
            self.butn_home.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.night_home, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_gps.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.night_gps, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_audio.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.night_audio, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_obd.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.night_obd, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_phone.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.night_phone, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_tools.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.night_tools, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.butn_weather.SetBitmapLabel(wx.Image(parent.settings.skin._buttonImagePath+parent.settings.skin.butn.night_weather, wx.BITMAP_TYPE_ANY).ConvertToBitmap())

        print "Current Button:"
        print self._currentButton

    def reSkin(self, parent, colorSchemeName):
        """
        Re-load skin information for specified colorSchemeName (day|night)
        """
        self.SetButtonImages(parent, colorSchemeName)
        if colorSchemeName == "day":
            self.SetBackgroundColour(parent.settings.skin.day_toolbarColor)
        else:
            self.SetBackgroundColour(parent.settings.skin.night_toolbarColor)
