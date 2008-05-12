#! /usr/bin/env python
# TuxTruck Audio main frame
# Time-stamp: "2008-05-12 14:38:31 jantman"
# $Id: TuxTruck_AudioPanel_Main.py,v 1.7 2008-05-12 18:49:59 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

# application imports
from TuxTruck_AudioPanel_PlayerPanel import *

class TuxTruck_AudioPanel_Main(wx.Panel):
    """
    This is the top-level panel for audio functions, including audio file playing, radio, and podcast playing.
    """

    def __init__(self, parent, id):
        """
        Init function for the audio panel. Sets everything up.
        """
        wx.Panel.__init__(self, parent, id) # init the panel

        # setup the main frame
        self.SetPosition(wx.Point(0,0)) # set the main window position
        self.SetSize(wx.Size(800,420)) # set the main window size TODO: use settings
        #self.SetWindowStyle(wx.NO_BORDER) # set window style to have no border
        self.Hide()

        # this will be a BitmapButton to access a menu popup to choose search, MP3, playlist, radio, podcasts, etc.
        self.menu_button = wx.Button(self, -1, "Menu", (0,10), (60,50))

        # add the audio player panel
        self.playerPanel = TuxTruck_AudioPanel_PlayerPanel(self, -1)

        # setup the skins
        self.reSkin(parent, parent._currentColorScheme)

        # we're going to show the player panel by default.
        self.playerPanel.Show()

    def reSkin(self, parent, colorSchemeName):
        # re-skin me
        
        if colorSchemeName == "day":
            # switch to day
            self.SetBackgroundColour(parent.settings.skin.day_bgColor)
            self.playerPanel.reSkin(parent, "day")
        else:
            # switch to night
            self.SetBackgroundColour(parent.settings.skin.night_bgColor)
            self.playerPanel.reSkin(parent, "night")
        self.Refresh()

