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

CUSTARD = '#E1D89F'
PISTACHIO = '#A8D786'
MINT = '#6ECB8A'
ELDERBERRY = '#4771B2'
CONCORD_GRAPE = '#51419C'
PLUM = '#7D387D'

MANDELBROT = [CUSTARD,   '#E0DA9E', '#E0DC9C', '#DFDE9B', '#DEDF9A', '#DBDE98',
           '#D8DE97', '#D4DD96', '#D1DD94', '#CDDC93', '#CADC92', '#C6DB91',
           '#C3DB8F', '#BFDA8E', '#BCD98D', '#B8D98B', '#B4D88A', '#B0D889',
           '#ACD788', PISTACHIO, '#A4D685', '#A0D684', '#9CD582', '#98D481',
           '#94D480', '#8FD37F', '#8BD37D', '#87D27C', '#82D17B', '#7ED17A',
           '#79D078', '#77D07A', '#76CF7C', '#75CF7E', '#73CE80', '#72CD83',
           '#71CD85', '#70CC87', MINT,      '#6DCB8C', '#6CCA8F', '#6BCA91',
           '#69C994', '#68C896', '#67C899', '#66C79C', '#65C79F', '#63C6A2',
           '#62C5A4', '#61C5A7', '#60C4AA', '#5FC3AD', '#5DC3B0', '#5CC2B3',
           '#5BC1B7', '#5AC1BA', '#59C0BD', '#57BFBF', '#56BABF', '#55B5BE',
           '#54B1BD', '#53ACBD', '#51A7BC', '#50A3BB', '#4F9EBB', '#4E99BA',
           '#4D94B9', '#4C8FB9', '#4A8AB8', '#4985B7', '#4880B7', '#487BB5',
           '#4876B4', ELDERBERRY,'#476CB1','#4668AF','#4663AE', '#465EAC',
           '#455AAB', '#4556A9', '#4551A8', '#444DA6', '#4449A5', '#4345A3',
           '#4543A2', '#4843A1', '#4B429F', '#4E429E', CONCORD_GRAPE,
           '#54419B', '#574199', '#594098', '#5C4096', '#5E3F95', '#613F94',
           '#633F92', '#653E91', '#673E8F', '#6A3D8E', '#6C3D8C', '#6D3C8B',
           '#6F3C8A', '#713C88', '#733B87', '#753B85', '#763A84', '#783A83',
           '#793981', '#7A3980', '#7C387E', PLUM]

PHOENIX = ['#ffe4b5', '#ffe5b2', '#ffe7af', '#ffe8ac', '#ffeaa8', '#ffeca5',
           '#ffeea2', '#fff09f', '#fff39c', '#fff699', '#fff996', '#fffc92',
           '#ffff8f', '#fbff8c', '#f8ff89', '#f4ff86', '#f0ff83', '#ebff80',
           '#e7ff7d', '#e2ff79', '#deff76', '#d8ff73', '#d3ff70', '#ceff6d',
           '#c8ff6a', '#c2ff67', '#bcff63', '#b6ff60', '#b0ff5d', '#a9ff5a',
           '#a3ff57', '#9cff54', '#94ff51', '#8dff4d', '#86ff4a', '#7eff47',
           '#76ff44', '#6eff41', '#66ff3e', '#5dff3b', '#54ff37', '#4cff34',
           '#43ff31', '#39ff2e', '#30ff2b', '#28ff29', '#25ff2d', '#21ff31',
           '#1eff34', '#1bff39', '#18ff3d', '#15ff41', '#12ff46', '#0fff4b',
           '#0cff50', '#08ff55', '#05ff5b', '#02ff60', '#00fe66', '#00fb6d',
           '#00f873', '#00f579', '#00f17f', '#00ee84', '#00eb8a', '#00e88f',
           '#00e594', '#00e299', '#00df9e', '#00dba2', '#00d8a6', '#00d5aa',
           '#00d2ae', '#00cfb2', '#00ccb6', '#00c9b9', '#00c5bc', '#00c2bf',
           '#00bdbf', '#00b4bc', '#00abb9', '#00a3b6', '#009bb3', '#0092af',
           '#008bac', '#0083a9', '#007ba6', '#0074a3', '#006da0', '#00669d',
           '#005f9a', '#005996', '#005293', '#004c90', '#00468d', '#00418a',
           '#003b87', '#003684', '#003080', '#002b7d', '#00277a', '#002277']


class Palette:
    def __init__(self, iteration):
        self.iteration = 0
    def getcolor(self, n):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")

class Sunset(Palette):


    def __init__(self, iteration):
        Palette.__init__(self, iteration)
        numColorSteps = 12
        i = math.ceil(self.iteration / numColorSteps)

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

        self.palette = sunset


    def getcolor(self, n):
        return self.palette[n]

class Thunderstorm(Palette):
    def __init__(self, iteration):
        Palette.__init__(self, iteration)
        numColorSteps = 8
        i = math.ceil(self.iteration / numColorSteps)

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

        self.palette = thunderstorm

    def getcolor(self, n):
        return self.palette[n]



