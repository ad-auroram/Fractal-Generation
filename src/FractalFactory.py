#return a fractal object given the name of a fractal
from Fractal import Mandelbrot, Mandelbrot3, Phoenix, Spider

def keyCheck(dict, key):
    if key in dict:
        return True
    else:
        return False

def makeFractal(fractalInfo):
    if fractalInfo == "":
        fractal = Mandelbrot(DEFAULT)
        return fractal
    elif fractalInfo["type"] == "mandelbrot":
        fractal = Mandelbrot(fractalInfo)
        return fractal
    
    elif fractalInfo["type"] == "phoenix":
        requiredKeys = ("preal", "pimag", "creal", "cimag")
        for key in requiredKeys:
            if not keyCheck(fractalInfo, key):
                raise RuntimeError(f"The required parameter {key} is missing")
        
        try:
            fractalInfo["preal"] = float(fractalInfo["preal"])
        except ValueError:
            raise ValueError("pReal should be a float!")
        try:
            fractalInfo["creal"] = float(fractalInfo["creal"])
        except ValueError:
            raise ValueError("cReal should be a float!")
        try:
            fractalInfo["pimag"] = float(fractalInfo["pimag"])
        except ValueError:
            raise ValueError("pImag should be a float!")
        try:
            fractalInfo["cimag"] = float(fractalInfo["cimag"])
        except ValueError:
            raise ValueError("cImag should be a float!")
        fractal = Phoenix(fractalInfo)
        return fractal
    
    elif fractalInfo["type"] == "mandelbrot3":
        fractal = Mandelbrot3(fractalInfo)
        return fractal

    elif fractalInfo["type"] == "spider":
        fractal = Spider(fractalInfo)
        return fractal
    else:
        raise NotImplementedError(f"FractalFactory cannot make that fractal!")


#enhance fractal
DEFAULT = {
    "type" : "mandelbrot",
    "pixels" : 512,
    "centerx": -1.48,
    "centery" : 0.0,
    "axislength" : 0.01,
    "iterations" : 300,
    "pixelsize" : 0.01/512,
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
