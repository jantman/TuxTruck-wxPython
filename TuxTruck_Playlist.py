#! /usr/bin/env python
# TuxTruck Playlist
# Time-stamp: "2008-05-27 16:23:58 jantman"
# $Id: TuxTruck_Playlist.py,v 1.7 2008-05-27 20:23:34 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

# NOTE: This depends on elementtree from <http://effbot.org/zone/element-index.htm>
import elementtree.ElementTree as ET
import os
import re

class TuxTruck_Playlist():
    """
    This handles *all* playlist-related functions. Specifically, this loads playlists and provides methods parse and write the playlist XML files.
    """

    current_file = ""
    playlistROOT = None # this will be the elementtree root node
    playlistTREE = None # this will be the full elementtree tree
    playlist_root_path = "" # as found in settings/audio

    songsROOT = None # this is the elementtree root for the songs entries

    def __init__(self, parent, playlistroot):
        # TODO: here, we should really load the last playlist, or a default one.
        self.parent = parent
        self.playlist_root_path = playlistroot

    def ReadPlaylist(self, file_path):
        """
        This function reads in a playlist and parses it. After calling this, you can get the individual entries. file_path is the *absolute* path to the playlist file.
        """
        #print "Reading playlist from "+file_path # DEBUG
        self.current_file = file_path # TODO: but only if reading it works
        self.playlistTREE = ET.parse(file_path)
        self.playlistROOT = self.playlistTREE.getroot()
        self.songsROOT = self.playlistROOT.find("songs")
        

    def IsInPlaylist(self, filepath):
        """
        Returns TRUE if the playlist located at playlistFile contains a (song) entry containing exactly filepath as its "filepath" field content. Otherwise returns false.
        """

        # TODO: create a GetSongByName() function

        songsIter = self.songsROOT.getiterator()
        
        for entry in songsIter:
            if entry.findtext('filepath') == filepath:
                return True
        return False

    def WriteCurrentPlaylist(self):
        """
        This function WRITES the current playlist changes to the playlist file. It's mainly used when building a new playlist, to write the complete tree, or when updating the rank of a file. Path is absolute.
        """
        #print "Writing playlist to "+self.current_file # debug

        # wrap it in an ElementTree instance, and save as XML
        tree = ET.ElementTree(self.playlistROOT)
        tree.write(self.current_file)

    def GetEntryByPos(self, pos):
        """
        This gets an entry by position number in the playlist. Takes the integer position as an argument, returns a 3-tuple (pos (int), filepath (string), displayName (string)). File path is relative to MP3_ROOT.
        """

    def GetNextEntry(self):
        """
        This function returns the next entry in the playlist. It returns a 3-tuple (pos (int), filepath (string), displayName (string)). filepath is relative to MP3_ROOT.
        """

    def AddEntry(self, filepath, displayName, title, artist, album, genre):
        """
        This function adds an entry to the current playlist. All entry information is specified as arguments - please see the playlist documentation for an explanation of the fields. Any fields that do not have an appropriate value should be sent as an empty string - "". WriteCurrentPlaylist() must be called to write out the playlist to the file.
        """

        #print "Adding entry with displayName "+displayName+" and filepath="+filepath+" to "+self.current_file # DEBUG

        entry = ET.SubElement(self.songsROOT, "playlist_entry")
        filepathElem = ET.SubElement(entry, "filepath")
        filepathElem.text = filepath
        displayNameElem = ET.SubElement(entry, "displayName")
        displayNameElem.text = displayName
        if title != "":
            titleElem = ET.SubElement(entry, "title")
            titleElem.text = title
        if artist != "":
            artistElem = ET.SubElement(entry, "artist")
            artistElem.text = artist
        if album != "":
            albumElem = ET.SubElement(entry, "album")
            albumElem.text = album
        if genre != "":
            genreElem = ET.SubElement(entry, "genre")
            genreElem.text = genre

    def CreateBlankPlaylist(self, filepath, name, type):
        """
        This function creates a skeleton of a blank playlist, ready for adding entries to (for use when building playlists from disk files). Entries are added with AddEntry(). When finished, it is written to disk with WriteCurrentPlaylist(). Arguments are filepath, name and type as seen in the playlist documentation. Path is absolute.
        """
        # TODO: also include playlist name, type, etc.

        self.current_file = filepath # where we'll save to

        self.playlistROOT = ET.Element("TuxTruck_Playlist") # create the root node

        typeElem = ET.SubElement(self.playlistROOT, "type")
        typeElem.text = type
        nameElem = ET.SubElement(self.playlistROOT, "name")
        nameElem.text = name

        self.songsROOT = ET.SubElement(self.playlistROOT, "songs")

        #print "CreateBlankPlaylist name="+name+" type="+type+" path="+filepath # DEBUG

    def ReadOrCreatePlaylist(self, filepath, name, type):
        """
        This function is used by playlist builders. If the specified path exists, it reads it in. If not, it creates it. Filepath is an absolute path.
        """

        #print "ReadOrCreatePlaylist name="+name+" type="+type+" path="+filepath # DEBUG

        if os.path.exists(filepath):
            self.ReadPlaylist(filepath)
        else:
            self.CreateBlankPlaylist(filepath, name, type)

    def ChangeRank(self, rank):
        """
        This function changes the integer rank of the current file. Rank should be an int, either -1, 0, or 1.
        """

        # TODO: implement this
        
        WriteCurrentPlaylist() # write out the changes immediately.

    def MakePlaylistFilename(self, s):
           """
           This function formats a string (such as an artist name or album name) as a playlist file. It converts it to a lower case string containing only the characters [a-z],[0-9],"-","_", and ".". It also appends the ".ttpl" extension. A single, double, or back quote is simply removed, everything else invalid is replaced with a dash, and spaces are replaced with underscores.
           """
           s = self.MakeValidFilename(s) # call makeValidFilename to handle most of the replacements
           s = s.lower() # convert to lower case
           s = s+".ttpl" # append ".ttpl"
           return s

    def MakeValidFilename(self, s):
        """
        This functions converts a string to a valid filename. All it does is make sure the string only contains the characters [a-z],[0-9],"-","_", and ".". A single, double, or back quote is simply removed, everything else invalid is replaced with a dash, and spaces are replaced with underscores.
        """
        while s[0] == ".":
            # remove leading dots
            s = s[1:]
        s = re.sub(" +", "_", s) # replace space with _
        s = s.replace("'", "") # replace ' with nothing
        s = s.replace("\"", "") # replace " with nothing
        s = s.replace("`", "") # replace ` with nothing
        # replace everything else with -
        return s
