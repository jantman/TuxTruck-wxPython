#! /usr/bin/env python
# TuxTruck Playlist
# Time-stamp: "2008-05-15 14:22:08 jantman"
# $Id: TuxTruck_Playlist.py,v 1.1 2008-05-15 18:27:20 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/


class TuxTruck_Playlist():
    """
    This handles *all* playlist-related functions.
    """

    # this is our playlist, stored as (displayName, path) tuples.
    playlist = {}


    def __init__(self, parent):
        # here, we should really load the last playlist, or a default one.
        print "playlist init"

        self.parent = parent

    def BuildPlaylist(self):
        # DEBUG
        self.playlist[0] = ('Etta James - Son of a Preacher Man', '/home/jantman/cvs-temp/MP3test/ettaJames.mp3')
        self.playlist[1] = ('S-Etta James - Son of a Preacher Man', '/home/jantman/cvs-temp/MP3test/ettaJames-short.mp3')
        self.playlist[2] = ('Bob Dylan - Aint Talkin', '/home/jantman/cvs-temp/MP3test/BobDylan-ModernTimes-10-AintTalkin.mp3')
        self.playlist[3] = ('S-Bob Dylan - Aint Talkin', '/home/jantman/cvs-temp/MP3test/BobDylan-short.mp3')
        self.playlist[4] = ('Tom Lehrer - Wernher Von Braun', '/home/jantman/cvs-temp/MP3test/WernherVonBraun.ogg')
        self.playlist[5] = ('S-Tom Lehrer - Wernher Von Braun', '/home/jantman/cvs-temp/MP3test/WernherVonBraun-short.ogg')

    def GetFileLocation(self, playlistPos):
        return self.playlist[playlistPos][1]

    def GetFileTitle(self, playlistPos):
        return self.playlist[playlistPos][0]
