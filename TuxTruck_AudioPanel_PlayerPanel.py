#! /usr/bin/env python
# TuxTruck Audio main frame
# Time-stamp: "2008-05-13 21:15:00 jantman"
# $Id: TuxTruck_AudioPanel_PlayerPanel.py,v 1.5 2008-05-14 01:14:32 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

class TuxTruck_AudioPanel_PlayerPanel(wx.Panel):
    """
    This is the audio player panel. It gives us an interface for playing audio files, podcasts, playlists, etc.
    """

    def __init__(self, parent, id):
        """
        Init function for the audio player panel.
        """
        wx.Panel.__init__(self, parent, id) # init the panel

        # setup the main frame
        self.SetPosition(wx.Point(60,0)) # set the main window position
        self.SetSize(wx.Size(740,420)) # set the main window size TODO: use settings
        #self.SetWindowStyle(wx.NO_BORDER) # set window style to have no border
        self.Hide()

	versionString = "Pymp v1.0"
	window, prefs, menu, remote = None, None, None, None
	playlist, control = None, None

        # DEBUG
        self.gauge1 = wx.Gauge(self, -1)
        self.gauge1.SetSize((400,20))
        self.gauge1.SetPosition((50,200))
        self.gauge1.SetRange(210) # just testing, this should be length in seconds
        
        #self.pause = wx.BitmapButton(self, -1, wx.Bitmap('icons/stock_media-pause.png'))
        #self.play  = wx.BitmapButton(self, -1, wx.Bitmap('icons/stock_media-play.png'))
        # END DEBUG


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

        #self.remote = remote.Remote(self)
        #self.playlist = playlist.Playlist(self)
        #self.control = control.Control(self)
        #self.menu = menu.Menu(self)
		
        #vbox = gtk.VBox(False, 0)
        #vbox.pack_start(self.playlist.view, True, True, 0)
        #vbox.pack_start(self.control.hbox, False, False, 0)
		
        #window.add(vbox)  #prepare to start ui
        #window.show_all()
		
        #window.move(self.prefs.getInt("x"), self.prefs.getInt("y"))
        #window.resize(self.prefs.getInt("width"), self.prefs.getInt("height"))
		
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
    # DEBUG
    def sliderUpdate(self, event):
        print "Slider1 changed:"
        print self.slider1.GetValue()
    # END DEBUG

	
    def OnClick1(self, event):
        print "playing etta james"
        self.mplayer.play("/home/jantman/cvs-temp/mp3-test/ettaJames.mp3")
        print "playing..."

    def OnClick2(self, event):
        print "playing bob dylan"
        self.mplayer.play("/home/jantman/cvs-temp/mp3-test/BobDylan-ModernTimes-10-AintTalkin.mp3")
        print "playing..."

    def OnClick3(self, event):
        print "playing tom lehrer .ogg"
        self.mplayer.play("/home/jantman/cvs-temp/mp3-test/WernherVonBraun.ogg")
        print "playing..."

    def OnClick4(self, event):
        print "pausing..."
        self.mplayer.pause()
        print "paused"

    def OnClick5(self, event):
        print "seeking +5"
        self.gauge1.SetValue(self.gauge1.GetValue()+1)
        #self.mplayer.seek(5)
        print "seeked"

    def OnClick6(self, event):
        print "seeking -5"
        #self.mplayer.seek(-5)
        self.gauge1.SetValue(self.gauge1.GetValue()-1)
        print "seeked"


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
