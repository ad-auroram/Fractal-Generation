#return a fractal object given the name of a fractal
from Fractal import Mandelbrot, Mandelbrot3, Phoenix, Spider
def makeFractal(fractalInfo):
    if fractalInfo == "":
        fractal = Mandelbrot(DEFAULT)
        return fractal
    elif fractalInfo["type"] == "mandelbrot":
        fractal = Mandelbrot(fractalInfo)
        return fractal
    elif fractalInfo["type"] == "phoenix":
        fractal = Phoenix(fractalInfo)
        return fractal
    elif fractalInfo["type"] == "mandelbrot3":
        fractal = Mandelbrot3(fractalInfo)
        return fractal
    elif fractalInfo["type"] == "spider":
        fractal = Spider(fractalInfo)
        return fractal
    else:
        raise NotImplementedError(f"FractalFactoryFactory cannot make that fractal!")



DEFAULT = {
    "type" : "mandelbrot",
    "pixels" : 512,
    "centerx": -1.48,
    "centery" : 0.0,
    "axislength" : 0.01,
    "iterations" : 300,
    "pixelsize" : 0.008/512,
    "min" : {
        "x" : -1.48-(0.01/2),
        "y" : 0.0 - (0.01/2)
    },
    "max" : {
        "x" : -1.48 + (0.01/2),
        "y" : 0.0 + (0.01/2)
    },
    "imagename" : "default"
}
