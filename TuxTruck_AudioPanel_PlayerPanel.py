#! /usr/bin/env python
# TuxTruck Audio main frame
# Time-stamp: "2008-05-12 15:43:27 jantman"
# $Id: TuxTruck_AudioPanel_PlayerPanel.py,v 1.2 2008-05-12 19:42:57 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

# for pymp
import sys, os, fcntl, pygtk, gtk, gobject, time
import pymp-1.0.prefs, pymp-1.0.menu, pymp-1.0.remote, pymp-1.0.playlist, pymp-1.0.control, pymp-1.0.mplayer

class TuxTruck_AudioPanel_PlayerPanel(wx.Panel):
    """
    This is the audio player panel. It gives us an interface for playing audio files, podcasts, playlists, etc.
    """

    # TODO: update these from settings
    MPLAYER = os.path.expanduser("~/.mplayer")
    HOME = os.path.expanduser("~/.pymp")

    def __init__(self, parent, id):
        """
        Init function for the audio player panel.
        """
        wx.Panel.__init__(self, parent, id) # init the panel

        # setup the main frame
        self.SetPosition(wx.Point(60,0)) # set the main window position
        self.SetSize(wx.Size(740,420)) # set the main window size TODO: use settings
        #self.SetWindowStyle(wx.NO_BORDER) # set window style to have no border
        self.Hide()

	versionString = "Pymp v1.0"
	window, prefs, menu, remote = None, None, None, None
	playlist, control, mplayer = None, None, None

        #
        # begin pymp.py code
        #

        window = gtk.Window(gtk.WINDOW_TOPLEVEL)  #create window
        window.connect("destroy", self.quit)
        window.set_title(self.versionString)
        window.set_icon(self.getIcon())
		
        self.window = window
        
        self.prefs = prefs.Prefs(self)
        
        self.mplayer = mplayer.Mplayer(self)
        self.remote = remote.Remote(self)
        self.playlist = playlist.Playlist(self)
        self.control = control.Control(self)
        self.menu = menu.Menu(self)
		
        vbox = gtk.VBox(False, 0)
        vbox.pack_start(self.playlist.view, True, True, 0)
        vbox.pack_start(self.control.hbox, False, False, 0)
		
        window.add(vbox)  #prepare to start ui
        window.show_all()
		
        window.move(self.prefs.getInt("x"), self.prefs.getInt("y"))
        window.resize(self.prefs.getInt("width"), self.prefs.getInt("height"))
		
        if targets:  #process targets
            
            for t in targets:  #add each target
                self.playlist.add(t)
                
                if self.playlist.continuous:  #and begin playback
                    self.playlist.jump(0)
                    
		else:  #or load last list
                    self.playlist.loadm3u()
			
	gtk.main()
	
    #
    #  Returns a gtk.gdk.Pixbuf
    #
    def getIcon(self):
        
        icons = [sys.path[0] + "/../../share/pixmaps/pymp.png",	"./pymp.png"]  #for development
		
        for icon in icons:
            if os.access(icon, os.F_OK):
                return gtk.gdk.pixbuf_new_from_file(icon)
            
        return None
		
    #
    #  Terminates the application cleanly.
    #
    def quit(self, widget, data=None):
        
        self.mplayer.close()
        self.remote.close()
        self.playlist.save()
        self.prefs.save()
        gtk.main_quit()
		

    def reSkin(self, parent, colorSchemeName):
        # re-skin me
        
        if colorSchemeName == "day":
            # switch to day
            self.SetBackgroundColour(parent.settings.skin.day_bgColor)
            # DEBUG
            #self.SetBackgroundColour((0,255,0))
            # END DEBUG
        else:
            # switch to night
            self.SetBackgroundColour(parent.settings.skin.night_bgColor)
            # DEBUG
            #self.SetBackgroundColour((255,0,0))
            # END DEBUG
        self.Refresh()
