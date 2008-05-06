#!/usr/bin/env python

import os, ConfigParser

PREFSFILE = os.path.expanduser("~/.pymp/preferences")

#
#  Implements storage and retrieval of GMP preferences.
#
class Prefs:
	
	pymp, parser = None, None
	
	defaults = { 
		"x" : "50",
		"y" : "50",
		"width" : "380",
		"height" : "100", 
		"continuous" : "True",
		"random" : "False",
		"repeat" : "False",
		"path" : os.path.expanduser("~/")
	}
	
	#
	#  Instantiates a new Prefs with the options from STORE.
	#
	def __init__(self, pymp):
		
		self.pymp = pymp
		
		self.parser = ConfigParser.SafeConfigParser(self.defaults)
		
		try:
			self.parser.read([PREFSFILE,])
		except StandardError:
			return
		
	#
	#  A convenience method for retrieving an option.
	#
	def get(self, option):
		return self.parser.get("DEFAULT", option)
		
	#
	#  A convenience method for retrieving an integer option.
	#
	def getInt(self, option):
		return int(self.parser.get("DEFAULT", option))
		
	#
	#  A convenience method for retrieving a boolean option.
	#
	def getBool(self, option):
		return self.parser.get("DEFAULT", option) == "True"
		
	#
	#  A convenience method for setting an option.
	#
	def set(self, option, value):
		self.parser.set("DEFAULT", option, value) 
		
	#
	#  Writes prefs to the specified file, defaulting to PREFSFILE.
	#
	def save(self, prefsFile=PREFSFILE):
		
		x, y = self.pymp.window.get_position()
		
		if x > 0 or y > 0:  #gtk gives 0,0 quite often
			self.set("x", str(x))
			self.set("y", str(y))
		
		rect = self.pymp.window.get_allocation()
		self.set("width", str(rect.width))
		self.set("height", str(rect.height))
		
		self.set("continuous", str(self.pymp.playlist.continuous))
		self.set("random", str(self.pymp.playlist.random))
		self.set("repeat", str(self.pymp.playlist.repeat))
		self.set("path", self.pymp.menu.path)
		
		try:
			self.parser.write(open(prefsFile, "w"))
		except StandardError:
			return
			
#End of file
