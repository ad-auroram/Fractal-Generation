#!/usr/bin/env python3

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.

import sys

import PaletteFactory
import FractalFactory
import FractalParser
from image_painter import paint


if len(sys.argv) < 2:
    #print ('Please provide the name of a fractal as an argument')
    #for f in FRACTALS:
     #   print(f"\t{f}")
    #sys.exit(1)
    fractal = FractalFactory.makeFractal("")
    palette = PaletteFactory.makePalette("", fractal.iterations())

#---------delete under here when done----------

if sys.argv[1] not in FRACTALS:
    print("ERROR:", sys.argv[1], "is not a valid fractal")
    print("Please choose one of the following:")
    for f in FRACTALS:
        print(f"\t{f}")
    sys.exit(1)

name = sys.argv[1]
fractal = FRACTALS[name]
if fractal['type'] == 'mandelbrot':
    palette = palette.MANDELBROT
    count = Mandelbrot.count
else:
    palette = palette.PHOENIX
    count = Phoenix.count

paint(fractal, name, count, palette)

#---------new main under here, delete above when done---------
frac = sys.argv[1]
info = FractalParser.parseFractal(frac)
fractal = FractalFactory.makeFractal(info)
if len(sys.argv) == 3:
    colors = sys.argv[2]
else:
    colors = ""
palette = PaletteFactory.makePalette(colors, info["iterations"])
