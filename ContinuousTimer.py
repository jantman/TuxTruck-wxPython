#! /usr/bin/env python
# Continuous timer for TuxTruck
# Time-stamp: "2008-05-16 01:06:28 jantman"
# $Id: ContinuousTimer.py,v 1.3 2008-05-16 05:15:47 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

from threading import Timer

class ContinuousTimer():
    """
    This class implements a Timer from the threading module that keeps running at the specified interval until the stop() method is called.
    Class is initialized like ContinuousTimer(self, interval) from a parent class. self becomes "parent" in ContinuousTimer class, and interval is the timer interval in SECONDS.
    """

    INTERVAL = 1 # interval in seconds
    __function = None # callback function, specified in __init__
    __stopped = True # handles telling whether we're stopped, so we don't create a new timer after canceling the current one.

    def __init__(self, parent, function, interval):
        """
        initiate ContinuousTimer. parent is my parent, interval is interval in seconds.
        """
        self.parent = parent
        self.INTERVAL = interval
        self.__function = function

    def start(self):
        """
        This starts the timer.
        """
        self.__stopped = False
        self.t = Timer(self.INTERVAL, self.timeEnd)
        self.t.start()

    def timeEnd(self):
        """
        INTERNAL USE ONLY - on timeout, calls parent callback function and starts a new timer.
        """
        
        # call the parent callback function
        self.__function()
        # make sure it's not stopped before we start a new one
        if self.__stopped == False:
            self.t = Timer(self.INTERVAL, self.timeEnd)
            self.t.start()

    def stop(self):
        """
        This stops the timer.
        """
        self.__stopped = True
        if self.t:
            self.t.cancel()

