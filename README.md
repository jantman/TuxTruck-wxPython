TuxTruck-wxPython
==================

[![Project Status: Abandoned - Initial development has started, but there has not yet been a stable, usable release; the project has been abandoned and the author(s) do not intend on continuing development.](http://www.repostatus.org/badges/0.1.0/abandoned.svg)](http://www.repostatus.org/#abandoned)

This is an old and largely abandoned project to create a CarPC environment in
wxPython. One developer has done some additional work on the audio player, but
not much other than that does anything. It was also the project I learned
Python with, so it's probably not the best example of coding
(understatement). I'm putting it up here in case anyone is interested, and
largely for the ideas contained in it, not the code (though some of it may be
useful). Lastly, these days it would probably make *much* more sense to build
TuxTruck on an Android-based platform, as it already has builtin support for a
lot of the stuff we want - as a matter of fact, aside from OBD, current
Android phones and tablets fulfill pretty much all of these requirements.

So, below is my original blog post describing this. I guess if you need a
media player in Python/wxWindows, there might be some good code to look
at. There's also a project wiki which has been taken offline, and now is just
in the "oldwiki/" directory in this repo.

I still own tuxtruck.org. If anyone is interested in continuing the project, please contact me.

Original Blog Post Description/Plan
------------------------------------

This comes from the [Original blog post on this project](http://blog.jasonantman.com/2008/05/sunspot-carpc-mediawiki-logging/)

My newest project – which I’m hoping to spend nearly the whole summer on – is
the TuxTruck. I’ve been frustrated with the lack of “smartness” in my truck
(an 06 Ford F-250), not to mention having to remember my MP3 player so I can
listen to podcasts on the way to work, and having so many gadgets in my
truck. So, the solution is obvious: a Linux-based CarPC. A nice little
Mini-ATX box under a seat, with a 7″ pull-out touchscreen in the dash
(replacing the factory radio). It’s a big, complicated, and expensive project
– but I want one, and I could use some experience with smaller systems.
The major features I have planned:

1. Realtime GPS navigation
2. Hands-free bluetooth calls from my cell, with address book, routing to contact address, possibly voice dialing.
3. Realtime weather
4. OBD-II interface, for vehicle diagnostics and fuel efficiency/performance profiling
5. Audio – at a minimum searching and playing MP3s, and automatically downloading podcasts and throwing them in a playlist. Perhaps also an AM/FM tuner

It’s not an easy project. So far, the major challenges seem to be:

- No full-featured GPS navigation package available. The ones that are available don’t seem to be too easy to integrate into my planned GUI, which will allot them 800×420 pixels (on an 800×480 screen) and requre the bottom toolbar to be always available.
- How to handle processing of multiple data streams that require near-real-time processing – specifically, GPS with text-to-speech, turn-by-turn directions, plus playing audio, plus responding to an incoming phone call in a timely manner, pausing the audio, and stopping GPS audio but continuing navigation.
- Whether to install a smaller stereo and use aux input for audio, or totally rip out the stereo, use an amp with the computer as its only input, and then how to control volume?

There will be more to come in the future. For now, take a look at the TuxTruck github.
