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

from tkinter import Tk, Canvas, PhotoImage, mainloop
import time
import sys


class ImagePainter:
    def __init__(self, fractal, palette):
        self.fractal = fractal
        self.palette = palette
        self.IMAGE_SIZE = fractal.pixels
        self.STATUS_BAR_WIDTH = 34



    def statusbar(self, rows):
        portion = (self.IMAGE_SIZE - rows) / self.IMAGE_SIZE
        status_percent = '{:>4.0%}'.format(portion)
        status_bar = '=' * int(self.STATUS_BAR_WIDTH * portion)
        status_bar = '{:<33}'.format(status_bar)
        return ''.join(list(['[', status_percent, ' ', status_bar, ']']))


    def paint(self):
        """Paint a Fractal image into the TKinter PhotoImage canvas"""

        print(f"Rendering {self.fractal.name} fractal")
        # Note the time of when we started so we can measure performance improvements
        before = time.time()

        # Set up the GUI so that we can display the fractal image on the screen
        win = Tk()
        img = PhotoImage(width=self.IMAGE_SIZE, height=self.IMAGE_SIZE)
        canvas = Canvas(win, width=self.IMAGE_SIZE, height=self.IMAGE_SIZE, bg='#000000')
        canvas.create_image((self.IMAGE_SIZE/2.0,self.IMAGE_SIZE/2.0), image=img, state="normal")
        canvas.pack()

        minx = self.fractal.minX
        miny = self.fractal.minY

        # At this scale, how much length and height on the
        # imaginary plane does one pixel take?
        pixelsize = self.fractal.pixelSize

        max_iter = len(self.palette.colors)
        for row in range(self.IMAGE_SIZE, 0, -1):
            cc = []
            for col in range(self.IMAGE_SIZE):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                cc.append(self.palette.getcolor(self.fractal.count(complex(x, y), max_iter-1)))
            img.put('{' + ' '.join(cc) + '}', to=(0, self.IMAGE_SIZE-row))
            win.update()  # display a row of pixels
            print(self.statusbar(row), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column

        after = time.time()
        print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
        img.write(f"{self.fractal.name}.png")
        print(f"Wrote picture {self.fractal.name}.png", file=sys.stderr)

        print("Close the image window to exit the program", file=sys.stderr)

        # tkinter.mainloop keeps GUI open
        mainloop()
