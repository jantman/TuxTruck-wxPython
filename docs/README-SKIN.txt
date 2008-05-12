TuxTruck wxPython GUI
http://www.jasonantman.com
Time-stamp: "2008-05-12 10:06:47 jantman"
$Id: README-SKIN.txt,v 1.1 2008-05-12 14:05:55 jantman Exp $

TuxTruck - Skin Documentation

Skins in TuxTruck are defined in XML files. The skin "defaultSkin" comes
standard with TuxTruck, and must be present for the GUI to work. 

A Skin is composed of the following files:
*The skin XML file, which defines *everything*
*A directory of button images. The default is TuxTruck/defaultSkin-buttons/

Each skin defines positions of all elements, as well as color information. For
each possible object color, there are two values - day and night, for day and
night modes, respectively. 

The buttons directory should hold four (4) images for each button, one each
for active and inactive states for day and night skins.

The naming convention for skin values is as follows:
*The entire skin is an XML file, contained in a root element called
"TuxTruckSkin"
*There are child elements for each logical area, mode/screen, or logical
object, such as:
	*globalSkin (general information about this skin, including name and buttonPath
	*window (the main, top-level window ("frame" in wxWidgets
	nomenclature)
	*button_images (defines the filenames of all button images
	*digitalClock - the digital clock on the Home screen
	*analogClock - the analog clock on the Home screen
* Values are named like {day|night}_propertyName. Any property that changes
between day and night modes (or should change) should be prefaced by "day_" or
"night_". I.e. the height and width of the main window are in the "window"
child of root node "TuxTruckSkin", and called "height" and "width",
respectively. The background color, however, is defined in "day_bgColor" and
"night_bgColor" for day and night modes, respectively.

A note on day and night mode:
Day and night mode should, in principle, be automatically controlled by a
photoresistor or light sensor. With a light sensing device present, TuxTruck
should automatically switch from day to night mode when the light level drops
below a predefined value (after a certain amount of time), and vice-versa when
the light level come back above that value. Day mode should be contrasting
colors, designed to be easily viewable in bright light. Night mode should be
dark colors, with mostly red, in order to preserve the driver's night vision
and reduce distraction and glare.

