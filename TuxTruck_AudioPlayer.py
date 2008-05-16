#! /usr/bin/env python
# TuxTruck Audio Player
# Time-stamp: "2008-05-16 01:08:53 jantman"
# $Id: TuxTruck_AudioPlayer.py,v 1.6 2008-05-16 05:15:47 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import sys, os, fcntl, time, gobject
from threading import Timer
from os import path
from ContinuousTimer import *

import id3reader


# TODO: this needs to be optimized to keep status updates looking like realtime, but not putting too much load on the system.
STATUS_TIMEOUT = 1 # in seconds


class TuxTruck_AudioPlayer():
    """
    This is the audio player. It handles playing audio files, podcasts, playlists, etc.
    """

    pymp, mplayerIn, mplayerOut = None, None, None
    eofHandler, statusQuery = 0, 0
    paused = False

    # local variables to store state
    _currentSongPath = ""
    _currentSongLength = 0
    _currentSongName = ""
    _currentSongArtist = ""
    _currentSongAlbum = ""

    __currentlyPlaying = False # this is used to tell whether to first call close() when play() is called.
    # close() should be called whenever we're in the middle of a job.

    def __init__(self, parent, id):
        self.parent = parent

    def play(self, target):
        """
        This function handles playing of a file. All play requests should come through here. It quits the currently running session, if needed, cleans up, and plays a file.
        """
        
        if self.__currentlyPlaying == True:
            # if currently playing, quit and cleanup
            self.close()

        try:
            # check to make sure the file exists. if so, play it
            if os.path.exists(target):
                self._currentSongPath = target # update the variable holding the current path

                mpc = "mplayer -slave -idle -quiet \"" + target + "\" 2>/dev/null" # command to run mplayer in slave mode
                # NOTE: -idle keeps mplayer running after the file is done.
                # this is a hack to prevent the whole program from SegFault'ing when the file ends and MPlayer HUPs
        
                self.statusQuery = ContinuousTimer(self, self.queryStatus, STATUS_TIMEOUT) # this will time to check status
        
                self.mplayerIn, self.mplayerOut = os.popen2(mpc)  #open pipe
                fcntl.fcntl(self.mplayerOut, fcntl.F_SETFL, os.O_NONBLOCK)
                
                # wait for startup output
                time.sleep(0.05)

                self.GetSongInfo()
                
                self.startStatusQuery()
                self.__currentlyPlaying = True
                
            else:
                print "File "+target+" does not exist, not playing."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        
    def GetSongInfo(self):
        """
        This gets some basic song information, like length, for the GUI.
        """
        # TODO: this still has intermittent failures of not reading the value.
        self.cmd("get_time_length")
        
        time.sleep(0.1)  #allow time for output
        
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

        # TODO: This is a hack because MPlayer doesn't give us what we need.
        # Read the rest of the information from the file directly, since MPlayer isn't telling us
        try:
            id3r = id3reader.Reader(self._currentSongPath)
            # Ask the reader for ID3 values:
            self._currentSongName = id3r.getValue('title')
            self._currentSongArtist = id3r.getValue('performer')
            self._currentSongAlbum = id3r.getValue('album')
        except id3reader.Id3Error, message:
            print "Id3Error: ", message

        return True

    def cmd(self, command):
        """
        This function handles sending commands to MPlayer.
        """

        if not self.mplayerIn:
            return
        
        try:
            self.mplayerIn.write(command + "\n")
            self.mplayerIn.flush()  #flush pipe
        except StandardError:
            return
        
    def pause(self):
        """
        This function toggles pausing of the current mplayer job, as well as the statusQuery timer.
        """
        if not self.mplayerIn:
            return
        
        if self.paused:  #unpause
            self.startStatusQuery()
            self.paused = False
            
        else:  #pause
            self.stopStatusQuery()
            self.paused = True
            
        self.cmd("pause")
		
    def seek(self, amount, mode=0):
        """
        This seeks the specified amount in the current file, and also updates the status.
        """
        self.cmd("seek " + str(amount) + " " + str(mode))
        self.queryStatus()
	
    def close(self):
        """
        This cleanly closes any IPC resources to mplayer. It is called when playback finishes, as well as when starting playback of a new file when mplayer is in the middle of a job.
        """
        if self.paused:  #untoggle pause to cleanly quit
            self.pause()

        self.__currentlyPlaying = False
        self.stopStatusQuery()  #cancel query
        
        self.cmd("quit")  #ask mplayer to quit
            
        try:			
            self.mplayerIn.close()	 #close pipes
            self.mplayerOut.close()
        except StandardError:
            pass
			
        self.mplayerIn, self.mplayerOut = None, None

        self.parent.updateProgressBar(0) # reset progress bar

        # reset all local variables
        self._currentSongPath = ""
        self._currentSongLength = 0
        self._currentSongName = ""
        self._currentSongArtist = ""
        self._currentSongAlbum = ""
				
    def queryStatus(self):
        """
        This function queries MPlayer's status when running and updates the progress bar on the parent panel.
        """

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

        if seconds == -1:
            # PLAYING has STOPPED. stop the status queries.
            self.statusQuery.stop()

        return True

		
    def startStatusQuery(self):
        """
        This function starts the statusQuery timer.
        """
        self.statusQuery = ContinuousTimer(self, self.queryStatus, STATUS_TIMEOUT) #
        self.statusQuery.start()
		
    def stopStatusQuery(self):
        """
        This function stops the statusQuery timer and cleans it up
        """
        if self.statusQuery:
            self.statusQuery.stop()
            self.statusQuery = None
		
