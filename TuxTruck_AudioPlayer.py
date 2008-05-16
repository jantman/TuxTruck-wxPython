#! /usr/bin/env python
# TuxTruck Audio Player
# Time-stamp: "2008-05-16 00:25:12 jantman"
# $Id: TuxTruck_AudioPlayer.py,v 1.5 2008-05-16 04:25:52 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import sys, os, fcntl, time, gobject
from threading import Timer
from os import path
from ContinuousTimer import *

import id3reader


STATUS_TIMEOUT = 1 # in seconds

class TuxTruck_AudioPlayer():
    """
    This is the audio player. It handles playing audio files, podcasts, playlists, etc.
    """

    pymp, mplayerIn, mplayerOut = None, None, None
    eofHandler, statusQuery = 0, 0
    paused = False

    _currentSongPath = ""
    _currentSongLength = 0
    _currentSongName = ""
    _currentSongArtist = ""
    _currentSongAlbum = ""

    __currentlyPlaying = False

    #doStatusQueries = False

    def __init__(self, parent, id):
        self.parent = parent
        #self.statusQuery = Timer(STATUS_TIMEOUT, self.queryStatus) # timer for status queries
        

    def play(self, target):
        
        # if currently playing, stop
        if self.__currentlyPlaying == True:
            print "already playing. TODO this may be a problem."
            self.close()

        try:
            if os.path.exists(target):
                self._currentSongPath = target

                mpc = "mplayer -slave -idle -quiet \"" + target + "\" 2>/dev/null"
        
                self.statusQuery = ContinuousTimer(self, self.queryStatus, STATUS_TIMEOUT) #
        
                self.mplayerIn, self.mplayerOut = os.popen2(mpc)  #open pipe
                print "opened pipe in play"
                fcntl.fcntl(self.mplayerOut, fcntl.F_SETFL, os.O_NONBLOCK)
                print "ran fcntl in play"
                
                # wait for startup output
                time.sleep(0.05)

                self.GetSongInfo()
                print "ran getSongInfo from play"
                
                self.startEofHandler()
                print "ran startEofHandler from play"
                self.startStatusQuery()
                print "ran startStatusQuery from play"
                self.__currentlyPlaying = True
                
            else:
                print "File "+target+" does not exist, not playing."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        
    #
    #  Get length in seconds of current song
    #
    def GetSongInfo(self):
        self.cmd("get_time_length")
        # TODO: these don't seem to be working...
        #self.cmd("get_meta_artist")
        #self.cmd("get_meta_title")
        #self.cmd("get_meta_album")
        #self.cmd("get_meta_genre")
        
        time.sleep(0.05)  #allow time for output
        
        line, seconds = None, -1

        while True:
            try:  #attempt to fetch last line of output
                line = self.mplayerOut.readline()
            except StandardError:
                break

            if not line: break

            print "LINE: ", line

            if line.startswith("ANS_LENGTH"):
                seconds = float(line.replace("ANS_LENGTH=", ""))
                self._currentSongLength = seconds
                self.parent.SetSongLength(seconds) # update progress bar DEBUG commented out debugging segfault

        # Construct a reader from a file or filename.
        try:
            id3r = id3reader.Reader(self._currentSongPath)
            # Ask the reader for ID3 values:
            self._currentSongName = id3r.getValue('title')
            self._currentSongArtist = id3r.getValue('performer')
            self._currentSongAlbum = id3r.getValue('album')
        except id3reader.Id3Error, message:
            print "Id3Error: ", message

        print "Length:", seconds

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

        self.__currentlyPlaying = False
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
        self._currentSongPath = ""
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
        self._currentSongPath = ""
        self.__currentlyPlaying = False
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

            #print line

            if line.startswith("ANS_TIME_POSITION"):
                seconds = float(line.replace("ANS_TIME_POSITION=", ""))
                self.parent.updateProgressBar(seconds) # update progress bar

        print "query status done."

        if seconds == -1:
            # PLAYING has STOPPED. stop the status queries.
            print "NO SECONDS."
            self.statusQuery.stop()

        return True

		
    #
    #  Inserts the status query monitor.
    #
    def startStatusQuery(self):
        print "running startStatusQuery"
        self.statusQuery = ContinuousTimer(self, self.queryStatus, STATUS_TIMEOUT) #
        self.statusQuery.start()
        #self.statusQuery = gobject.timeout_add(STATUS_TIMEOUT, self.queryStatus)
        #self.doStatusQueries = True;
        print "startStatusQuery done."
		
    #
    #  Removes the status query monitor.
    #
    def stopStatusQuery(self):
        print "running stopStatusQuery"
        if self.statusQuery:
            #gobject.source_remove(self.statusQuery)
            self.statusQuery.stop()
            print "statusQuery stopped"
            self.statusQuery = None
            #self.doStatusQueries = False
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