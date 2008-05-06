#!/usr/bin/env python

import sys, os, time, gobject

REMOTE_TIMEOUT, REMOTE_BUFFSIZE = .010, 8192
FIFO = os.path.expanduser("~/.pymp/fifo")

#
#  Performs any requested remote commands in args on startup.
#  Returns True if commands were processed, False otherwise.
#
def remote(args):
	
	if not os.access(FIFO, os.F_OK | os.R_OK | os.W_OK):
		os.mkfifo(FIFO)  #create fifo
		
	fifo = os.open(FIFO, os.O_RDWR | os.O_NONBLOCK)
	
	command, delim, ind, add, out = "", " ", 2, False, None
	
	if len(args) < 2:  #no command specified, query to see if we should start
		command = "status"
	elif args[1] != "-remote":  #add files, delimit paths with newlines
		command, delim, ind, add = "add\n", "\n", 1, True
	
	for a in args[ind:]:  #construct command
		command = command + a + delim
	
	os.write(fifo, command)  #write command to fifo
	
	time.sleep(REMOTE_TIMEOUT)  #allow for processing
	
	try:  #determine if command was processed
		out = os.read(fifo, REMOTE_BUFFSIZE)
	except StandardError:  #quietly ignore
		pass
		
	os.close(fifo)  #close fifo
	
	if add and out:  #adds not processed
		return False
	
	if out == command:  #command not processed
		return False
	
	if out:  #print output
		print out
	
	return True

#
#  Provides remote control mechanisms over fifo.
#
class Remote:
	
	pymp, fifo, handle = None, None, 0
	
	#
	#  Instantiates a new Remote listener.
	#
	def __init__(self, pymp):
		
		self.pymp = pymp
		
		if not os.access(FIFO, os.F_OK | os.R_OK | os.W_OK):
			os.mkfifo(FIFO)  #create fifo
		
		fifo = os.open(FIFO, os.O_RDWR | os.O_NONBLOCK)
		handle = gobject.io_add_watch(fifo, gobject.IO_IN, self.cmd)
		
		self.fifo, self.handle = fifo, handle
	
	#
	#  Adds each arg in args to the playlist.
	#
	def _cmd_add(self, args):
		for a in args:  #add all args
			self.pymp.playlist.add(a)
	
	#
	#  Attempts to play a target at index args[0].
	#
	def _cmd_play(self, args):
		try:  #attempt to play track at index
			self.pymp.playlist.play(args[0])
		except StandardError:
			pass
	
	#
	#  Pauses playback of the current target.
	#
	def _cmd_pause(self, args):
		self.pymp.mplayer.pause()
	
	#
	#  Stops playback of the current target.
	#
	def _cmd_stop(self, args):
		self.pymp.playlist.stop(None, None)
	
	#
	# Plays the next target.
	#
	def _cmd_next(self, args):
		self.pymp.playlist.next(None, None)
	
	#
	# Plays the previous target.
	#
	def _cmd_prev(self, args):
		self.pymp.playlist.prev(None, None)
	
	#
	# Write the current target's title to fifo.
	#
	def _cmd_status(self, args):
		status = self.pymp.playlist.status()
		
		gobject.source_remove(self.handle)
		
		os.write(self.fifo, status)
		time.sleep(REMOTE_TIMEOUT * 2)
		
		self.handle = gobject.io_add_watch(self.fifo, gobject.IO_IN, self.cmd)
	
	#
	#  Passes cmd through to mplayer.
	#
	def _cmd_generic(self, cmd):
		self.pymp.mplayer.cmd(cmd)
	
	#
	#  Process commands waiting on fd, dispatch appropriately.
	#
	def cmd(self, fd, cond):
		try:
			buff = os.read(fd, REMOTE_BUFFSIZE).strip()
			
			delim = " "  #normal commands delimited with whitespace
			if buff.startswith("add\n"):  #paths are delimited with newlines
				delim = "\n"
			
			command = buff.split(delim)
			
			cmd, args = command[0], command[1:]  #split args
			
			getattr(self, "_cmd_%s" % cmd)(args)
			
		except StandardError:
			self._cmd_generic(buff)
		
		return True
		
	#
	#  Cleanly closes this listener's fifo.
	#
	def close(self):
		os.close(self.fifo)
	
#End of file
