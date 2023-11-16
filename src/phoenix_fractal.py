#!/usr/bin/env python3
# Phoenix Fractal Visualizer - a variation of the Julia Fractal

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
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time


SPC = chr(0o40)  # Why doesn't anybody write octal numbers anymore...
s = 0o1000

def getColorFromPalette(z):
    """
    Return the index of the color of the current pixel
    within the Phoenix fractal in the palette array
    """

    global grad
    global win

    # JuliaCon is the Julia Constant; varying this value gives rise to a variety of variated images
    JuliaCon = complex(0.5667, 0.0)

    # phoenix is the Phonix Constant; same deal as above - adjust this to get different results
    phoenixCon = complex(-0.5, 0.0)

    # reflect its components, so the imaginary part becomes the real part, and vice versa
    zFlipped = complex(z.imag, z.real)

    # zPrevious is the PREVIOUS Z value, except the 1st time through the
    # function, when it starts out as Complex Zero
    zPrev = 0+0j
    # set Z back to zFlipped,
    z = zFlipped


    for i in range(102):

        zSave = z  # save the current Z value before we overwrite it
        # compute the new Z value from the current and previous Zs
        z = z * z + JuliaCon + (phoenixCon * zPrev)
        zPrev = zSave  # Set the prevZ value for the next iteration

        if abs(z) > 2:
            return grad[i]  # The sequence is unbounded
            z = z * z + JuliaCon  # + zPrev * phoenixCon
    # TODO: One of these returns occasionally makes the program crash sometimes
    return grad[101]         # Else this is a bounded sequence


def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):
    """Make sure that the fractal configuration data repository dictionary
    contains a key by the name of 'name'

    When the key 'name' is present in the fractal configuration data repository
    dictionary, return its value.

    Return False otherwise
    """
    for key in dictionary:
        if key in dictionary:
            if key == name:
                return key


Save_As_Picture = True
tkPhotoImage = None

def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 640x640 pixels."""

    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane

    # Compute the minimum coordinate of the picture
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),
           (f['centerY'] - (f['axisLength'] / 2.0)))


    # Compute the maximum coordinate of the picture
    # The program has only one axisLength because the images are square
    max = ((f['centerX'] + (f['axisLength'] / 2.0)),
           (f['centerY'] + (f['axisLength'] / 2.0)))


    tk_Interface_PhotoImage_canvas_pixel_object = Canvas(win, width=s, height=s, bg=W)

    tk_Interface_PhotoImage_canvas_pixel_object.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?

    # Create the TK PhotoImage object that backs the Canvas Object
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((s/2, s/2), image=p, state="normal")

    size = abs(max[0] - min[0]) / s

    # for r (where r means "row") in the range of the size of the square image,
    # but count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to
    # but I have to here because we're actually going BACKWARDS, which took me
    # a long time to figure out, so don't change it, or else the picture won't
    # come out right
    r = s
    while r in range(s, 0, -1):
        # for c (c == column) in the range of pixels in a square of size s
        cs = []
        for c in range(s):
            # calculate the X value in the complex plane
            X = min[0] + c * size
            Y = 0
            # calculate the X value in the complex plane
            Y = min[1] + r * size
            # TODO: do I really need to call getColorFromPalette() twice?
            #       It seems like this should be slow...
            #       But, if it aint broken, don't repair it, right?
            cp = getColorFromPalette(complex(X, Y))
            cs.append(cp)
        pixls = '{' + ' '.join(cs) + '}'
        p.put(pixls, (0, s - r))
        w.update()  # display a row of pixels
        fraction_of_pixels_writtenSoFar = (s - r) / s   # update the number of pixels output so far
        # print a statusbar on the console
        print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"
                + f'{SPC}'
                + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",
                end="\r"
                , file=sys.stderr)
        r -= 1


# This is the color palette, which defines the palette that images are drawn
# in as well as limiting the number of iterations the escape-time algorithm uses
#
# TODO: It would be nice to add more or different colors to this list, but it's
# just so much work to calculate all of the in-between shades!
grad = ['#ffe4b5', '#ffe5b2', '#ffe7af', '#ffe8ac', '#ffeaa8', '#ffeca5',
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

# Patrick T. 11/22/2022
# The program was crashing from IndexError because the color palette had too
# few colors.  Boy, was the customer mad about that!  I added some extra black
# pixels at the end to stop it crashing until somebody solves the actual
# problem.  PLEASE DELETE THIS CODE AFTER THE BUG GETS FIXED!!!
class Black:
    BLACK = '#FFFFFF'

grad += [Black.BLACK] * 6  # six pixels should be enough


# This dictionary contains the different views of the Phoenix set you can make
# with this program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'i'.
#
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into
# this configuration dictionary instead of hardcoding it into this program.
# But I don't have time for this right now, too busy.  I'll just keep doing it
# the way I know how.
f = {
        'phoenix': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  3.25,
            },

        'peacock': {
            'centerX':     -0.363287878200906,
            'centerY':     0.381197981824009,
            'axisLength':  0.0840187115019564,
        },

        'monkey-knife-fight': {
            'centerX':    -0.945542168674699,
            'centerY':    0.232234726688103,
            'axisLength': 0.136626506024096,
            },

        'shrimp-cocktail': {
            'centerX': 0.529156626506024,
            'centerY': -0.3516077170418,
            'axisLength': 0.221204819277108,
            },
        }



WHITE = '#ffffff'
RED = '#ff0000'
BLUE = '#00ff00'
GREEN = '#0000ff'
BLACK = '#000000'
ORANGE = '#ffa50'
TOMATO = '#ff6347'
HOT_PINK = '#ff69b4'
REBECCA_PURPLE = '#663399'
LIME_GREEN = '#89ff00'
GREY0 = '#000000'
GRAY37 = '#5e5e5e'
GREY74 = '#bdbdbd'
GRAY99 = '#fcfcfc'


def phoenix_main(i):
    """The main entry-point for the Phoenix fractal generator"""

    # the size of the image we will create is 512x512 pixels
    # Look, I  know globals are bad, but I don't know how else to use those
    # variables in here if I don't do it this way.  I didn't take any fancy CS
    # classes, sue me
    global tkPhotoImage
    global win
    global s

    # Note the time of when we started so we can measure performance improvements
    b4 = time()
    # Set up the GUI so that we can display the fractal image on the screen
    win = Tk()

    print("Rendering %s fractal" % i, file=sys.stderr)
    # construct a new TK PhotoImage object that is 512 pixels square...
    tkPhotoImage = PhotoImage(width=s, height=s)
    # ... and use it to make a picture of a fractal
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?
    makePictureOfFractal(f[i], i, ".png", win, grad, tkPhotoImage, GREY0, None, None, s)

    if Save_As_Picture:
        # Write out the Fractal into a .gif image file
        tkPhotoImage.write(i + ".png")
        print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)

    if Save_As_Picture:
        # Output the Fractal into a .png image
        tkPhotoImage.write(f"{i}.png")
        print("Saved image to file " + i + ".png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    # Call tkinter.mainloop so the GUI remains open
    mainloop()

