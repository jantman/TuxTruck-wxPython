#! /usr/bin/env python
# TuxTruck Audio Player
# Time-stamp: "2008-05-15 11:07:12 jantman"
# $Id: TuxTruck_AudioPlayer.py,v 1.1 2008-05-15 15:08:14 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import sys, os, fcntl, gobject, time

STATUS_TIMEOUT = 10000

class TuxTruck_AudioPlayer():
    """
    This is the audio player. It handles playing audio files, podcasts, playlists, etc.
    """

    pymp, mplayerIn, mplayerOut = None, None, None
    eofHandler, statusQuery = 0, 0
    paused = False

    def __init__(self, parent, id):
        self.parent = parent

    def play(self, target):
        
        if os.path.exists(target):
            mpc = "mplayer -slave -quiet \"" + target + "\" 2>/dev/null"
        
            self.mplayerIn, self.mplayerOut = os.popen2(mpc)  #open pipe
            fcntl.fcntl(self.mplayerOut, fcntl.F_SETFL, os.O_NONBLOCK)

            getSongLengthSec()
        
            self.startEofHandler()
            self.startStatusQuery()
            
        else:
            print "File "+target+" does not exist, not playing."
        
    #
    #  Get length in seconds of current song
    #
    def getSongLengthSec(self):
        
        #self.cmd("get_percent_pos")  #submit status query
        self.cmd("get_time_length")
        
        time.sleep(0.05)  #allow time for output
        
        line, seconds = None, -1
        
        while True:
            try:  #attempt to fetch last line of output
                line = self.mplayerOut.readline()
            except StandardError:
                break
            
            if not line: break

            # DEBUG
            print line
            # END DEBUG
            
            if line.startswith("ANS_PERCENT_POSITION"):
                percent = int(line.replace("ANS_PERCENT_POSITION=", ""))
                
                #self.gauge1.SetValue(percent)  #reset bar
                
            if line.startswith("ANS_TIME_POSITION"):
                seconds = float(line.replace("ANS_TIME_POSITION=", ""))
                parent.updateProgressBar(seconds) # update progress bar
		#self.pymp.control.setProgress(percent, seconds)
        return True


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
        parent.updateProgressBar(0) # reset progress bar
        return False
		
    #
    #  Queries mplayer's playback status and upates the progress bar.
    #
    def queryStatus(self):
        
        #self.cmd("get_percent_pos")  #submit status query
        self.cmd("get_time_pos")
        
        time.sleep(0.05)  #allow time for output
        
        line, percent, seconds = None, -1, -1
        
        while True:
            try:  #attempt to fetch last line of output
                line = self.mplayerOut.readline()
            except StandardError:
                break
            
            if not line: break

            # DEBUG
            print line
            # END DEBUG
            
            if line.startswith("ANS_PERCENT_POSITION"):
                percent = int(line.replace("ANS_PERCENT_POSITION=", ""))
                
                #self.gauge1.SetValue(percent)  #reset bar
                
            if line.startswith("ANS_TIME_POSITION"):
                seconds = float(line.replace("ANS_TIME_POSITION=", ""))
                parent.updateProgressBar(seconds) # update progress bar
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
