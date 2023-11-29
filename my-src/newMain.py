import sys
from ImagePainter import paint

from FractalInformation import fractalList as fractals


def printOptions():
    print("Please choose one of the following:")
    for key in fractals:
        print(key)

def main():
    fractal = sys.argv[1]

    if len(sys.argv) < 2:
        print("{}".format('Please provide the name of a fractal as an argument'))
        printOptions()
        sys.exit(1)

    elif len(sys.argv) < 1:
        print("Usage: The first argument needs to name a fractal")

    elif fractal not in fractals:
        print("ERROR:", fractal, "is not a valid fractal")
        printOptions()
        sys.exit(1)

    if fractal in fractals:
        paint(fractals, fractal)



