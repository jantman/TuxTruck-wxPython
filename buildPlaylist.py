#! /usr/bin/env python
# TuxTruck Playlist Builder
# Time-stamp: "2008-05-27 14:20:49 jantman"
# $Id: buildPlaylist.py,v 1.4 2008-05-27 18:23:08 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

"""
This script updates all of the playlists for newly added files.
"""

import os
import id3reader

# TuxTruck imports

from TuxTruck_Settings import * # import TuxTruck_Settings to get user settings
from TuxTruck_Playlist import *

# global variables
settings = TuxTruck_Settings() # initiate the settings object
MP3_ROOT = settings.audio.mp3root # the root directory for all audio files
PLAYLIST_ROOT = settings.audio.playlistroot # the root directory for all playlists
playlist_ALL = None # the master playlist of ALL songs
playlist_dir = None # directory-specific playlist

paths_to_check = [MP3_ROOT, ] # list of paths to check, prime with MP3_ROOT

fileExtensions = ['mp3', 'MP3', 'ogg', 'OGG'] # list of file extensions to put in playlists



"""
playlist.CreateBlankPlaylist(os.path.join(PLAYLIST_ROOT, fname+".ttpl"), fname, "path")
playlist.AddEntry(fpath, displayName, title, artist, album, genre)
playlist.WriteCurrentPlaylist()
"""

def handleMP3(fpath, fname):
    """
    This function is called every time we identify a new MP3 file. It handles reading the ID3 tag and then adding the file to the appropriate playlists.
    """
    global playlist_ALL
    global playlist_dir
    global MP3_ROOT
    global PLAYLIST_ROOT
    print "handleMP3 called. path="+fpath+" file="+fname # DEBUG

    # TODO: This is a hack because MPlayer doesn't give us what we need.
    # Read the rest of the information from the file directly, since MPlayer isn't telling us

    absolutePath = MP3_ROOT+fpath # this is the actual (absolute path)

    print os.path.join(absolutePath, fname)
    print os.path.join(fpath, fname)

    relPath = os.path.join(absolutePath, fname).replace(MP3_ROOT, "")
    print relPath

    try:
        id3r = id3reader.Reader(os.path.join(absolutePath, fname))
        print "reading ID3 from "+os.path.join(absolutePath, fname)
        # Ask the reader for ID3 values:
        title = id3r.getValue('title')
        artist = id3r.getValue('performer')
        album = id3r.getValue('album')
        genre = id3r.getValue('genre')
        #displayName = artist+" - "+title+" ("+album+")"
        displayName = ""
        if artist != None:
            displayName = displayName + artist + " - "
        if title != None:
            displayName = displayName + title
        if album != None:
            displayName = displayName + " ("+album+")"
    except id3reader.Id3Error, message:
        print "Id3Error: ", message
        displayName = fname
        title = ""
        artist = ""
        album = ""
        genre = ""

    # add to directory playlist and write it out.
    playlist_dir.AddEntry(os.path.join(fpath, fname), displayName, title, artist, album, genre)
    playlist_dir.WriteCurrentPlaylist()

    # add to ALL playlist and write it out.
    playlist_ALL.AddEntry(os.path.join(fpath, fname), displayName, title, artist, album, genre)
    playlist_ALL.WriteCurrentPlaylist()

    # if we got an artist name, add it to the artist playlist
    if artist != "":
        temp = TuxTruck_Playlist(None, PLAYLIST_ROOT)
        playlist.CreateBlankPlaylist(os.path.join(PLAYLIST_ROOT, fname+".ttpl"), fname, "path")
        playlist.AddEntry(fpath, displayName, title, artist, album, genre)
        playlist.WriteCurrentPlaylist()

def handleOGG(fpath,fname):
    """
    This function is called every time we identify a new OGG file. It adds the file to the appripriate playlists.
    TOSO: How do we get artist, album, song name, etc.?
    """
    print "handleOGG called. path="+fpath+" file="+fname # DEBUG

def checkPath(fpath):
    """
    Handle all files and subdirectories in path. This finds the files in the specified directory, calls handleMP3 or handleOGG on them, and then adds subdirectories to paths_to_check.
    """
    global playlist_dir

    paths_to_check.remove(fpath) # remove this path from the list of paths to check

    # read in or create the directory-specific playlist
    playlist_dir = TuxTruck_Playlist(None, fpath)
    playlist_dir.ReadOrCreatePlaylist(fpath+"/dir.ttpl", fpath, "path")

    dirList=os.listdir(fpath)

    for fname in dirList:
        if os.path.isdir(os.path.join(fpath,fname)):
            # is a directory, add to paths_to_check
            paths_to_check.append(os.path.join(fpath,fname))
        else:
            # is a file
            extension = fname[fname.rfind(".")+1:] # get the file extension

            # convert paths from absolute to relative
            fpath = fpath.replace(MP3_ROOT, '')

            if not playlist_dir.IsInPlaylist(os.path.join(fpath, fname)):
                # TODO: left off here
                # this is a file we haven't seen before, handle it

                if extension == "mp3" or extension == "MP3":
                    # handle the file as an MP3
                    handleMP3(fpath,fname)
                elif extension == "ogg" or extension == "OGG":
                    # handle the file as an OGG
                    handleOGG(fpath,fname)


# load the ALL playlist
playlist_ALL = TuxTruck_Playlist(None, PLAYLIST_ROOT)
playlist_ALL.ReadOrCreatePlaylist(os.path.join(PLAYLIST_ROOT, "all.ttpl"), "ALL", "ALL")

# main loop. checks paths, starting at MP3_ROOT, until paths_to_check is empty
while len(paths_to_check) > 0:
    checkPath(paths_to_check[0]) # check the first path in the list
