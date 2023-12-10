
import unittest
from FractalParser import parseFractal
from PaletteFactory import makePalette
from Fractal import Mandelbrot

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

        self.assertEqual(parseFractal("mandelbrot.frac"), mandelbrot)

    def testCount(self):
        pass
