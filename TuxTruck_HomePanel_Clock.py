#! /usr/bin/env python
# TuxTruck clock panel for home view
# Time-stamp: "2008-05-07 16:11:32 jantman"
# $Id: TuxTruck_HomePanel_Clock.py,v 1.1 2008-05-07 20:13:45 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

# the clocks came from http://xoomer.alice.it/infinity77/main/SpeedMeter.html

import wx # import wx for the GUI
import wx.lib.buttons
from math import pi, sqrt

import SpeedMeter as SM

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

        #
        # BEGIN CLOCK CODE FROM SpeedMeter Demo
        #
        # Second SpeedMeter: We Use The Following Styles:
        #
        # SM_DRAW_HAND: We Want To Draw The Hand (Arrow) Indicator
        # SM_DRAW_SECTORS: Full Sectors Will Be Drawn, To Indicate Different Intervals
        # SM_DRAW_MIDDLE_TEXT: We Draw Some Text In The Center Of SpeedMeter
        # SM_DRAW_SECONDARY_TICKS: We Draw Secondary (Intermediate) Ticks Between
        #                          The Main Ticks (Intervals)
        # SM_DRAW_PARTIAL_FILLER: The Region Passed By The Hand Indicator Is Highlighted
        #                         With A Different Filling Colour
        # SM_DRAW_SHADOW: A Shadow For The Hand Indicator Is Drawn
        
        self.SpeedWindow2 = SM.SpeedMeter(self,
                                          extrastyle=SM.SM_DRAW_HAND |
                                          SM.SM_DRAW_SECTORS |
                                          SM.SM_DRAW_MIDDLE_TEXT |
                                          SM.SM_DRAW_SECONDARY_TICKS |
                                          SM.SM_DRAW_PARTIAL_FILLER |
                                          SM.SM_DRAW_SHADOW
                                          )

        # We Want To Simulate A Clock. Somewhat Tricky, But Did The Job
        self.SpeedWindow2.SetAngleRange(pi/2, 5*pi/2)

        intervals = range(0, 13)
        self.SpeedWindow2.SetIntervals(intervals)

        colours = [wx.SystemSettings_GetColour(0)]*12
        self.SpeedWindow2.SetIntervalColours(colours)

        ticks = [str(interval) for interval in intervals]
        ticks[-1] = ""
        ticks[0] = "12"
        self.SpeedWindow2.SetTicks(ticks)
        self.SpeedWindow2.SetTicksColour(wx.BLUE)
        self.SpeedWindow2.SetTicksFont(wx.Font(11, wx.SCRIPT, wx.NORMAL, wx.BOLD, True))
        self.SpeedWindow2.SetNumberOfSecondaryTicks(4)

        # Set The Colour For The External Arc        
        self.SpeedWindow2.SetArcColour(wx.BLUE)

        self.SpeedWindow2.SetHandColour(wx.BLACK)

        self.SpeedWindow2.SetMiddleText("0 s")
        self.SpeedWindow2.SetMiddleTextColour(wx.RED)

        # We Set The Background Colour Of The SpeedMeter OutSide The Control
        self.SpeedWindow2.SetSpeedBackground(wx.WHITE)

        # Set The Colour For The Shadow
        self.SpeedWindow2.SetShadowColour(wx.Colour(128, 128, 128))        

        self.SpeedWindow2.SetSpeedValue(0.0)
        
        # These Are Cosmetics For The Second SpeedMeter Control
        
        # Create The Timer For The Clock
        self.timer = wx.PyTimer(self.ClockTimer)
        self.currvalue = 0

        bsizer2 = wx.BoxSizer(wx.VERTICAL)
        bsizer2.Add(self.SpeedWindow2, 1, wx.EXPAND)        
        self.SetSizer(bsizer2)

        self.timer.Start()

        #
        # End SpeedMeter Demo Code
        #

    def ClockTimer(self):
        if self.currvalue >= 59:
            self.currvalue = 0
        else:
            self.currvalue = self.currvalue + 1

        self.SpeedWindow2.SetMiddleText(str(self.currvalue) + " s")            
        self.SpeedWindow2.SetSpeedValue(self.currvalue/5.0)


    def setBgColor(self, mycolor):
        """
        This is called on a skin change to update my background color
        """
        self.SetBackgroundColour(mycolor)
