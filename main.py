#! /usr/bin/env python
# TuxTruck Main Application (this is what you run!)
# Time-stamp: "2008-05-12 10:24:28 jantman"
# $Id: main.py,v 1.19 2008-05-12 14:23:48 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

import wx # import wx for the GUI

# TODO: do we need all of the self. here?
# TODO: need to update buttons to use a sizer
# TODO: rename MainApp to MainFrame
# TODO: use active images for buttons

from TuxTruck_Main import * # the main app frame

if __name__ == '__main__':
    """ 
    main method for the whole program. This gets called when we start this application,
    and it instantiates all of the necessary classes and starts the GUI and backend code.
    """
    app = wx.App()

    frame = TuxTruck_MainApp(parent=None, id=-1)

    frame.Show()
    app.MainLoop()
