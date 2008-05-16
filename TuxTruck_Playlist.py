#! /usr/bin/env python
# TuxTruck Playlist
# Time-stamp: "2008-05-16 01:15:25 jantman"
# $Id: TuxTruck_Playlist.py,v 1.3 2008-05-16 05:15:47 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/


class TuxTruck_Playlist():
    """
    This handles *all* playlist-related functions. Specifically, this loads playlists and provides methods to access the file titles (as displayed in the GUI) and paths, as well as getting the next path and file.
    """

    # this is our playlist, stored as (displayName, path) tuples.
    playlist = {}

    def __init__(self, parent):
        # TODO: here, we should really load the last playlist, or a default one.
        self.parent = parent

    def BuildPlaylist(self):
        """
        This builds a playlist. DEBUG - this is HARD CODED.
        """
        # DEBUG
        self.playlist[0] = ('Etta James - Son of a Preacher Man (Pulp Fiction Soundtrack)', '/home/jantman/cvs-temp/MP3test/ettaJames.mp3')
        self.playlist[1] = ('S-Etta James - Son of a Preacher Man (Pulp Fiction Soundtrack)', '/home/jantman/cvs-temp/MP3test/ettaJames-short.mp3')
        self.playlist[2] = ('Bob Dylan - Aint Talkin (Modern Times)', '/home/jantman/cvs-temp/MP3test/BobDylan-ModernTimes-10-AintTalkin.mp3')
        self.playlist[3] = ('S-Bob Dylan - Aint Talkin (Modern Times)', '/home/jantman/cvs-temp/MP3test/BobDylan-short.mp3')
        self.playlist[4] = ('Tom Lehrer - Wernher Von Braun', '/home/jantman/cvs-temp/MP3test/WernherVonBraun.ogg')
        self.playlist[5] = ('S-Tom Lehrer - Wernher Von Braun', '/home/jantman/cvs-temp/MP3test/WernherVonBraun-short.ogg')

    def GetFilePath(self, playlistPos):
        """
        This function returns the path to the playlist entry number specified by playlistPos, as stored in the playlist.
        """
        return self.playlist[playlistPos][1]

    def GetFileTitle(self, playlistPos):
        """
        This method returns the title of the playlist entry number specified by playlistPos. It should be a "title" suitable for direct display in the GUI - most likely, a string including the title, artist, and album.
        """
        return self.playlist[playlistPos][0]
