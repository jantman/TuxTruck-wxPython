#! /usr/bin/env python

# Time-stamp: "2008-05-06 16:59:18 jantman"

import wx

# application includes
from TuxTruck_Settings import *

class TuxTruck_MainApp(wx.Frame):
    """The top-level frame for TuxTruck. This is the top-level component of the application"""

    # variables holding state
    currentColorScheme = "day"
    currentButton = ""

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '', style=wx.NO_BORDER)

        # setup the main frame
        self.SetPosition(wx.Point(0,0))
        self.SetSize(settings.skin.topWindowSize)
        self.SetBackgroundColour(settings.skin.bgColor)
        if settings.skin.topWindowCentered == 1:
            self.CenterOnScreen()
        self.SetWindowStyle(wx.NO_BORDER)

        # create buttons
        # buttons also have to be added to switchColorScheme and setButtonsColor
        self.butn_home = wx.Button(self, 1, 'Home', settings.skin.butn_home_pos, settings.skin.butn_home_size)
        self.butn_gps = wx.Button(self, 2, 'GPS', settings.skin.butn_gps_pos, settings.skin.butn_gps_size)
        self.butn_audio = wx.Button(self, 3, 'Audio', settings.skin.butn_audio_pos, settings.skin.butn_audio_size)

        # bind buttons
        self.Bind(wx.EVT_BUTTON, self.OnClick_home, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnClick_gps, id=2)
        self.Bind(wx.EVT_BUTTON, self.OnClick_audio, id=3)


    def OnClick_gps(self, event):
        print "GPS clicked" # DEBUG
        self.butn_gps.SetBackgroundColour(settings.skin.fgColor)
        self.Refresh()
        self.currentButton = "butn_gps"

    def OnClick_audio(self, event):
        print "Audio clicked" # DEBUG
        self.currentButton = "butn_audio"

    def OnClick_home(self, event):
        print "Home clicked" # DEBUG
        self.switchColorScheme()
        self.currentButton = "butn_home"

    def setButtonsColor(self, buttonColor, textColor):
        """ sets all buttons to the specified color"""
        self.butn_home.SetBackgroundColour(buttonColor)
        self.butn_home.SetForegroundColour(textColor)
        self.butn_home.Refresh()
        self.butn_gps.SetBackgroundColour(buttonColor)
        self.butn_gps.SetForegroundColour(textColor)
        self.butn_audio.SetBackgroundColour(buttonColor)
        self.butn_audio.SetForegroundColour(textColor)

    def switchColorScheme(self):
        if self.currentColorScheme == "day":
            self.setButtonsColor(settings.skin.night_fgColor, settings.skin.night_highlightColor)
            self.SetBackgroundColour(settings.skin.night_bgColor)
            self.currentColorScheme = "night"
            self.Refresh()
        else:
            self.setButtonsColor(settings.skin.fgColor, settings.skin.highlightColor)
            self.SetBackgroundColour(settings.skin.bgColor)
            self.currentColorScheme = "day"
            self.Refresh()

# test it ...
if __name__ == '__main__':
    app = wx.App()
    settings = TuxTruck_Settings() # application-wide settings
    print "Loaded skin "+settings.skin.currentSkinName+" from file "+settings.skin.currentSkinFile
    frame = TuxTruck_MainApp(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
