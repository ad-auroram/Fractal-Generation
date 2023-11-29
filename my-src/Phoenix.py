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
from FractalInformation import fractalList


SPC = chr(32)
sideLength = 512

def getColorFromPalette(z):
    """
    Return the index of the color of the current pixel
    within the Phoenix fractal in the palette array
    """

    global grad
    global win

    JuliaCon = complex(0.5667, 0.0)

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

def makePictureOfFractal(fractalList, w, p, W, sideLength):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 640x640 pixels."""

    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane

    # Compute the minimum coordinate of the picture



    tk_Interface_PhotoImage_canvas_pixel_object = Canvas(win, width=sideLength, height=sideLength, bg=W)

    tk_Interface_PhotoImage_canvas_pixel_object.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?

    # Create the TK PhotoImage object that backs the Canvas Object
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((sideLength/2, sideLength/2), image=p, state="normal")




    # count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to
    # but I have to here because we're actually going BACKWARDS, which took me
    # a long time to figure out, so don't change it, or else the picture won't
    # come out right
    row = sideLength
    while row in range(sideLength, 0, -1):
        # for c (c == column) in the range of pixels in a square of size s
        cs = []
        for c in range(sideLength):
            # calculate the X value in the complex plane
            X = min[0] + c * size
            # calculate the X value in the complex plane
            Y = min[1] + row * size
            # TODO: do I really need to call getColorFromPalette() twice?
            #       It seems like this should be slow...
            #       But, if it aint broken, don't repair it, right?
            cp = getColorFromPalette(complex(X, Y))
            cs.append(cp)
        pixls = '{' + ' '.join(cs) + '}'
        p.put(pixls, (0, sideLength - row))
        w.update()  # display a row of pixels
        fraction_of_pixels_writtenSoFar = (sideLength - row) / sideLength   # update the number of pixels output so far
        # print a statusbar on the console
        print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"
                + f'{SPC}'
                + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",
                end="\r"
                , file=sys.stderr)
        row -= 1

def phoenix_main(i):
    """The main entry-point for the Phoenix fractal generator"""

    # the size of the image we will create is 512x512 pixels
    # Look, I  know globals are bad, but I don't know how else to use those
    # variables in here if I don't do it this way.  I didn't take any fancy CS
    # classes, sue me
    global tkPhotoImage
    global win
    global sideLength

    # Note the time of when we started so we can measure performance improvements
    b4 = time()
    # Set up the GUI so that we can display the fractal image on the screen
    win = Tk()

    print("Rendering %s fractal" % i, file=sys.stderr)
    # construct a new TK PhotoImage object that is 512 pixels square...
    tkPhotoImage = PhotoImage(width=sideLength, height=sideLength)
    # ... and use it to make a picture of a fractal
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?
    makePictureOfFractal(fractalList[i], win, tkPhotoImage, '#000000', sideLength)

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

