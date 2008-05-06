#! /usr/bin/env python

# Time-stamp: "2008-05-06 19:04:44 jantman"

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

        # load the button images
        self.loadButtonImages()

        # create buttons
        # buttons also have to be added to switchColorScheme and setButtonsColor
        self.butn_home = wx.BitmapButton(self, id=1, bitmap=self.butn_home_image, pos=settings.skin.butn_home_pos, size = (self.butn_home_image.GetWidth(), self.butn_home_image.GetHeight()))
        self.butn_gps = wx.BitmapButton(self, id=2, bitmap=self.butn_gps_image, pos=settings.skin.butn_gps_pos, size = (self.butn_gps_image.GetWidth(), self.butn_gps_image.GetHeight()))
        self.butn_audio = wx.BitmapButton(self, id=3, bitmap=self.butn_audio_image, pos=settings.skin.butn_audio_pos, size = (self.butn_audio_image.GetWidth(), self.butn_audio_image.GetHeight()))
        self.butn_obd = wx.BitmapButton(self, id=4, bitmap=self.butn_obd_image, pos=settings.skin.butn_obd_pos, size = (self.butn_obd_image.GetWidth(), self.butn_obd_image.GetHeight()))
        self.butn_phone = wx.BitmapButton(self, id=5, bitmap=self.butn_phone_image, pos=settings.skin.butn_phone_pos, size = (self.butn_phone_image.GetWidth(), self.butn_phone_image.GetHeight()))
        self.butn_tools = wx.BitmapButton(self, id=6, bitmap=self.butn_tools_image, pos=settings.skin.butn_tools_pos, size = (self.butn_tools_image.GetWidth(), self.butn_tools_image.GetHeight()))
        self.butn_weather = wx.BitmapButton(self, id=7, bitmap=self.butn_weather_image, pos=settings.skin.butn_weather_pos, size = (self.butn_weather_image.GetWidth(), self.butn_weather_image.GetHeight()))

        # bind buttons
        self.Bind(wx.EVT_BUTTON, self.OnClick_home, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnClick_gps, id=2)
        self.Bind(wx.EVT_BUTTON, self.OnClick_audio, id=3)
        self.Bind(wx.EVT_BUTTON, self.OnClick_obd, id=4)
        self.Bind(wx.EVT_BUTTON, self.OnClick_phone, id=5)
        self.Bind(wx.EVT_BUTTON, self.OnClick_tools, id=6)
        self.Bind(wx.EVT_BUTTON, self.OnClick_weather, id=7)


        # set initial button
        self.currentButton = self.butn_home
        

    def OnClick_gps(self, event):
        print "GPS clicked" # DEBUG
        self.currentButton = self.butn_gps

    def OnClick_audio(self, event):
        print "Audio clicked" # DEBUG
        self.currentButton = self.butn_audio

    def OnClick_home(self, event):
        print "Home clicked" # DEBUG
        self.switchColorScheme()
        self.currentButton = self.butn_home

    def OnClick_obd(self, event):
        print "obd clicked" # DEBUG
        self.currentButton = self.butn_obd

    def OnClick_phone(self, event):
        print "phone clicked" # DEBUG
        self.currentButton = self.butn_phone

    def OnClick_tools(self, event):
        print "tools clicked" # DEBUG
        self.currentButton = self.butn_tools

    def OnClick_weather(self, event):
        print "weather clicked" # DEBUG
        self.currentButton = self.butn_weather

    def setButtonImages(self, colorSchemeName):
        """ sets all buttons to the specified color"""
        if colorSchemeName == "day":
            # set day images
            print "day" # DEBUG
        else:
            # set night images
            print "night" # DEBUG

    def switchColorScheme(self):
        """ does everything needed to switch color schemes"""
        if self.currentColorScheme == "day":
            # TODO - make night images
            print "night mode not setup, need to make images"
            self.SetBackgroundColour(settings.skin.night_bgColor)
            self.currentColorScheme = "night"
            self.Refresh()
        else:

            self.SetBackgroundColour(settings.skin.bgColor)
            self.currentColorScheme = "day"
            self.Refresh()
            
    def loadButtonImages(self):
        """Load all of the button images"""
        self.butn_home_image = wx.Image(settings.skin.buttonImagePath+"home.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_audio_image = wx.Image(settings.skin.buttonImagePath+"audio.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_gps_image = wx.Image(settings.skin.buttonImagePath+"gps.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_obd_image = wx.Image(settings.skin.buttonImagePath+"obd.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_phone_image = wx.Image(settings.skin.buttonImagePath+"phone.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_tools_image = wx.Image(settings.skin.buttonImagePath+"tools.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_weather_image = wx.Image(settings.skin.buttonImagePath+"weather.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_home_active_image = wx.Image(settings.skin.buttonImagePath+"home_active.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_audio_active_image = wx.Image(settings.skin.buttonImagePath+"audio_active.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_gps_active_image = wx.Image(settings.skin.buttonImagePath+"gps_active.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_obd_active_image = wx.Image(settings.skin.buttonImagePath+"obd_active.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_phone_active_image = wx.Image(settings.skin.buttonImagePath+"phone_active.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_tools_active_image = wx.Image(settings.skin.buttonImagePath+"tools_active.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.butn_weather_active_image = wx.Image(settings.skin.buttonImagePath+"weather_active.gif", wx.BITMAP_TYPE_ANY).ConvertToBitmap()


# test it ...
if __name__ == '__main__':
    app = wx.App()
    settings = TuxTruck_Settings() # application-wide settings
    print "Loaded skin "+settings.skin.currentSkinName+" from file "+settings.skin.currentSkinFile
    frame = TuxTruck_MainApp(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
