#! /usr/bin/env python
# TuxTruck Audio main frame
# Time-stamp: "2008-05-27 13:11:24 jantman"
# $Id: TuxTruck_AudioPanel_PlayerPanel.py,v 1.14 2008-05-27 18:23:08 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

#mplayer stuff
#import sys, os, fcntl, gobject, time

# TODO: document this code. remove debugging stuff.

from TuxTruck_AudioPlayer import *

from TuxTruck_Playlist import *

class TuxTruck_AudioPanel_PlayerPanel(wx.Panel):
    """
    This is the audio player panel. It gives us an interface for playing audio files, podcasts, playlists, etc.
    """

    # mplayer sample code
    pymp, mplayerIn, mplayerOut = None, None, None
    eofHandler, statusQuery = 0, 0
    paused = False
    # end mplayer sample code

    _currentPlaylistPosition = -1

    def __init__(self, parent, id):
        """
        Init function for the audio player panel.
        """
        wx.Panel.__init__(self, parent, id) # init the panel

        self.parent = parent

        # setup the playlist
        self.playlist = TuxTruck_Playlist(self, parent.parent.settings.audio.playlistroot) # TODO this is a hack, need program-wide globals
        #self.playlist.BuildPlaylist() # DEBUG ONLY

        # setup the main frame
        self.SetPosition(wx.Point(60,0)) # set the main window position
        self.SetSize(wx.Size(740,420)) # set the main window size TODO: use settings
        #self.SetWindowStyle(wx.NO_BORDER) # set window style to have no border
        self.Hide()

        self.mplayer = TuxTruck_AudioPlayer(self, -1)

        # DEBUG
        self.gauge1 = wx.Gauge(self, -1)
        self.gauge1.SetSize((400,20))
        self.gauge1.SetPosition((50,200))
        self.gauge1.SetRange(100) # just testing, this should be length in seconds

        # DEBUG text area
        self.textBox = wx.TextCtrl(self, -1, '', style=wx.TE_LEFT)
        self.textBox.SetPosition((100,300))
        self.textBox.SetSize((500,50))

        # THE LIST BOX (DEBUG)

        # DEBUG
        # these are buttons to test mplayer
        self.button1 = wx.Button(self, -1, "Play etta", (100,10), (60,50))
        self.button1.Bind(wx.EVT_BUTTON, self.OnClick1)
        self.button2 = wx.Button(self, -1, "Play bob", (150,10), (60,50))
        self.button2.Bind(wx.EVT_BUTTON, self.OnClick2)
        self.button3 = wx.Button(self, -1, "Play tom", (200,10), (60,50))
        self.button3.Bind(wx.EVT_BUTTON, self.OnClick3)
        self.button4 = wx.Button(self, -1, "Play pause", (250,10), (60,50))
        self.button4.Bind(wx.EVT_BUTTON, self.OnClick4)
        self.button5 = wx.Button(self, -1, "skip+", (300,10), (60,50))
        self.button5.Bind(wx.EVT_BUTTON, self.OnClick5)
        self.button6 = wx.Button(self, -1, "skip-", (350,10), (60,50))
        self.button6.Bind(wx.EVT_BUTTON, self.OnClick6)
        # END DEBUG

		
        """
        if targets:  #process targets
            
            for t in targets:  #add each target
                self.playlist.add(t)
                
                if self.playlist.continuous:  #and begin playback
                    self.playlist.jump(0)
                    
		else:  #or load last list
                    self.playlist.loadm3u()
			
	gtk.main()
        """

	
    def OnClick1(self, event):
        self.mplayer.play(self.playlist.GetFilePath(0))

    def OnClick2(self, event):
        self.mplayer.play("/home/jantman/cvs-temp/MP3test/BobDylan-short.mp3")

    def OnClick3(self, event):
        self.mplayer.play("/home/jantman/cvs-temp/MP3test/WernherVonBraun-short.ogg")

    def OnClick4(self, event):
        self.mplayer.pause()

    def OnClick5(self, event):
        self.mplayer.seek(5)
        #print self.playlist.GetFileTitle(3)

    def OnClick6(self, event):
        self.mplayer.seek(-5)
        #print self.playlist.GetFilePath(3)


    def reSkin(self, parent, colorSchemeName):
        # re-skin me
        
        if colorSchemeName == "day":
            # switch to day
            self.SetBackgroundColour(parent.settings.skin.day_bgColor)
            # DEBUG
            #self.SetBackgroundColour((0,255,0))
            # END DEBUG
        else:
            # switch to night
            self.SetBackgroundColour(parent.settings.skin.night_bgColor)
            # DEBUG
            #self.SetBackgroundColour((255,0,0))
            # END DEBUG
        self.Refresh()

        # BEGIN mplayer sample code

    # DEBUG: got rid of progress bar updates trying to fix segfault

    def updateProgressBar(self, progressValue):
        """
        This function called from mplayer class to update the progress bar
        """
        self.gauge1.SetValue(progressValue)

    def SetSongLength(self, lengthSec):
        """
        This function called from mplayer class to set progress bar length in seconds.
        """
        self.gauge1.SetRange(lengthSec)
        # DEBUG
        self._currentPlaylistPosition = 3
        # END DEBUG
        self.textBox.SetValue(self.playlist.GetFileTitle(self._currentPlaylistPosition))
