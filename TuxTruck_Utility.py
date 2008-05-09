# TuxTruck Utilities
# Time-stamp: "2008-05-08 21:05:55 jantman"
# $Id: TuxTruck_Utility.py,v 1.1 2008-05-09 01:22:41 jantman Exp $
#
# Copyright 2008 Jason Antman. Licensed under GNU GPLv3 or latest version (at author's discretion).
# Jason Antman - jason@jasonantman.com - http://www.jasonantman.com
# Project web site at http://www.jasonantman.com/tuxtruck/

"""
This module holds all of the utility functions for TuxTruck.
"""

def str2tuple(s, fieldName):
    """
    Convert tuple-like strings to real tuples.
    eg '(1,2,3,4)' -> (1, 2, 3, 4)

    s is the string to parse
    fieldName is the field name for error messages

    This is used to parse the XML skin data.
    Got it from Steven D'Aprano, posted to python-list@python.org 2005-07-19
    TODO: this needs better error checking
    """
    if s[0] + s[-1] != "()":
        raise ValueError("Badly formatted string (missing brackets) in skin field "+fieldName+". It should be formatted like (a,b,c)")
    items = s[1:-1]  # removes the leading and trailing brackets
    items = items.split(',')
    L = [int(x.strip()) for x in items] # clean up spaces, convert to ints
    return tuple(L) 
