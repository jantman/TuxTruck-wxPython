#! /usr/bin/env python
# TuxTruck Audio main frame
# Time-stamp: "2008-05-12 14:40:39 jantman"
# $Id: TuxTruck_AudioPanel_PlayerPanel.py,v 1.1 2008-05-12 19:01:44 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI


class TuxTruck_AudioPanel_PlayerPanel(wx.Panel):
    """
    This is the audio player panel. It gives us an interface for playing audio files, podcasts, playlists, etc.
    """

    def __init__(self, parent, id):
        """
        Init function for the audio player panel.
        """
        wx.Panel.__init__(self, parent, id) # init the panel

        # setup the main frame
        self.SetPosition(wx.Point(60,0)) # set the main window position
        self.SetSize(wx.Size(740,420)) # set the main window size TODO: use settings
        #self.SetWindowStyle(wx.NO_BORDER) # set window style to have no border
        self.Hide()

    def reSkin(self, parent, colorSchemeName):
        # re-skin me
        
        if colorSchemeName == "day":
            # switch to day
            self.SetBackgroundColour(parent.settings.skin.day_bgColor)
            # DEBUG
            #self.SetBackgroundColour((0,255,0))
            # END DEBUG
        else:
            # switch to night
            self.SetBackgroundColour(parent.settings.skin.night_bgColor)
            # DEBUG
            #self.SetBackgroundColour((255,0,0))
            # END DEBUG
        self.Refresh()


