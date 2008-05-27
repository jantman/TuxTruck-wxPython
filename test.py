#!/usr/bin/env python

# TuxTruck testing file - used to test functions before addition to mainline code
# NOTICE - this is used to test simple (non object-oriented) functions ONLY
# Time-stamp: "2008-05-27 14:11:52 jantman"
# $Id: test.py,v 1.2 2008-05-27 18:23:08 jantman Exp $

import re
import elementtree.ElementTree as ET

def makeValidFilename(s):
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

def makePlaylistFilename(s):
    """
    This function formats a string (such as an artist name or album name) as a playlist file. It converts it to a lower case string containing only the characters [a-z],[0-9],"-","_", and ".". It also appends the ".ttpl" extension. A single, double, or back quote is simply removed, everything else invalid is replaced with a dash, and spaces are replaced with underscores.
    """
    s = makeValidFilename(s) # call makeValidFilename to handle most of the replacements
    s = s.lower() # convert to lower case
    s = s+".ttpl" # append ".ttpl"
    return s


def IsInPlaylist(filepath):
    """
    Returns TRUE if the playlist located at playlistFile contains a (song) entry containing exactly filepath as its "filepath" field content. Otherwise returns false.
    """
    tree = ET.parse("/home/jantman/cvs-temp/MP3test/EttaJames/dir.ttpl")
    root = tree.getroot()
    songs = root.find("songs")
    songsIter = songs.getiterator()

    for entry in songsIter:
        if entry.findtext('filepath') == filepath:
            return True
    return False
    

print IsInPlaylist("/EttaJames/ettaJames.mp3")

testStr = "file Name / hi \ & $ % # ^ @ ! hi.*"
print testStr
print "filename: "+makeValidFilename(testStr)
print "playlist: "+makePlaylistFilename(testStr)
print "---------------------------------"
testStr = "The B-52's"
print testStr
print "filename: "+makeValidFilename(testStr)
print "playlist: "+makePlaylistFilename(testStr)
print "---------------------------------"
testStr = "ALICEc\"ooper"
print testStr
print "filename: "+makeValidFilename(testStr)
print "playlist: "+makePlaylistFilename(testStr)
print "---------------------------------"
testStr = "JanIcE  JoPlIn"
print testStr
print "filename: "+makeValidFilename(testStr)
print "playlist: "+makePlaylistFilename(testStr)
print "---------------------------------"
testStr = "The Beatle's"
print testStr
print "filename: "+makeValidFilename(testStr)
print "playlist: "+makePlaylistFilename(testStr)
print "---------------------------------"
testStr = "Tom LehreR"
print testStr
print "filename: "+makeValidFilename(testStr)
print "playlist: "+makePlaylistFilename(testStr)
print "---------------------------------"
testStr = ".T*oby    K%it#"
print testStr
print "filename: "+makeValidFilename(testStr)
print "playlist: "+makePlaylistFilename(testStr)
print "---------------------------------"
testStr = "......tim   McGraw"
print testStr
print "filename: "+makeValidFilename(testStr)
print "playlist: "+makePlaylistFilename(testStr)
print "---------------------------------"
