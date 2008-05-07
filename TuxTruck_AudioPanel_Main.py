#! /usr/bin/env python
# TuxTruck Audio main frame
# Time-stamp: "2008-05-07 14:33:38 jantman"
# $Id: TuxTruck_AudioPanel_Main.py,v 1.1 2008-05-07 18:36:38 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

class TuxTruck_AudioPanel_Main(wx.Panel):
    """
    TODO: This needs to be documented
    """

    def __init__(self, parent, id):
        """
        TODO: This needs to be documented.
        """
        wx.Panel.__init__(self, parent, id) # init the panel

        # setup the main frame
        self.SetPosition(wx.Point(0,0)) # set the main window position
        self.SetSize(wx.Size(800,420)) # set the main window size TODO: use settings
        self.SetBackgroundColour(wx.Colour(0,0,0)) # set the main window background color
        #self.SetWindowStyle(wx.NO_BORDER) # set window style to have no border
        self.Hide()
