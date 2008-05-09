#! /usr/bin/env python
# TuxTruck Main Application (this is what you run!)
# Time-stamp: "2008-05-08 20:12:16 jantman"
# $Id: main.py,v 1.17 2008-05-09 00:16:45 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

# TODO: do we need all of the self. here?
# TODO: need to update buttons to use a sizer
# TODO: rename MainApp to MainFrame
# TODO: use active images for buttons

# application includes
from TuxTruck_Settings import * # import TuxTruck_Settings to get user settings
from TuxTruck_AudioPanel_Main import *
from TuxTruck_HomePanel_Clock import *

class TuxTruck_MainApp(wx.Frame):
    """
    This is the top-level frame/window/app for TuxTruck. It's the root of everything
    and everything happens (or is strated here). 
    This should just handle building the base GUI (blank main panel), and then instantiate
    child classes to do EVERYTHING else. Each part of the GUI should be its own class, that 
    holds a main panel and then does everything relating to that component (hopefully with 
    multiple child classes).
    NOTE: This should ONLY
      a) start the GUI, and init everything
      b) init TuxTruck_Settings to get user settings
      c) init any of the elements/categories that need to be constantly running (gps, phone, audio, obd)
      d) handle ALL of the communication/events that require interaction between categories, or
         require interrupts (GPS instructions, pop-ups, phone calls, etc.)
    """

    # variables holding state of the program
    _currentColorScheme = "day" # holds the name of the current color scheme
    _currentButton = "" # reference to the currently selected button, default to Home
    settings = TuxTruck_Settings()

    def __init__(self, parent, id):
        """
        This is the BIG function. It initiates EVERYTHING that gets initiated at start, 
        including settings, and all components that must run as long as the app is running.
        It SHOULD initiate GPS, Phone, and anything else that could take a while to start,
        as soon as possible.
        """
        wx.Frame.__init__(self, parent, id, '', style=wx.NO_BORDER) # init the main frame

        # setup the settings
        print "Loaded skin "+self.settings.skin.currentSkinName+" from file "+self.settings.skin.currentSkinFile

        # setup the main frame
        self.SetPosition(self.settings.skin.topWindowPos) # set the main window position
        self.SetSize(self.settings.skin.topWindowSize) # set the main window size
        if self.settings.skin.topWindowCentered == 1:
            # check whether to center the window or not
            self.CenterOnScreen()
        self.SetWindowStyle(wx.NO_BORDER) # set window style to have no border

        # TODO: we need to load the right images for our skin. figure out how.
        self.loadButtonImages() # load the button images

        # create each of the buttons individually
        # NOTE: buttons must be explicitly added to switchColorScheme and loadButtonImages
        self.butn_home = wx.BitmapButton(self, bitmap=self.settings.skin.butn.day_home_active, size = (self.butn_home_image.GetWidth(), self.butn_home_image.GetHeight()))
        self.butn_gps = wx.BitmapButton(self, bitmap=self.settings.skin.butn.day_gps, size = (self.butn_gps_image.GetWidth(), self.butn_gps_image.GetHeight()))
        self.butn_audio = wx.BitmapButton(self, bitmap=self.settings.skin.butn.day_audio, size = (self.butn_audio_image.GetWidth(), self.butn_audio_image.GetHeight()))
        self.butn_obd = wx.BitmapButton(self, bitmap=self.settings.skin.butn.day_obd, size = (self.butn_obd_image.GetWidth(), self.butn_obd_image.GetHeight()))
        self.butn_phone = wx.BitmapButton(self, bitmap=self.settings.skin.butn.day_phone, size = (self.butn_phone_image.GetWidth(), self.butn_phone_image.GetHeight()))
        self.butn_tools = wx.BitmapButton(self, bitmap=self.settings.skin.butn.day_tools, size = (self.butn_tools_image.GetWidth(), self.butn_tools_image.GetHeight()))
        self.butn_weather = wx.BitmapButton(self, bitmap=self.settings.skin.butn.day_weather, size = (self.butn_weather_image.GetWidth(), self.butn_weather_image.GetHeight()))

        # TODO: how do we set the correct image for the active button?

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

        # DEBUG
        print self.box.GetSizeTuple()
        print self.box.GetPositionTuple()

        # bind each of the buttons to its' click handler
        self.butn_home.Bind(wx.EVT_BUTTON, self.OnClick_home)
        self.butn_gps.Bind(wx.EVT_BUTTON, self.OnClick_gps)
        self.butn_audio.Bind(wx.EVT_BUTTON, self.OnClick_audio)
        self.butn_obd.Bind(wx.EVT_BUTTON, self.OnClick_obd)
        self.butn_phone.Bind(wx.EVT_BUTTON, self.OnClick_phone)
        self.butn_tools.Bind(wx.EVT_BUTTON, self.OnClick_tools)
        self.butn_weather.Bind(wx.EVT_BUTTON, self.OnClick_weather)

        self._currentButton = self.butn_home # set butn_home to be our initial button

        # add main audio panel
        self.audioPanel_main = TuxTruck_AudioPanel_Main(self, -1)
        # add home clock panel
        # TODO: figure out how to skin this
        self.homePanel_clock = TuxTruck_HomePanel_Clock(self, -1)

        # now SET THE SKINS on EVERYTHING
        self.reSkin("day")
        
    def OnClick_gps(self, event):
        """ Handles click of the GPS button, switching to the GPS screen"""
        print "GPS clicked" # DEBUG
        self._currentButton = self.butn_gps

    def OnClick_audio(self, event):
        """ Handles click of the Audio button, switching to the audio screen (panel/frame)"""
        # TODO: update the docs for proper use of words application, window, panel, frame
        print "Audio clicked" # DEBUG
        self._currentButton = self.butn_audio
        self.switchToModePanel(self.audioPanel_main) # show the main audio panel

    def OnClick_home(self, event):
        """ Handles click of the home button, switching to the home screen"""
        print "Home clicked" # DEBUG
        self._currentButton = self.butn_home # update reference to current button
        # DEBUG - testing only since we only have one panel
        self.audioPanel_main.Hide()
        # TODO: what do we show at startup? default? selection from settings? last?
        self.homePanel_clock.Show()

    def OnClick_obd(self, event):
        """Handles click of the OBD button, switching to the OBD screen"""
        print "obd clicked" # DEBUG
        self._currentButton = self.butn_obd

    def OnClick_phone(self, event):
        """ Handles click of the phone button, switching to the phone screen"""
        print "phone clicked" # DEBUG
        self._currentButton = self.butn_phone

    def OnClick_tools(self, event):
        """Handles click of the tools button, switching to the tools screen"""
        print "tools clicked" # DEBUG
        self._currentButton = self.butn_tools
        self.switchColorScheme() # DEBUG

    def OnClick_weather(self, event):
        """Handles click of the weather button, switching to the weather screen"""
        print "weather clicked" # DEBUG
        self._currentButton = self.butn_weather

    def SetButtonImages(self, colorSchemeName):
        """
        This method sets the images of all of the buttons to the correct images
        for the selected color scheme (day/night within a specific skin). 
        """
        if colorSchemeName == "day":
            print "setting day button images" # DEBUG
            self.butn_home.bitmap = self.settings.skin.butn.day_home
            self.butn_gps.bitmap = self.settings.skin.butn.day_gps
            self.butn_audio.bitmap = self.settings.skin.butn.day_audio
            self.butn_obd.bitmap = self.settings.skin.butn.day_obd
            self.butn_phone.bitmap = self.settings.skin.butn.day_phone
            self.butn_tools.bitmap = self.settings.skin.butn.day_tools
            self.butn_weather.bitmap = self.settings.skin.butn.day_weather
        else:
            # set night images
            print "setting night button images" # DEBUG
            self.butn_home.bitmap = self.settings.skin.butn.night_home
            self.butn_gps.bitmap = self.settings.skin.butn.night_gps
            self.butn_audio.bitmap = self.settings.skin.butn.night_audio
            self.butn_obd.bitmap = self.settings.skin.butn.night_obd
            self.butn_phone.bitmap = self.settings.skin.butn.night_phone
            self.butn_tools.bitmap = self.settings.skin.butn.night_tools
            self.butn_weather.bitmap = self.settings.skin.butn.night_weather

    def switchColorScheme(self):
        """
        This method does everything needed to toggle between day/night modes
        in the current skin
        """

        # DEBUG
        print "in main.py switching color scheme from "+self._currentColorScheme
        # END DEBUG
        
        if self._currentColorScheme == "day":
            self.reSkin("night")
        else:
            self.reSkin("day")


    def reSkin(self, colorSchemeName):
        if self._currentColorScheme == "day":
            # reskin myself
            self.SetBackgroundColour(self.settings.skin.night_bgColor) # reskin myself
            self.SetButtonImages("night")

            # reskin EVERYTHING else
            self.audioPanel_main.reSkin(self, "night")
            self.homePanel_clock.reSkin(self, "night")

            self._currentColorScheme = "night" # keep track of what skin I'm using now

        else:
            # reskin myself
            self.SetBackgroundColour(self.settings.skin.day_bgColor)
            self.SetButtonImages("day")

            # reskin EVERYTHING else
            self.audioPanel_main.reSkin(self, "day")
            self.homePanel_clock.reSkin(self, "day")

            self._currentColorScheme = "day" # keep track of what skin I'm using now

        # refresh myself
        self.Refresh()        
        
    def switchToModePanel(self, activePanel):
        """Hides all of the top-level mode panels and then shows the one we want"""
        # hide all of the top-level mode panels
        self.audioPanel_main.Hide()
        self.homePanel_clock.Hide()
        activePanel.Show()


if __name__ == '__main__':
    """ 
    main method for the whole program. This gets called when we start this application,
    and it instantiates all of the necessary classes and starts the GUI and backend code.
    """
    app = wx.App()

    frame = TuxTruck_MainApp(parent=None, id=-1)

    frame.Show()
    app.MainLoop()
