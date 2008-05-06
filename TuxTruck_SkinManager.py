# skin manager test

import wx

class TuxTruck_SkinManager:
    "Provides interface to all of the skin data"

    currentSkinName = "" # declare it empty
    currentSkinFile = "" # declare it empty

    bgColor = "" # declare it empty
    fgColor = "" # declare it empty
    highlightColor = "" # declare it empty
    topWindowSize = 0

    def loadSkin(self, name, file):
        # load the skin with given name at given location

        # DEBUG
        self.currentSkinName = name
        self.currentSkinFile = file
        self.bgColor = wx.Colour(22,127,230)
        self.fgColor = wx.Colour(3,90,166)
        self.highlightColor = wx.Colour(211,235,253)
        self.topWindowSize = wx.Size(800, 480)

    def __init__(self, parent):
        #get the default skin name and file from settings
        #load the skin file. make changes to default, anything not specified stays default
        self.loadSkin("TestSkin", "testSkin.nofile")
    
