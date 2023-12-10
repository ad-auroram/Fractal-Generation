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

import colour
import math


class Palette:
    def __init__(self, iteration):
        self.iteration = iteration

    def getcolor(self, n):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")


class Sunset(Palette):
    def __init__(self, iteration):
        super().__init__(iteration)
        numColorSteps = 12
        i = math.ceil(self.iteration/numColorSteps+1)

        purple = colour.Color("#1F214D")
        white = colour.Color("#FFFFFF")
        pink = colour.Color("#BF3475")
        orange = colour.Color("#EE6C45")
        yellow = colour.Color("#FFCE61")

        sunset = []
        for color in purple.range_to(white, i):
            sunset.append(color.hex_l)
        for color in list(white.range_to(pink, i))[1:]:
            sunset.append(color.hex_l)
        for color in list(pink.range_to(white, i))[1:]:
            sunset.append(color.hex_l)
        for color in list(white.range_to(orange, i))[1:]:
            sunset.append(color.hex_l)
        for color in list(orange.range_to(white, i))[1:]:
            sunset.append(color.hex_l)
        for color in list(white.range_to(yellow, i))[1:]:
            sunset.append(color.hex_l)
        for color in list(yellow.range_to(white, i))[1:]:
            sunset.append(color.hex_l)
        for color in list(white.range_to(orange, i))[1:]:
            sunset.append(color.hex_l)
        for color in list(orange.range_to(white, i))[1:]:
            sunset.append(color.hex_l)
        for color in list(white.range_to(pink, i))[1:]:
            sunset.append(color.hex_l)
        for color in list(pink.range_to(white, i))[1:]:
            sunset.append(color.hex_l)
        for color in list(white.range_to(purple, i))[1:]:
            sunset.append(color.hex_l)

        self.colors = sunset

    def getcolor(self, n):
        return self.colors[n]


class Thunderstorm(Palette):
    def __init__(self, iteration):
        super().__init__(iteration)
        numColorSteps = 8
        i = math.ceil(self.iteration / numColorSteps+1)

        darkBlue = colour.Color("#0D1B2A")
        white = colour.Color("#FFFFFF")
        aqua = colour.Color("#50D8D7")
        black = colour.Color("#000000")
        yellow = colour.Color("#EFA00B")
        blueGray = colour.Color("#415A77")

        thunderstorm = []
        for color in black.range_to(aqua, i):
            thunderstorm.append(color.hex_l)
        for color in list(aqua.range_to(white, i))[1:]:
            thunderstorm.append(color.hex_l)
        for color in list(white.range_to(blueGray, i))[1:]:
            thunderstorm.append(color.hex_l)
        for color in list(blueGray.range_to(black, i))[1:]:
            thunderstorm.append(color.hex_l)
        for color in list(black.range_to(yellow, i))[1:]:
            thunderstorm.append(color.hex_l)
        for color in list(yellow.range_to(white, i))[1:]:
            thunderstorm.append(color.hex_l)
        for color in list(white.range_to(darkBlue, i))[1:]:
            thunderstorm.append(color.hex_l)
        for color in list(darkBlue.range_to(black, i))[1:]:
            thunderstorm.append(color.hex_l)

        self.colors = thunderstorm

    def getcolor(self, n):
        return self.colors[n]



