#! /usr/bin/env python
# TuxTruck Main Frame - This is the root of everything, called from the App in main.py
# Time-stamp: "2008-05-12 14:32:51 jantman"
# $Id: TuxTruck_Main.py,v 1.5 2008-05-12 18:49:59 jantman Exp $ 
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

# application includes
from TuxTruck_Settings import * # import TuxTruck_Settings to get user settings
from TuxTruck_AudioPanel_Main import *
from TuxTruck_HomePanel_Clock import *
from TuxTruck_Toolbar import *

class TuxTruck_Main(wx.Frame):
    """
    This is the top-level frame. It's the root of everything and everything happens (or is strated here).
    THIS IS CALLED from main.py, which is the runnable main program file.
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
    settings = TuxTruck_Settings()

    def __init__(self, parent, id):
        """
        This is the BIG function. It initiates EVERYTHING that gets initiated at start, 
        including settings, and all components that must run as long as the app is running.
        It SHOULD initiate GPS, Phone, and anything else that could take a while to start,
        as soon as possible. It also initiates everything that must run constantly.
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

        # add and init the toolbar
        self.toolbar = TuxTruck_Toolbar(self, -1)

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
        self.toolbar._currentButton = self.toolbar.butn_gps

    def OnClick_audio(self, event):
        """ Handles click of the Audio button, switching to the audio screen (panel/frame)"""
        # TODO: update the docs for proper use of words application, window, panel, frame
        print "Audio clicked" # DEBUG
        self.toolbar._currentButton = self.toolbar.butn_audio
        self.switchToModePanel(self.audioPanel_main) # show the main audio panel

    def OnClick_home(self, event):
        """ Handles click of the home button, switching to the home screen"""
        print "Home clicked" # DEBUG
        self.toolbar._currentButton = self.toolbar.butn_home # update reference to current button
        # DEBUG - testing only since we only have one panel
        self.audioPanel_main.Hide()
        # TODO: what do we show at startup? default? selection from settings? last?
        self.homePanel_clock.Show()

    def OnClick_obd(self, event):
        """Handles click of the OBD button, switching to the OBD screen"""
        print "obd clicked" # DEBUG
        self.toolbar._currentButton = self.toolbar.butn_obd

    def OnClick_phone(self, event):
        """ Handles click of the phone button, switching to the phone screen"""
        print "phone clicked" # DEBUG
        self.toolbar._currentButton = self.toolbar.butn_phone

    def OnClick_tools(self, event):
        """Handles click of the tools button, switching to the tools screen"""
        print "tools clicked" # DEBUG
        self.toolbar._currentButton = self.toolbar.butn_tools
        self.switchColorScheme() # DEBUG

    def OnClick_weather(self, event):
        """Handles click of the weather button, switching to the weather screen"""
        print "weather clicked" # DEBUG
        self.toolbar._currentButton = self.toolbar.butn_weather

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
            # update _currentColorScheme
            self._currentColorScheme = "night" # keep track of what skin I'm using now
        else:
            # reskin myself
            self.SetBackgroundColour(self.settings.skin.day_bgColor)
            # update _currentColorScheme
            self._currentColorScheme = "day" # keep track of what skin I'm using now

        # reskin EVERYTHING else using the new _colorSchemeName
        self.audioPanel_main.reSkin(self, self._currentColorScheme)
        self.homePanel_clock.reSkin(self, self._currentColorScheme)
        self.toolbar.reSkin(self, self._currentColorScheme)


        # refresh myself
        self.Refresh()        
        
    def switchToModePanel(self, activePanel):
        """Hides all of the top-level mode panels and then shows the one we want"""
        # hide all of the top-level mode panels
        activePanel.Show()
