#! /usr/bin/env python

# Time-stamp: "2008-05-06 16:38:42 jantman"

import wx

# application includes
from TuxTruck_Settings import *

class TuxTruck_MainApp(wx.Frame):
    """The top-level frame for TuxTruck. This is the top-level component of the application"""
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '', style=wx.NO_BORDER)

        # variables holding state information
        self.currentColorScheme = "day"
        self.currentButton = ""

        # setup the main frame
        self.SetPosition(wx.Point(0,0))
        self.SetSize(settings.skin.topWindowSize)
        self.SetBackgroundColour(settings.skin.bgColor)
        if settings.skin.topWindowCentered == 1:
            self.CenterOnScreen()
        self.SetWindowStyle(wx.NO_BORDER)

        # DEBUG
        print settings.skin.butn_home_size
        # END

        # setup buttons
        self.butn_home = wx.Button(self, 1, 'Home', settings.skin.butn_home_pos, settings.skin.butn_home_size)
        self.butn_gps = wx.Button(self, 2, 'GPS', settings.skin.butn_gps_pos, settings.skin.butn_gps_size)
        self.butn_audio = wx.Button(self, 3, 'Audio', settings.skin.butn_audio_pos, settings.skin.butn_audio_size)

        # DEBUG - close button
        self.butn_close = wx.Button(self, 4, 'Close', (530, 410), (100, 70))
        # END DEBUG

        # bind buttons
        self.Bind(wx.EVT_BUTTON, self.OnClick_home, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnClick_gps, id=2)
        self.Bind(wx.EVT_BUTTON, self.OnClick_audio, id=3)

        # DEBUG - close button
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=4)
        # END DEBUG

    def OnClick_gps(self, event):
        print "GPS clicked"
        self.butn_gps.SetBackgroundColour(settings.skin.fgColor)
        self.Refresh()
        self.currentButton = "butn_gps"

    def OnClick_audio(self, event):
        print "Audio clicked"
        self.currentButton = "butn_audio"

    def OnClick_home(self, event):
        print "Home clicked"
        self.SetBackgroundColour('Yellow')
        self.Refresh()
        self.currentButton = "butn_home"

    def OnClose(self, event):
        frame.Close(True)        
    
# test it ...
if __name__ == '__main__':
    app = wx.App()
    settings = TuxTruck_Settings() # application-wide settings
    print "Loaded skin "+settings.skin.currentSkinName+" from file "+settings.skin.currentSkinFile
    frame = TuxTruck_MainApp(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
