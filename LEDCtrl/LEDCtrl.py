__name__    = "LEDCtrl"
__author__  = "E. A. Tacao <e.a.tacao |at| estadao.com.br>"
__date__    = "29 Dez 2005, 17:00 GMT-03:00"
__version__ = "0.07"
__doc__     = """
LEDCtrl - a LED display control

This is a control that simulates a 7-segment LED display. It accepts decimal
and hexadecimal digits as well as any number of dots (.), traces (-),
colons (:) and a few other characters.


Usage

LEDCtrl(parent, id, pos, size, style, digits, value, geometry, ledstyle)

- parent, id, pos, size, style are used as in a wx.Window.

- digits (int) tells what would be the number of 7-segment digits on the
  control.

- value (str) is a string containing digits, letters [A-Z][a-z] and/or
  dots, traces or whitespaces.

- geometry (LEDGeometry) allows changing the control geometry. For more info
  please see the LEDGeometry class.

- ledstyle (int) define the led display styles, as described below.


Led styles

LED_ALIGN_LEFT
Align to the left.

LED_ALIGN_RIGHT
Align to the right.

LED_ALIGN_CENTRE (or LED_ALIGN_CENTER)
Center on display.

LED_DRAW_FADED
Draw faded segments.

LED_SLANT
Slant display by 10 degrees.

LED_ALLOW_COLONS
Allows the use of ":" characters.

LED_ZFILL
Fills display with zeros in the left, if the lenght of the value passed to
the display is lower than its number of digits. The lenght doesn't take into
account the dots and colons passed, if any. This style overrides any alignment 
styles passed.

LED_AGG
Draws anti-aliased displays. It uses Fredrik Lundh's aggdraw module
(if available) to draw segments. For more info and download please see
<http://effbot.org/zone/draw-agg.htm>.

The aggdraw module is accessed using a slightly modified version of
Jimmy Retzlaff's wxagg.py <http://www.averdevelopment.com/python/wxAGG.html>.
For more info and licensing notes please see the wxagg.py file.

Note that if the aggdraw module is not available, LEDCtrl will still work 
(obviously without anti-aliasing capabilities) and will silently ignore 
this flag.


Methods

SetValue(string), GetValue()
Set, get the value for the control.

SetForegroundColour(colour), GetForegroundColour()
Set, get the led colours. This also sets a fade colour automatically based on
the colour passed. If you want to use another colour for fading, call the
SetFadeColour method described below. A wx.Colour(0, 204, 204) is used by
default.

SetBackgroundColour(colour), GetBackgroundColour()
Set, get the colour for the led panel. Black is used by default. This also sets
a fade colour automatically based on the colour passed. If you want to use
another colour for fading, call the SetFadeColour method described below.

SetFadeColour(colour), GetFadeColour()
Set, get the colour for faded segments.

SetFadeFactor(factor), GetFadeFactor()
Set, get the fade factor, which may be an integer or float between 0 and 100. 
This factor is used to calculate the fade colour, and defaults to 33. Lower
values will render fade colours closer to the background; higher values produce 
fades closer to the foreground colour.

SetLedStyle(ledstyle), GetLedStyle()
Set, get the style for the display (see led styles above).

SetDigits(digits), GetDigits()
Defines, retrieves the number of digits on the led display.

GetValidChars()
Returns a list of all accepted characters.

SetGeometry(LEDGeometry), GetGeometry()
Set, get the control geometry. For more info please see the LEDGeometry class.

Additionally, several methods of wx.Window are available as well.


About:

LEDCtrl is distributed under the wxWidgets license.
Jimmy Retzlaff's wxagg.py module is distributed under the MIT license. Please
see the file wxagg.py for more details.

For all kind of problems, requests, enhancements, bug reports, etc,
please drop me an e-mail.

For updates please visit <http://j.domaindlx.com/elements28/wxpython/>.
"""

# History:
#
# Version 0.07:
#   - Added Set/GetFadeFactor and also some enhancements on fade colour
#     calculation thanks to a patch from Alexander 'boesi' Bosecke.
#
# Version 0.06:
#   - Minor improvements on fade colour calculation.
#
# Version 0.05:
#   - Geometry info now have their own class.
#
# Version 0.04:
#   - Fixed alignment issues.
#
# Version 0.03:
#   - Code clean-up
#   - Implemented ":" handling and fixed some bugs after
#     Alexander 'boesi' Bosecke suggestions on the wxPython users mailing list.
#
# Version 0.02:
#   - Some code clean-up and fixes to get it working with wxPython 2.6.1.0.
#   - Added aggdraw stuff.
#
# Version 0.01:
#   - Initial release.

#-------------------------------------------------------------------------------

import wx

try:
    from wxagg import AggDC
    _use_agg = True
except:
    _use_agg = False

#-------------------------------------------------------------------------------

# ledstyles

LED_DRAW_FADED   = 1
LED_ALIGN_LEFT   = 2
LED_ALIGN_RIGHT  = 4
LED_ALIGN_CENTRE = LED_ALIGN_CENTER = 8
LED_SLANT        = 16
LED_ZFILL        = 32
LED_AGG          = 64
LED_ALLOW_COLONS = 128

# Recognized chars; "."s and ":" are also accepted as well,
# but handled elsewhere.

_opts = {"0" : "1111110",
         "1" : "0110000",
         "2" : "1101101",
         "3" : "1111001",
         "4" : "0110011",
         "5" : "1011011",
         "6" : "1011111",
         "7" : "1110010",
         "8" : "1111111",
         "9" : "1111011",
         "A" : "1110111",
         "B" : "0011111",
         "C" : "1001110",
         "D" : "0111101",
         "E" : "1001111",
         "F" : "1000111",
         "-" : "0000001",
         " " : "0000000",
         "R" : "0000101",
         "O" : "0011101",
         "H" : "0110111",
         "L" : "0001110",
         "P" : "1100111"}

#-------------------------------------------------------------------------------

class LEDGeometry:
    def __init__(self, t = 3., sp = 3., wh = 40., hv = 25., r = 3.5, dd = 10.,
                 hg = 10., vg = 12.):
        """LEDGeometry holds the relative values needed to build segments and
           digits. For best results use float types for all arguments.

           Arguments:
             t  - Segment thickness; higher values produce 'fatter' segments.
             sp - Space between segments.
             wh - Width of horizontal segments; higher values produce wider
                  segments.
             hv - Height of vertical segment; higher values produce taller
                  segments.
             r  - Dot radius (used in dots and colons)
             dd - Horizontal spacing between digit and dot.
             hg - Horizontal spacing between digits.
             vg - Vertical spacing between the top of the client window/
                  top of digit and bottom of the client window/bottom of digit.
        """

        self.t = t; self.sp = sp; self.wh = wh; self.hv = hv
        self.r = r; self.dd = dd; self.hg = hg; self.vg = vg


    def Get(self):
        return self.t, self.sp, self.wh, self.hv, \
               self.r, self.dd, self.hg, self.vg

#-------------------------------------------------------------------------------

class _Segment:
    def __init__(self, name, state, geometry):

        t, sp, wh, hv, r, dd, hg, vg = geometry.Get()

        # Now we calc coords and positions based on geometry...

        mt = t / 2; mwh = wh - mt; mhv = hv - mt

        coords = {"h" : ((mt, 0), (mwh, 0), (wh, mt),
                         (mwh, t), (mt, t), (0, mt)),
                  "v" : ((mt, 0), (t, mt), (t, mhv),
                         (mt, hv), (0, mhv), (0, mt))}

        segpos = {"a" : ((mt + sp, 0), "h"),
                  "b" : ((sp * 2 + wh, mt + sp), "v"),
                  "c" : ((sp * 2 + wh, mt + 3 * sp + hv), "v"),
                  "d" : ((mt + sp, 4 * sp + 2 * hv), "h"),
                  "e" : ((0, mt + 3 * sp + hv), "v"),
                  "f" : ((0, mt + sp), "v"),
                  "g" : ((mt + sp, 2 * sp + hv), "h")}

        self.state = state

        i = segpos[name]
        self.position = i[0]
        self.coords = coords[i[1]]
        
        self.name = name


    def GetDrawingParams(self, x, y, k):
        px = x + self.position[0] / k; py = y + self.position[1] / k

        coords = []
        for xc, yc in self.coords:
            coords.append([px + xc / k, py + yc / k])

        return coords


    def Draw(self, dc, x, y, k, slant, draw_faded = False):
        coords = self.GetDrawingParams(x, y, k)

        if slant:
            # Slant by 10 degrees
            h = dc.GetSize().GetHeight()
            for i in coords:
                i[0] -= (i[1] - h) * 0.1745329

        if self.state and not draw_faded:
            dc.DrawPolygon(coords)
        elif draw_faded and not self.state:
            dc.DrawPolygon(coords)

#-------------------------------------------------------------------------------

class _Dot:
    def __init__(self, state, geometry):
        t, sp, wh, hv, r, dd, hg, vg = geometry.Get()

        x = sp * 2 + wh + t + dd
        y = 4 * sp + 2 * hv + t - r * 2

        self.position = (x, y)  # circle's bounding rect's top-left corner
        self.radius = r
        self.state = state


    def GetDrawingParams(self, x, y, k):
        radius = self.radius / k
        x, y = self.position[0] / k + x + radius, \
               self.position[1] / k + y + radius

        return x, y, radius


    def Draw(self, dc, x, y, k, slant, draw_faded = False):
        x, y, radius = self.GetDrawingParams(x, y, k)

        if slant:
            # Slant by 10 degrees
            h = dc.GetSize().GetHeight()
            x -= (y - h) * 0.1745329

        if self.state and not draw_faded:
            dc.DrawCircle(x, y, radius)
        elif draw_faded and not self.state:
            dc.DrawCircle(x, y, radius)

#-------------------------------------------------------------------------------

class _Colon:
    def __init__(self, state, geometry):
        t, sp, wh, hv, r, dd, hg, vg = geometry.Get()

        x = sp * 2 + wh + t + dd
        y1 = 2 * sp + hv - r * 2 - t
        y2 = 2 * sp + hv + t * 2

        self.position1 = (x, y1)
        self.position2 = (x, y2)
        self.radius = r
        self.state = state


    def GetDrawingParams(self, x, y, k):
        radius = self.radius / k
        x, y1, y2 = self.position1[0] / k + x + radius, \
                    self.position1[1] / k + y + radius, \
                    self.position2[1] / k + y + radius

        return x, x, y1, y2, radius


    def Draw(self, dc, x, y, k, slant, draw_faded = False):
        x1, x2, y1, y2, radius = self.GetDrawingParams(x, y, k)

        if slant:
            # Slant by 10 degrees
            h = dc.GetSize().GetHeight()
            x1 -= (y1 - h) * 0.1745329
            x2 -= (y2 - h) * 0.1745329

        if self.state and not draw_faded:
            dc.DrawCircle(x1, y1, radius)
            dc.DrawCircle(x2, y2, radius)
        elif draw_faded and not self.state:
            dc.DrawCircle(x1, y1, radius)
            dc.DrawCircle(x2, y2, radius)

#-------------------------------------------------------------------------------

class _Digit:
    def __init__(self, style, geometry):

        self.style = style
        self.geometry = geometry
        self.SetValue("  ")
        self.SetPosition(0, 0)


    def SetValue(self, value):
        dig = value[0]; pos = value[1]

        state = _opts[dig]; segs = "abcdefg"; self.elements = {}

        for i in range(0, 7):
            self.elements[segs[i]] = _Segment(segs[i], bool(int(state[i])),
                                              self.geometry)

        self.elements["dot"] = _Dot(pos == ".", self.geometry)

        if self.style & LED_ALLOW_COLONS:
            self.elements["colon"] = _Colon(pos == ":", self.geometry)


    def SetPosition(self, x, y):
        self.x = x; self.y = y


    def Draw(self, dc, k, draw_faded = False):
        for element in self.elements.values():
            element.Draw(dc, self.x, self.y, k,
                         self.style & LED_SLANT,
                         draw_faded)

#-------------------------------------------------------------------------------

class LEDCtrl(wx.Window):
    def __init__(self, parent, id = -1, pos = wx.DefaultPosition,
                 size = wx.DefaultSize, style = 0, name = "LEDCtrl",
                 digits = 12, value = "0", geometry = None,
                 ledstyle = LED_DRAW_FADED|LED_ALIGN_RIGHT|LED_AGG):

        """LEDCtrl - Constructor"""

        wx.Window.__init__(self, parent, id, pos, size, style, name)

        # Some references
        self.parent  = parent

        # Default geometry
        if geometry is None:
            self.geometry = LEDGeometry()
        else:
            self.geometry = geometry

        # Styles
        self.style = self._checkStyle(ledstyle)

        # Digits
        self.nod = digits
        self._initDigits()

        # Colour defaults
        self.bgColour = wx.BLACK.Get()
        self.fgColour = (0, 204, 204)
        self.fdFactor = 33
        self.SetBackgroundColour(self.bgColour)
        self.SetForegroundColour(self.fgColour)

        self.SetValue(value)

        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        wx.CallAfter(self.OnSize)


    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        if _use_agg and self.style & LED_AGG:
            dc = AggDC(dc)

        self._doUpdate(dc)


    def OnSize(self, evt = None):
        try:
            self._recalcDigSize(*self.GetClientSize().Get())
            self._initDisplay()
        except ZeroDivisionError:
            pass

        if evt:
            evt.Skip()


    def _checkStyle(self, ledstyle):
        # No alignment? We'll use LED_ALIGN_RIGHT by default.

        for align in [LED_ALIGN_RIGHT, LED_ALIGN_CENTRE, LED_ALIGN_CENTER, \
                      LED_ALIGN_LEFT]:
            if ledstyle & align:
                break
        else:
            ledstyle |= LED_ALIGN_RIGHT

        # Should we use aggdraw?
        if ledstyle & LED_AGG and not _use_agg:
            ledstyle -= LED_AGG
            
        return ledstyle


    def _selColours(self, colour, dc):
        dc.SetPen(wx.Pen(colour, 1, wx.SOLID))
        dc.SetBrush(wx.Brush(colour, wx.SOLID))


    def _initDigits(self):
        self.digits = []
        for i in range(0, self.nod):
            _d = _Digit(self.style, self.geometry)
            self.digits.append(_d)


    def _recalcDigSize(self, w, h):
        t, sp, wh, hv, r, dd, hg, vg = self.geometry.Get()

        kw = float(sp * 2 + wh + dd + r * 2 + t + hg) / w
        kh = float(4 * sp + 2 * hv + t + vg) / h
        self.k = max(kw, kh)

        xsp = hg / self.k

        _d = _Digit(self.style, self.geometry)

        ac = []
        for name, element in _d.elements.items():
            params = element.GetDrawingParams(0, 0, self.k)
            if name == "dot":
                x = params[0] + params[2]; y = params[1] + params[2]
                ac.append([x, y])
            elif name == "colon":
                x = params[0] + params[4]; y = params[3] + params[4]
                ac.append([x, y])
            else:
                ac += params
        dh = max([y for x, y in ac])
        dw = max([x for x, y in ac]) + xsp

        tw = dw * self.nod + xsp
        if tw > w:
            if self.style & LED_SLANT:
                tw += dh * 0.1745329
            k = tw / w
            self.k *= k; dw /= k; dh /= k; xsp /= k

        self.dw = dw; self.dh = dh; self.xsp = xsp


    def _initDisplay(self):
        w, h = self.GetClientSize()

        vdig, vdot = self.value[1:]

        offx = (w - (self.nod * self.dw) + self.xsp) / 2
        offy = (h - self.dh) / 2

        for i in range(0, self.nod):
            x = i * self.dw + offx; y = offy

            if self.style & LED_SLANT:
                x = x - offy * 0.1745329

            self.digits[i].SetPosition(x, y)


    def _doUpdate(self, dc):
        if not hasattr(self, "k"):
            self._recalcDigSize(*dc.GetSize().Get())

        dc.BeginDrawing()

        self._selColours(self.fgColour, dc)
        [digit.Draw(dc, self.k) for digit in self.digits]

        if self.style & LED_DRAW_FADED:
           self._selColours(self.fdColour, dc)
        else:
           self._selColours(self.bgColour, dc)
        [digit.Draw(dc, self.k, True) for digit in self.digits]

        dc.EndDrawing()


    def _adjustFadeColour(self):
        conv = lambda fg, bg: bg + (fg - bg) * (self.fdFactor / 100.)
        self.fdColour = tuple(map(conv, self.fgColour, self.bgColour))


    # Public methods -----------------------------------------------------------

    def SetForegroundColour(self, colour):
        """Set the led colours. This also sets a fading colour automatically
           based on the colour passed. If you want to use another colour for
           fading, call the SetFadeColour method after this method."""

        if type(colour) <> tuple:
            colour = colour.Get()
        self.fgColour = colour
        wx.Window.SetForegroundColour(self, colour)
        self._adjustFadeColour()


    def SetBackgroundColour(self, colour):
        """Set the background colour. This also sets a fading colour 
           automatically based on the colour passed. If you want to use another 
           colour for fading, call the SetFadeColour method after this 
           method."""

        if type(colour) <> tuple:
            colour = colour.Get()
        self.bgColour = colour
        wx.Window.SetBackgroundColour(self, colour)
        self._adjustFadeColour()


    def SetFadeColour(self, colour):
        """Set the fading colour."""

        if type(colour) <> tuple:
            colour = colour.Get()
        self.fdColour = colour
        self.Refresh()


    def GetFadeColour(self):
        """Get the fading colour."""
        return wx.Colour(*self.fdColour)


    def SetFadeFactor(self, factor):
        """Set the fading factor."""

        self.fdFactor = factor
        self._adjustFadeColour()
        self.Refresh()


    def GetFadeFactor(self):
        """Get the fading factor."""
        return self.fdFactor


    def SetDigits(self, digits):
        """Defines the number of digits on the led display."""

        self.nod = digits
        self._initDigits()
        self.SetValue(self.GetValue(), True)
        self._recalcDigSize(*self.GetClientSize().Get())
        self._initDisplay()


    def GetDigits(self):
        """Gets the number of digits on the led display."""
        return self.nod


    def SetLedStyle(self, ledstyle):
        """Sets the display style:
             LED_ALIGN_LEFT           Align to the left.
             LED_ALIGN_RIGHT          Align to the right.
             LED_ALIGN_CENTRE (or LED_ALIGN_CENTER) Center on display.
             LED_DRAW_FADED           Draw faded segments.
             LED_SLANT                Skews display by 10 degrees.
             LED_ZFILL                Fills display with zeros in the left.
             LED_AGG                  Draws anti-aliased displays.
             LED_ALLOW_COLONS         Allows the use of ":".
        """

        self.style = self._checkStyle(ledstyle)
        self._initDigits()
        self.SetValue(self.GetValue(), True)
        self._initDisplay()


    def GetLedStyle(self):
        """Get the display style:"""
        return self.style


    def SetValue(self, value, need_refresh = False):
        """Set the value for the control."""

        # We're case-insensitive.
        vo = value.upper()

        # Some consistency check
        vc = "".join(self.GetValidChars())
        for x in vo:
            if x not in vc:
                err = "Character '%s' is not supported. " \
                      "Only the following chars are allowed: '%s'" % (x, vc)
                raise ValueError, err

        # Finding dots, colons
        vdig = ""; vdot = ""; cursor = 0; i = 0
        while i < len(vo):
            if vo[i] == ".":
                if len(vdig) == cursor:
                    vdig += " "
                vdot += "."

            elif vo[i] == ":":
                if len(vdig) == cursor:
                    vdig += " "
                vdot += ":"

            else:
                if i < len(vo) - 1:
                    if vo[i+1] == ".":
                        vdig += vo[i]
                        vdot += "."
                        i += 1

                    elif vo[i+1] == ":":
                        vdig += vo[i]
                        vdot += ":"
                        i += 1

                    else:
                        vdig += vo[i]
                        vdot += " "
                        
                else:
                    vdig += vo[i]
                    vdot += " "

            cursor += 1
            i += 1

        # Alignment & zfill
        d = self.nod
        if self.style & LED_ZFILL:
            vdig = vdig.zfill(d)
            vdot = vdot.rjust(d)
        if self.style & LED_ALIGN_LEFT:
            vdig = vdig.ljust(d)
            vdot = vdot.ljust(d)
        elif self.style & LED_ALIGN_RIGHT:
            vdig = vdig.rjust(d)
            vdot = vdot.rjust(d)
        elif self.style & LED_ALIGN_CENTER:
            vdig = vdig.center(d)
            vdot = vdot.center(d)

        self.value = [value, vdig, vdot]
        
        for i in range(0, self.nod):
            self.digits[i].SetValue(vdig[i] + vdot[i])

        if need_refresh:
            self.Refresh()

        else:
            dc = wx.ClientDC(self)
            if _use_agg and self.style & LED_AGG:
                dc = AggDC(dc)

            self._doUpdate(dc)


    def GetValue(self):
        """Return the current value."""
        return self.value[0]


    def GetValidChars(self):
        """Returns a list of all accepted characters."""
        vc = _opts.keys() + [".", ":"]; vc.sort()
        return vc


    def SetGeometry(self, geometry):
        """Defines the display geometry. 'geometry' should be an instance
           of the LEDGeometry class."""

        self.geometry = geometry
        self._initDigits()
        self.SetValue(self.GetValue(), True)
        self._initDisplay()


    def GetGeometry(self, geometry):
        """Returns the instance of the LEDGeometry class used to build this
           display."""


#
##
### eof