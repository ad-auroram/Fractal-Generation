
import unittest
from FractalParser import parseFractal
from PaletteFactory import makePalette
from FractalFactory import makeFractal

class Tests(unittest.TestCase):

    def testPalette(self):
        palette = makePalette("sunset", 100)
        palette2 = makePalette("thunderstorm", 512)
        self.assertEqual(len(palette.colors)-1, 108)
        self.assertEqual(len(palette2.colors)-1, 512)

    def testFractalInfo(self):
        mandelbrot = {
            "type" : "mandelbrot",
            "pixels" : 640,
            "centerx": 0.0,
            "centery" : 0.0,
            "axislength" : 4.0,
            "iterations" : 100,
            "pixelsize" : 4.0/640,
            "min" : {
                "x" : 0.0-2.0,
                "y" : 0.0-2.0
            },
            "max": {
                "x": 0.0 + 2.0,
                "y": 0.0 + 2.0
            },
            "imagename" : "mandelbrot"
        }

        self.assertEqual(parseFractal("test-file/mandelbrot.frac"), mandelbrot)

    def testDefault(self):
        fractal1 = makeFractal("")
        fractal2 = makeFractal(parseFractal("test-file/enhance.frac"))
        self.assertEqual(fractal1.type,fractal2.type)
        self.assertEqual(fractal1.pixels, fractal2.pixels)
        self.assertEqual(fractal1.iterations, fractal2.iterations)
