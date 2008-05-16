#! /usr/bin/env python
# Continuous timer for TuxTruck
# Time-stamp: "2008-05-15 23:26:15 jantman"
# $Id: ContinuousTimer.py,v 1.1 2008-05-16 03:25:20 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

from threading import Timer

class ContinuousTimer():
    """
    This class implements a Timer from the threading module that keeps running at the specified interval until the stop() method is called.
    """

    INTERVAL = 1 # interval in seconds

    def __init__(self, parent):
        
