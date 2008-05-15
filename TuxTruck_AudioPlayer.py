#! /usr/bin/env python
# TuxTruck Audio Player
# Time-stamp: "2008-05-15 13:27:56 jantman"
# $Id: TuxTruck_AudioPlayer.py,v 1.2 2008-05-15 17:28:33 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import sys, os, fcntl, time, gobject
from threading import Timer

STATUS_TIMEOUT = 1 # in seconds

class TuxTruck_AudioPlayer():
    """
    This is the audio player. It handles playing audio files, podcasts, playlists, etc.
    """

    pymp, mplayerIn, mplayerOut = None, None, None
    eofHandler, statusQuery = 0, 0
    paused = False

    _currentSongLength = 0
    _currentSongName = ""
    _currentSongArtist = ""
    _currentSongAlbum = ""

    doStatusQueries = False

    def __init__(self, parent, id):
        self.parent = parent
        self.statusQuery = Timer(STATUS_TIMEOUT, self.queryStatus) # timer for status queries

    def play(self, target):
        
        try:
            if os.path.exists(target):
                mpc = "mplayer -slave -quiet \"" + target + "\" 2>/dev/null"
                
                self.mplayerIn, self.mplayerOut = os.popen2(mpc)  #open pipe
                print "opened pipe in play"
                fcntl.fcntl(self.mplayerOut, fcntl.F_SETFL, os.O_NONBLOCK)
                print "ran fcntl in play"
                
                # wait for startup output
                time.sleep(0.05)

                self.getSongInfo()
                print "ran getSongInfo from play"
                
                self.startEofHandler()
                print "ran startEofHandler from play"
                self.startStatusQuery()
                print "ran startStatusQuery from play"
                
            else:
                print "File "+target+" does not exist, not playing."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        
    #
    #  Get length in seconds of current song
    #
    def getSongInfo(self):
        self.cmd("get_time_length")
        
        time.sleep(0.05)  #allow time for output
        
        line, seconds = None, -1

        while True:
            try:  #attempt to fetch last line of output
                line = self.mplayerOut.readline()
            except StandardError:
                break

            if not line: break

            if line.startswith("ANS_LENGTH"):
                seconds = float(line.replace("ANS_LENGTH=", ""))
                self._currentSongLength = seconds
                self.parent.SetSongLength(seconds) # update progress bar DEBUG commented out debugging segfault

        return True


    #
    #  Issues command to mplayer.
    #
    def cmd(self, command):
        print "running cmd with command "+command
        if not self.mplayerIn:
            return
        
        try:
            self.mplayerIn.write(command + "\n")
            self.mplayerIn.flush()  #flush pipe
        except StandardError:
            return

        print "cmd done."
        
    #
    #  Toggles pausing of the current mplayer job and status query.
    #
    def pause(self):
        print "running pause"
        if not self.mplayerIn:
            return
        
        if self.paused:  #unpause
            self.startStatusQuery()
            self.paused = False
            
        else:  #pause
            self.stopStatusQuery()
            self.paused = True
            
        self.cmd("pause")
        print "pause done"
		
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
        print "running close"
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
        self.parent.updateProgressBar(0) # reset progress bar
        self._currentSongLength = 0
        self._currentSongName = ""
        self._currentSongArtist = ""
        self._currentSongAlbum = ""
        print "close done"
		
    #
    #  Triggered when mplayer's stdout reaches EOF.
    #
    def handleEof(self, source, condition):
        print "running handleEof"
        self.stopStatusQuery()  #cancel query
        
        self.mplayerIn, self.mplayerOut = None, None
        """
        if self.pymp.playlist.continuous:  #play next target
        self.pymp.playlist.next(None, None)
        else:  #reset progress bar
        self.pymp.control.setProgress(-1)
        """
        self.parent.updateProgressBar(0) # reset progress bar
        self._currentSongLength = 0
        self._currentSongName = ""
        self._currentSongArtist = ""
        self._currentSongAlbum = ""
        print "eof done"
        return False
		
    #
    #  Queries mplayer's playback status and upates the progress bar.
    #
    def queryStatus(self):
        print "running queryStatus"
        self.cmd("get_time_pos")
        
        time.sleep(0.05)  #allow time for output
        
        line, percent, seconds = None, -1, -1
        
        while True:
            try:  #attempt to fetch last line of output
                line = self.mplayerOut.readline()
            except StandardError:
                break
            
            if not line: break

            if line.startswith("ANS_TIME_POSITION"):
                seconds = float(line.replace("ANS_TIME_POSITION=", ""))
                self.parent.updateProgressBar(seconds) # update progress bar

        print "query status done."
        #self.statusQuery.start() # do it again. and again. and again...
        return True

		
    #
    #  Inserts the status query monitor.
    #
    def startStatusQuery(self):
        print "running startStatusQuery"
        self.statusQuery.start()
        #self.statusQuery = gobject.timeout_add(STATUS_TIMEOUT, self.queryStatus)
        self.doStatusQueries = True;
        print "startStatusQuery done."
		
    #
    #  Removes the status query monitor.
    #
    def stopStatusQuery(self):
        print "running stopStatusQuery"
        if self.statusQuery:
            #gobject.source_remove(self.statusQuery)
            self.statusQuery.cancel()
            self.doStatusQueries = False
        print "stopStatusQuery done."
		
    #
    #  Inserts the EOF monitor.
    #
    def startEofHandler(self):
        print "running startEofHandler"
        #self.eofHandler = wx.Timer(self)
        #self.Bind(wx.EVT_TIMER, self.handleEof, self.eofHandler)
        #self.timer.Start()
        self.eofHandler = gobject.io_add_watch(self.mplayerOut, gobject.IO_HUP, self.handleEof)
        print "startEofHandler done."
	
    #
    #  Removes the EOF monitor.
    #
    def stopEofHandler(self):
        print "running stopEofHandler"
        if self.eofHandler:
            gobject.source_remove(self.eofHandler)
            self.eofHandler = 0
        print "stopEofHandler done."
