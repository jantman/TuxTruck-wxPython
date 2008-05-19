#! /usr/bin/env python
# TuxTruck Playlist Builder
# Time-stamp: "2008-05-19 02:08:27 jantman"
# $Id: buildPlaylist.py,v 1.2 2008-05-19 06:08:50 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

"""
This script updates all of the playlists for newly added files.
"""

import os

import id3reader

from TuxTruck_Settings import * # import TuxTruck_Settings to get user settings
from TuxTruck_Playlist import *

# global variables
settings = TuxTruck_Settings() # initiate the settings object
MP3_ROOT = settings.audio.mp3root # the root directory for all audio files
PLAYLIST_ROOT = settings.audio.playlistroot # the root directory for all playlists

paths_to_check = [MP3_ROOT, ] # need to check the root path

fileExtensions = ['mp3', 'MP3', 'ogg', 'OGG'] # list of file extensions to put in playlists

print "playlist root="+PLAYLIST_ROOT
print "MP3 root="+MP3_ROOT

def testPlaylist(fpath, displayName, title, artist, album, genre):
    # DEBUG ONLY
    playlist = TuxTruck_Playlist(None, PLAYLIST_ROOT)

    # DEBUG
    fname = title.replace(" ", "_")
    # END DEBUG

    playlist.CreateBlankPlaylist(os.path.join(PLAYLIST_ROOT, fname+".ttpl"), fname, "path")
    playlist.AddEntry(fpath, displayName, title, artist, album, genre)
    playlist.WriteCurrentPlaylist()

def handleMP3(fpath, fname):
    """
    This function is called every time we identify a new MP3 file
    """
    print "handleMP3 called. path="+fpath+" file="+fname # DEBUG

    # TODO: This is a hack because MPlayer doesn't give us what we need.
    # Read the rest of the information from the file directly, since MPlayer isn't telling us

    absolutePath = MP3_ROOT+fpath # this is the actual (absolute path)

    print os.path.join(absolutePath, fname)

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

    testPlaylist(os.path.join(absolutePath, fname), displayName, title, artist, album, genre)

def handleOGG(fpath,fname):
    """
    This function is called every time we identify a new OGG file.
    """
    print "handleOGG called. path="+fpath+" file="+fname # DEBUG

def isNewFile(fpath,fname):
    """
    This function searches the playlist for a directory and checks whether the specified fname is new or not.
    """
    print "isNewFile called. path="+fpath+" file="+fname # DEBUG

    # TODO: parse the playlist for directory `fpath` and see if this file is in it. If it is in the playlist, return false. else return true.

    return True


def checkPath(fpath):
    """
    Handle all files and subdirectories in path.
    """

    #print "Checking Path "+fpath+" ..." # DEBUG

    paths_to_check.remove(fpath) # remove this path from the list of paths to check

    # add all files in a path to the appropriate playlists.
    # add subdirs to paths_to_check list

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

            if isNewFile(fpath,fname):
                # this is a file we haven't seen before, handle it

                if extension == "mp3" or extension == "MP3":
                    # handle the file as an MP3
                    handleMP3(fpath,fname)
                elif extension == "ogg" or extension == "OGG":
                    # handle the file as an OGG
                    handleOGG(fpath,fname)



# main loop. checks paths until paths_to_check is empty
while len(paths_to_check) > 0:
    checkPath(paths_to_check[0]) # check the first path in the list
