#!/usr/bin/env python

import sys, os, fcntl, pygtk, gtk, gobject, time

import prefs, menu, remote, playlist, control, mplayer

MPLAYER = os.path.expanduser("~/.mplayer")
HOME = os.path.expanduser("~/.pymp")

#
#  The Python Media Player main class.
#
class Pymp:
	
	versionString = "Pymp v1.0"
	window, prefs, menu, remote = None, None, None, None
	playlist, control, mplayer = None, None, None
	
	#
	#  Returns a gtk.gdk.Pixbuf
	#
	def getIcon(self):
		
		icons = [sys.path[0] + "/../../share/pixmaps/pymp.png",
			"./pymp.png"]  #for development
		
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
		
	#
	#  Initializes and the player and its components.
	#
	def __init__(self, targets):
		
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
#  Ensure preferenecs directory exists and create Pymp instance.
#
def main():
	
	if not os.access(MPLAYER, os.F_OK | os.W_OK):
		os.mkdir(MPLAYER)  #create mplayer directory
	
	if not os.access(HOME, os.F_OK | os.W_OK):
		os.mkdir(HOME)  #create prefs directory
		
	if not remote.remote(sys.argv):
		Pymp(sys.argv[1:])  #create new Pymp
	
main()  #start the program

#End of file
