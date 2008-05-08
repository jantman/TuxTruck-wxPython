#! /usr/bin/env python
# TuxTruck Audio main frame
# Time-stamp: "2008-05-07 21:13:50 jantman"
# $Id: TuxTruck_AudioPanel_Main.py,v 1.5 2008-05-08 01:14:11 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

class TuxTruck_AudioPanel_Main(wx.Panel):
    """
    TODO: This needs to be documented
    This panel should hold a main page with buttons that show sub-panels.
    """

    def __init__(self, parent, id):
        """
        TODO: This needs to be documented.
        """
        wx.Panel.__init__(self, parent, id) # init the panel

        # setup the main frame
        self.SetPosition(wx.Point(0,0)) # set the main window position
        self.SetSize(wx.Size(800,420)) # set the main window size TODO: use settings
        #self.SetWindowStyle(wx.NO_BORDER) # set window style to have no border
        self.Hide()
        # DEBUG
        #
        # family: wx.DEFAULT, wx.DECORATIVE, wx.ROMAN, wx.SCRIPT, wx.SWISS, wx.MODERN
        # slant: wx.NORMAL, wx.SLANT or wx.ITALIC
        # weight: wx.NORMAL, wx.LIGHT or wx.BOLD
        #FFont(pointSize, family, flags, face, encoding) 
        # use additional fonts this way ...
        font1 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1)
        debugText = wx.StaticText(self, -1, "Audio Panel", wx.Point(100, 200))
        debugText.SetFont(font1)
        debugText.SetForegroundColour(wx.Colour(255,0,0))
        # END DEBUG
        print parent.settings.skin.currentSkinName
        self.reSkin(parent, parent._currentColorScheme)

    def reSkin(self, parent, colorSchemeName):
        # re-skin me
        
        # DEBUG
        print "in TuxTruck_AudioPanel_Main switching color scheme to "+colorSchemeName
        # END DEBUG

        if colorSchemeName == "day":
            # switch to day
            self.SetBackgroundColour(parent.settings.skin.day_bgColor)
        else:
            # switch to night
            self.SetBackgroundColour(parent.settings.skin.night_bgColor)
        self.Refresh()

