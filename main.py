#! /usr/bin/env python

import wx

# application includes
from TuxTruck_Settings import *

class TuxTruck_MainApp(wx.Frame):
    """The top-level frame for TuxTruck. This is the top-level component of the application"""
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '', style=wx.NO_BORDER)

        # setup the main frame
        self.SetPosition(wx.Point(0,0))
        self.SetSize(settings.skin.topWindowSize)
        self.SetBackgroundColour(settings.skin.bgColor)
        self.CenterOnScreen()
        self.SetWindowStyle(wx.NO_BORDER)

        # setup buttons
        self.butn_home = wx.Button(self, 1, 'Home', (10, 410), (70, 100))
        self.butn_gps = wx.Button(self, 2, 'GPS', (120, 410), (70, 100))
        self.butn_close = wx.Button(self, 3, 'Close', (230, 410), (70, 100))

        # bind buttons
        self.Bind(wx.EVT_BUTTON, self.OnClick_home, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnClick_gps, id=2)
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=3)

    def OnClick_gps(self, event):
        print "GPS clicked"
        self.butn_gps.SetBackgroundColour(settings.skin.fgColor)
        self.Refresh()

    def OnClick_home(self, event):
        print "Home clicked"
        self.SetBackgroundColour('Yellow')
        self.Refresh()

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
