#return a fractal object given the name of a fractal
from Fractal import Mandelbrot, Phoenix
def makeFractal(fractalInfo):
    if fractalInfo == "":
        fractal = Mandelbrot(DEFAULT)
        return fractal
    elif fractalInfo["type:"] == "mandelbrot":
        fractal = Mandelbrot(fractalInfo)
        return fractal
    elif fractalInfo["type:"] == "phoenix":
        fractal = Phoenix(fractalInfo)
        return fractal
    else:
        raise NotImplementedError(f"FractalFactoryFactory cannot make that fractal!")



DEFAULT = {
    "type" : "mandelbrot",
    "pixels" : 640,
    "centerx": -1.0,
    "centery" : 0.0,
    "axislength" : 1.0,
    "iterations" : 256,
    "pixelsize" : 1/640,
    "min" : {
        "x" : -1.0-(1.0/2),
        "y" : 0 - (1.0/2)
    },
    "max" : {
        "x" : -1.0 + (1.0/2),
        "y" : 0 + (1.0/2)
    },
    "imagename" : "mandelbrot-zoomed"
}
