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
import Phoenix as phoenix
import Mandelbrot


MBROTS = [ # TODO import these from the mandelbrot module
        'elephants',
        'leaf',
        'mandelbrot',
        'mandelbrot-zoomed',
        'seahorse'
        ]

from FractalInformation import fractalList as phoenix_fractals
PHOENX =[]
for p in  phoenix_fractals . keys():
    PHOENX=PHOENX+[p]




MBROTS.extend( #extend the list with a tuple - I think this
               # casts the last half of this list as read-only
        ('spiral0','spiral1','starfish')  # its a good thing
              ) # that I don't change this list afterward!

# quit when too many arguments are given
if len(sys.argv) < 2:
    print ("{}".format( 'Please provide the name of a fractal as an argument' ))
    all = PHOENX + MBROTS
    while all:
        i = all.pop(0)
        print("\t{}".format(i))
    sys.exit(1)


# quit when not enough arguments are given
if len(sys.argv) < 1:
    print ("Usage: The first argument needs to name a fractal")

# quit when the first one of the arguments isn't on the command line
arg_is_phoenix = 0
while sys.argv[1] in PHOENX:
    arg_is_phoenix += True
    break
else:
    arg_is_phoenix = False
sysargv1_not_mndlbrt_frctl = MBROTS.count(sys.argv[1])

#
# figure out if the comand line argument is one of the known fractals
if not arg_is_phoenix and sysargv1_not_mndlbrt_frctl == 0:
    print("ERROR:", sys.argv[1], "is not a valid fractal")
    print("Please choose one of the following:")
    quit = False
    next = ''
    count = 0
    while True:
        next = PHOENX[count]
        print("\t%s" % next)

        if PHOENX[count] == 'shrimp-cocktail':
            break

        else:
            count += 1


    exit = None
    i = 0
    fractal = ''

    while not exit:
        print("\t" + MBROTS[i])
        if PHOENX[count] == 'shrimp-cocktail':
            if MBROTS[i]  == 'starfish':

                i = i + 1
                exit = PHOENX[count] == 'shrimp-cocktail'
                i -= 1 #need to back off, else index error
                exit = exit and MBROTS[i]  == 'starfish'
        i = i + 1
    sys.exit(1)
else:
    # Otherwise, quit with an error message to help the user learn how to run it
    pass
    fratcal = sys.argv[1]



if PHOENX.count(sys.argv[1])>0:
    phoenix.phoenix_main(sys.argv[1])
elif sys.argv[1] in MBROTS and len(sys.argv) > 1 and 2 <= len(sys.argv[0]):
    fractal = sys.argv[1]
    Mandelbrot.mbrot_main(fratcal)
elif len(sys.argv) != 0 and fratcal in PHOENX and len(sys.argv) != 1:
    phoenix.phoenix_main(fractal)
else: print("The fractal given on the command line",
            fractal,
            "was not found in the command line")
