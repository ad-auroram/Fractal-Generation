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
from image_painter import ImagePainter


if len(sys.argv) < 2:
    fractal = FractalFactory.makeFractal("")
    palette = PaletteFactory.makePalette("", fractal.iterations)
    painter = ImagePainter(fractal, palette)
    ImagePainter.paint(painter)
    exit(0)


frac = sys.argv[0]
info = FractalParser.parseFractal(frac)
fractal = FractalFactory.makeFractal(info)
if len(sys.argv) == 2:
    colors = sys.argv[1]
else:
    colors = ""
palette = PaletteFactory.makePalette(colors, info["iterations"])
painter = ImagePainter(fractal,palette)
ImagePainter.paint(painter)