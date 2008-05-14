#! /usr/bin/env python
# TuxTruck Audio main frame
# Time-stamp: "2008-05-13 21:34:18 jantman"
# $Id: TuxTruck_AudioPanel_PlayerPanel.py,v 1.6 2008-05-14 03:31:47 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

#mplayer stuff
import sys, os, fcntl, gobject, time

STATUS_TIMEOUT = 10000

class TuxTruck_AudioPanel_PlayerPanel(wx.Panel):
    """
    This is the audio player panel. It gives us an interface for playing audio files, podcasts, playlists, etc.
    """

    # mplayer sample code
    pymp, mplayerIn, mplayerOut = None, None, None
    eofHandler, statusQuery = 0, 0
    paused = False
    # end mplayer sample code

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
        self.gauge1.SetRange(100) # just testing, this should be length in seconds
        
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

	
    def OnClick1(self, event):
        print "playing etta james"
        self.play("/home/jantman/cvs-temp/MP3test/ettaJames.mp3")
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
        self.pause()
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

        # BEGIN mplayer sample code

    def play(self, target):
        
        mpc = "mplayer -slave -quiet \"" + target + "\" 2>/dev/null"
        
        self.mplayerIn, self.mplayerOut = os.popen2(mpc)  #open pipe
        fcntl.fcntl(self.mplayerOut, fcntl.F_SETFL, os.O_NONBLOCK)
        
        self.startEofHandler()
        self.startStatusQuery()
        
	#
	#  Issues command to mplayer.
	#
    def cmd(self, command):
        
        if not self.mplayerIn:
            return
        
        try:
            self.mplayerIn.write(command + "\n")
            self.mplayerIn.flush()  #flush pipe
        except StandardError:
            return
        
	#
	#  Toggles pausing of the current mplayer job and status query.
	#
    def pause(self):
        
        if not self.mplayerIn:
            return
        
        if self.paused:  #unpause
            self.startStatusQuery()
            self.paused = False
            
        else:  #pause
            self.stopStatusQuery()
            self.paused = True
            
        self.cmd("pause")
		
	#
	#  Seeks the amount using the specified mode.  See mplayer docs.
	#
    def seek(self, amount, mode=0):
        self.pymp.mplayer.cmd("seek " + str(amount) + " " + str(mode))
        self.pymp.mplayer.queryStatus()
	
	#
	#  Cleanly closes any IPC resources to mplayer.
	#
    def close(self):
        
        if self.paused:  #untoggle pause to cleanly quit
            self.pause()
            
        self.stopStatusQuery()  #cancel query
        self.stopEofHandler()  #cancel eof monitor
        
        self.cmd("quit")  #ask mplayer to quit
            
        try:			
            self.mplayerIn.close()	 #close pipes
            self.mplayerOut.close()
        except StandardError:
            pass
			
        self.mplayerIn, self.mplayerOut = None, None
        self.gauge1.SetValue(0)  #reset bar
		
	#
	#  Triggered when mplayer's stdout reaches EOF.
	#
    def handleEof(self, source, condition):
        
        self.stopStatusQuery()  #cancel query
        
        self.mplayerIn, self.mplayerOut = None, None
        """
        if self.pymp.playlist.continuous:  #play next target
        self.pymp.playlist.next(None, None)
        else:  #reset progress bar
        self.pymp.control.setProgress(-1)
        """
        self.gauge1.SetValue(0)  #reset bar
        return False
		
	#
	#  Queries mplayer's playback status and upates the progress bar.
	#
    def queryStatus(self):
        
        self.cmd("get_percent_pos")  #submit status query
        self.cmd("get_time_pos")
        
        time.sleep(0.05)  #allow time for output
        
        line, percent, seconds = None, -1, -1
        
        while True:
            try:  #attempt to fetch last line of output
                line = self.mplayerOut.readline()
            except StandardError:
                break
            
            if not line: break

            print line
            
            if line.startswith("ANS_PERCENT_POSITION"):
                percent = int(line.replace("ANS_PERCENT_POSITION=", ""))
                self.gauge1.SetValue(percent)  #reset bar
                
            if line.startswith("ANS_TIME_POSITION"):
                seconds = float(line.replace("ANS_TIME_POSITION=", ""))

		#self.pymp.control.setProgress(percent, seconds)
        return True
		
	#
	#  Inserts the status query monitor.
	#
    def startStatusQuery(self):
        self.statusQuery = gobject.timeout_add(STATUS_TIMEOUT, self.queryStatus)
		
	#
	#  Removes the status query monitor.
	#
    def stopStatusQuery(self):
        if self.eofHandler:
            gobject.source_remove(self.statusQuery)
        self.statusQuery = 0
		
	#
	#  Inserts the EOF monitor.
	#
    def startEofHandler(self):
        self.eofHandler = gobject.io_add_watch(self.mplayerOut, gobject.IO_HUP, self.handleEof)
	
	#
	#  Removes the EOF monitor.
	#
    def stopEofHandler(self):
        if self.eofHandler:
            gobject.source_remove(self.eofHandler)
            self.eofHandler = 0
