#! /usr/bin/env python
# TuxTruck clock panel for home view
# Time-stamp: "2008-05-07 16:21:11 jantman"
# $Id: TuxTruck_HomePanel_Clock.py,v 1.2 2008-05-07 20:20:15 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

# the clocks came from http://xoomer.alice.it/infinity77/main/SpeedMeter.html

import wx # import wx for the GUI

from wx.lib.analogclock import *

class TuxTruck_HomePanel_Clock(wx.Panel):
    """
    TODO: This needs to be documented
    This panel shows the clocks for the main "home" mode.
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

        self.clock = AnalogClockWindow(self)
        self.clock.SetBackgroundColour("yellow")

        self.bsizer2 = wx.BoxSizer(wx.VERTICAL)
        self.bsizer2.Add(self.clock, 1, wx.EXPAND|wx.ALIGN_CENTER|wx.ALL|wx.SHAPED, 10)        
        self.SetSizer(self.bsizer2)
        
        


    def setBgColor(self, mycolor):
        """
        This is called on a skin change to update my background color
        """
        self.SetBackgroundColour(mycolor)
