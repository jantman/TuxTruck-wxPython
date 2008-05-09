#! /usr/bin/env python
# TuxTruck clock panel for home view
# Time-stamp: "2008-05-08 21:03:49 jantman"
# $Id: TuxTruck_HomePanel_Clock.py,v 1.6 2008-05-09 01:22:06 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

# the clocks came from http://xoomer.alice.it/infinity77/main/SpeedMeter.html

import wx # import wx for the GUI

from wx.lib.analogclock import *

import LEDCtrl as led
import time

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

        # analog clock
        self.clock = AnalogClockWindow(self)
        self.clock.SetBackgroundColour("yellow")

        self.bsizer2 = wx.BoxSizer(wx.VERTICAL)
        self.bsizer2.Add(self.clock, 1, wx.EXPAND|wx.ALIGN_CENTER|wx.ALL|wx.SHAPED, 10)        

        # digital clock
        self.myled = led.LEDCtrl(self)
        
        style = led.LED_ALIGN_CENTRE| \
                led.LED_AGG|          \
                led.LED_ALLOW_COLONS| \
                led.LED_SLANT
        
        self.myled.SetLedStyle(style)

        # TODO: need to get aggdraw working for this.

        #self.size = self.myled.GetSize()
        self.myled.Freeze()
        self.myled.SetWindowStyle(wx.SUNKEN_BORDER)
        self.myled.SetSize((600, 100))
        self.myled.SetDigits(6)
        #self.myled.SetSize(self.size)
        self.myled.Thaw()

        self.bsizer2.Add(self.myled, 1, wx.EXPAND|wx.ALIGN_CENTER|wx.ALL|wx.SHAPED, 10)        
        self.SetSizer(self.bsizer2)

        self.tc = -1
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.StartTimer()

    def StartTimer(self):
        self.timer.Start(500)


    def StopTimer(self):
        self.timer.Stop()


    def OnTimer(self, evt):
        self.tc = -self.tc
        t = time.localtime(time.time())
        if self.tc > 0:
            st = time.strftime("%H:%M:%S", t)
        else:
            st = time.strftime("%H%M%S", t)
        self.myled.SetValue(st)
        


    def setBgColor(self, mycolor):
        """
        This is called on a skin change to update my background color
        """
        self.SetBackgroundColour(mycolor)

    def reSkin(self, parent, colorSchemeName):
        """
        This is called to re-load the skin settings.
        """

        # DEBUG
        print "in TuxTruck_HomePanel_Clock switching color scheme to "+colorSchemeName
        # END DEBUG
        
        if colorSchemeName == "day":
            self.myled.SetForegroundColour(parent.settings.skin.digiClock.day_fgColor)
            self.myled.SetBackgroundColour(parent.settings.skin.digiClock.day_bgColor)
            self.myled.SetFadeColour(parent.settings.skin.digiClock.day_fadeColor)
            self.myled.SetFadeFactor(parent.settings.skin.digiClock.fadeFactor)
            self.clock.SetHandColours(parent.settings.skin.anaClock.day_handColor_h, parent.settings.skin.anaClock.day_handColor_m, parent.settings.skin.anaClock.day_handColor_s)
            self.clock.SetShadowColour(parent.settings.skin.anaClock.day_shadowColor)
            self.clock.SetBackgroundColour(parent.settings.skin.anaClock.day_bgColor)
            self.Refresh()
        else:
            # set night scheme
            self.myled.SetForegroundColour(parent.settings.skin.digiClock.night_fgColor)
            self.myled.SetBackgroundColour(parent.settings.skin.digiClock.night_bgColor)
            self.myled.SetFadeColour(parent.settings.skin.digiClock.night_fadeColor)
            self.myled.SetFadeFactor(parent.settings.skin.digiClock.fadeFactor)
            self.clock.SetHandColours(parent.settings.skin.anaClock.night_handColor_h, parent.settings.skin.anaClock.night_handColor_m, parent.settings.skin.anaClock.night_handColor_s)
            self.clock.SetShadowColour(parent.settings.skin.anaClock.night_shadowColor)
            self.clock.SetBackgroundColour(parent.settings.skin.anaClock.night_bgColor)
            self.Refresh()
