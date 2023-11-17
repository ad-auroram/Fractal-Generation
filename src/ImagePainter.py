from tkinter import Tk, Canvas, PhotoImage, mainloop

def paint(fractals, imagename, window):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 640x640 pixels in size."""

    global palette
    global img

    fractal = fractals[imagename]

    side = 512

    window = Tk()
    img = PhotoImage(width=side, height=side)
    paint(fractalList, image, window)

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

    # Display the image on the screen
    canvas = Canvas(window, width=side, height=side, bg='#000000')
    canvas.pack()
    canvas.create_image((side/2, side/2), image=img, state="normal")

    pixelsize = abs(maxx - minx) / side

    for row in range(side, 0, -1):
        cc = []
        for col in range(side):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            # "Leaf" is the only well-behaved fractal - all of the others crash
            #
            if imagename in [ 'leaf', ]:
                idx = PixelColorOrIndex(complex(x, y), None)
                color = palette[idx]
            # The rest of the fractals
            else:
                color = PixelColorOrIndex(complex(x, y), palette)
            cc.append(color)

        img.put('{' + ' '.join(cc) + '}', to=(0, 512-row))
        window.update()  # display a row of pixels

        print(pixelsWrittenSoFar(row), end='\r', file=sys.stderr)
        mainloop()


def pixelsWrittenSoFar(rows, cols):
    portion = (512 - rows) / 512

    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))