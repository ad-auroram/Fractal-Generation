#return a fractal object given the name of a fractal
from Fractal import Mandelbrot, Phoenix
def makeFractal(fractalInfo):
    if fractalInfo == "":
        fractal = Mandelbrot(DEFAULT["centerX"], DEFAULT["centerY"], DEFAULT["iterations"])
        return fractal
    elif fractalInfo["type:"] == "mandelbrot":
        fractal = Mandelbrot(fractalInfo["centerx"], fractalInfo["centery"], fractalInfo["iterations"])
        return fractal
    elif fractalInfo["type:"] == "phoenix":
        fractal = Phoenix(fractalInfo["centerx"], fractalInfo["centery"], fractalInfo["iterations"])
        return fractal
    else:
        raise NotImplementedError(f"FractalFactoryFactory cannot make that fractal!")



DEFAULT = {
    "type" : "mandelbrot",
    "pixels" : 640,
    "centerx": -1.0,
    "centery" : 0.0,
    "axislength" : 1.0,
    "iterations" : 256
}
