# Pymp Makefile

PYTHON=`which python`
PREFIX=/usr/local
DESTDIR=

all: control.py menu.py mplayer.py playlist.py prefs.py pymp.py
	$(PYTHON) ./build.py; rm -f ./build.pyc
	
install: all
	
	install -d $(DESTDIR)/$(PREFIX)/lib/pymp
	install *.pyc $(DESTDIR)/$(PREFIX)/lib/pymp
	
	install -d $(DESTDIR)/$(PREFIX)/share/pixmaps
	install -m 644 pymp.png $(DESTDIR)/$(PREFIX)/share/pixmaps
	
	install -d $(DESTDIR)/$(PREFIX)/bin
	install pymp $(DESTDIR)/$(PREFIX)/bin
	
	sed -i "s|PREFIX|$(PREFIX)|g" \
		$(DESTDIR)/$(PREFIX)/bin/pymp
	
clean:
	rm -f *.pyc
	
#End of file
