#! /usr/bin/env python
# TuxTruck clock panel for home view
# Time-stamp: "2008-05-12 12:32:04 jantman"
# $Id: TuxTruck_HomePanel_Clock.py,v 1.8 2008-05-12 16:34:40 jantman Exp $
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
        self.SetBackgroundColour(parent.settings.skin.day_bgColor)
        self.Hide()

        # analog clock
        self.clock = AnalogClock(self)

        # digital clock
        self.myled = led.LEDCtrl(self)
        
        style = led.LED_ALIGN_CENTRE| \
                led.LED_AGG|          \
                led.LED_ALLOW_COLONS| \
                led.LED_SLANT
        self.myled.SetLedStyle(style)

        # TODO: need to get aggdraw working for this.

        self.myled.Freeze()
        self.myled.SetWindowStyle(wx.SUNKEN_BORDER)

        # set sizes and positons
        self.myled.SetSize((400, 80))
        self.myled.SetPosition((200,330))
        self.clock.SetSize((300,300))
        self.clock.SetPosition((250,10))

        self.myled.SetDigits(6)
        #self.myled.SetSize(self.size)
        self.myled.Thaw()

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
        


    def reSkin(self, parent, colorSchemeName):
        """
        This is called to re-load the skin settings.
        """

        # DEBUG
        print "in TuxTruck_HomePanel_Clock switching color scheme to "+colorSchemeName
        # END DEBUG
        
        if colorSchemeName == "day":
            # me (panel)
            self.SetBackgroundColour(parent.settings.skin.day_bgColor)

            # LED clock
            self.myled.SetForegroundColour(parent.settings.skin.digiClock.day_fgColor)
            self.myled.SetBackgroundColour(parent.settings.skin.digiClock.day_bgColor)
            self.myled.SetFadeColour(parent.settings.skin.digiClock.day_fadeColor)
            self.myled.SetFadeFactor(parent.settings.skin.digiClock.fadeFactor)

            # analog clock
            self.clock.SetHandBorderColour(parent.settings.skin.anaClock.day_handColor)
            self.clock.SetHandFillColour(parent.settings.skin.anaClock.day_handColor)
            self.clock.SetShadowColour(parent.settings.skin.anaClock.day_shadowColor)
            self.clock.SetBackgroundColour(parent.settings.skin.anaClock.day_bgColor)
            self.clock.SetTickBorderColour(parent.settings.skin.anaClock.day_tickColor)
            self.clock.SetTickFillColour(parent.settings.skin.anaClock.day_tickColor)
            self.clock.SetFaceBorderColour(parent.settings.skin.anaClock.day_faceBorderColor)
            self.clock.SetFaceFillColour(parent.settings.skin.anaClock.day_faceColor)

            self.Refresh()
        else:
            # set night scheme
            self.SetBackgroundColour(parent.settings.skin.night_bgColor)

            # LED clock
            self.myled.SetForegroundColour(parent.settings.skin.digiClock.night_fgColor)
            self.myled.SetBackgroundColour(parent.settings.skin.digiClock.night_bgColor)
            self.myled.SetFadeColour(parent.settings.skin.digiClock.night_fadeColor)
            self.myled.SetFadeFactor(parent.settings.skin.digiClock.fadeFactor)
            
            # analog clock
            self.clock.SetHandBorderColour(parent.settings.skin.anaClock.night_handColor)
            self.clock.SetHandFillColour(parent.settings.skin.anaClock.night_handColor)
            self.clock.SetShadowColour(parent.settings.skin.anaClock.night_shadowColor)
            self.clock.SetBackgroundColour(parent.settings.skin.anaClock.night_bgColor)
            self.clock.SetTickBorderColour(parent.settings.skin.anaClock.night_tickColor)
            self.clock.SetTickFillColour(parent.settings.skin.anaClock.night_tickColor)
            self.clock.SetFaceBorderColour(parent.settings.skin.anaClock.night_faceBorderColor)
            self.clock.SetFaceFillColour(parent.settings.skin.anaClock.night_faceColor)

            self.Refresh()
