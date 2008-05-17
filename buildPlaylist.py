#! /usr/bin/env python
# TuxTruck Playlist Builder
# Time-stamp: "2008-05-17 18:20:05 jantman"
# $Id: buildPlaylist.py,v 1.1 2008-05-17 22:20:28 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

"""
This script updates all of the playlists for newly added files.
"""

from TuxTruck_Settings import * # import TuxTruck_Settings to get user settings
settings = TuxTruck_Settings() # initiate the settings object
MP3_ROOT = settings.audio.mp3root # the root directory for all audio files
PLAYLIST_ROOT = settings.audio.playlistroot # the root directory for all playlists

print "playlist root="+PLAYLIST_ROOT
print "MP3 root="+MP3_ROOT
