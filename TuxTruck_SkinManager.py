# skin manager test

import wx

class TuxTruck_SkinManager:
    "Provides interface to all of the skin data"

    # current skin information
    currentSkinName = "" # declare it empty
    currentSkinFile = "" # declare it empty

    # primary (day) color scheme
    bgColor = "" # declare it empty
    fgColor = "" # declare it empty
    highlightColor = "" # declare it empty

    # secondary (night) color scheme
    night_bgColor = ""
    night_fgColor = ""
    night_highlightColor = ""

    # main window settings
    topWindowSize = 0
    topWindowPos = 0
    topWindowCentered = 0

    #buttons
    butn_home_size = (0, 0)
    butn_home_pos = (0, 0)
    butn_gps_size = (0, 0)
    butn_gps_pos = (0, 0)
    butn_audio_size = (0, 0)
    butn_audio_pos = (0, 0)

    def loadSkin(self, name, file):
        # load the skin with given name at given location

        # DEBUG TEST SETTINGS
        self.currentSkinName = name
        self.currentSkinFile = file

        self.bgColor = wx.Colour(22,127,230)
        self.fgColor = wx.Colour(3,90,166)
        self.highlightColor = wx.Colour(211,235,253)

        # DEBUG as a test, just swap colors
        self.night_bgColor = wx.Colour(3,90,166)
        self.night_fgColor = wx.Colour(22,127,230)
        self.night_highlightColor = wx.Colour(0,0,0)

        self.topWindowSize = wx.Size(800, 480)
        self.topWindowPos = wx.Size(100,100)
        self.topWindowCentered = 1

        self.butn_home_size = (100, 70)
        self.butn_home_pos = (10, 410)
        self.butn_gps_size = (100, 70)
        self.butn_gps_pos = (110, 410)
        self.butn_audio_size = (100, 70)
        self.butn_audio_pos = (210, 410)

    def __init__(self, parent):
        #get the default skin name and file from settings
        #load the skin file. make changes to default, anything not specified stays default
        self.loadSkin("TestSkin", "testSkin.nofile")
    
