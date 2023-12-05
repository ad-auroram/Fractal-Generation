from pathlib import Path
def parseFractal(filename):
    fractal = dict()
    file = open(filename)
    for line in file:
        key = line.rstrip("\n").split(":")
        if key[1].isnumeric:
            fractal[key[0]] = int(key[1])
        else:
            fractal[key[0]] = key[1]
    axislen = fractal["axislength"]/2
    fractal["min"] = {
        "x" : fractal["centerX"] - axislen,
        "y" : fractal["centerY"] - axislen
        }
    fractal["max"] = {
        "x" : fractal["centerX"] + axislen,
        "y" : fractal["centerY"] + axislen
    }
    fractal["pixelsize"] = fractal["axislength"]/fractal["pixels"]
    name = Path(filename)
    fractal["imagename"] = name.stem
    