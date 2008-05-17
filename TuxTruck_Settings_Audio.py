# TuxTruck Skin Manager
# Time-stamp: "2008-05-17 18:11:01 jantman"
# $Id: TuxTruck_Settings_Audio.py,v 1.3 2008-05-17 22:20:28 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx

# NOTE: This depends on elementtree from <http://effbot.org/zone/element-index.htm>
from elementtree import ElementTree

# TODO: write out settings

class TuxTruck_Settings_Audio:
    """
    This class handles reading and writing all of the settings related to audio playing.
    """

    def loadSkin(self, parent, file):
        """
        This function loads a new skin by reading and parsing the file, and then
        updating the variables in this class. The skin is specified by a file, in the
        path specified in the class documentation. It only updates the variables here,
        and doesn't make any changes to the GUI.
        NOTE: The size of buttons is exactly the size of the image used for the button.
        """

        # TODO: parse the XML and read the values
        audioTree = ElementTree.parse(file).getroot()

        self.mp3root = audioTree.findtext("mp3root")
        self.playlistroot = audioTree.findtext("playlistroot")
        self.podcastroot = audioTree.findtext("podcastroot")
        

    def __init__(self, parent, file):
        """
        Here, we get the default skin name from settings, then load that file.
        This must happen before we build any of the GUI.
        """

        self.loadSkin(parent, file) # load the file
