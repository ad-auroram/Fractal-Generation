from pathlib import Path
def parseFractal(filename):
    fractal = dict()
    file = open(filename)
    for line in file:
        line = line.lower()
        key = line.rstrip("\n").split(":")
        fractal[key[0]] = key[1]

    if fractal["centerx"].isnumeric():
        fractal["centerx"] = float(fractal["centerx"])
    else:
        raise ValueError("Center X should be a float!")

    if fractal["centery"].isnumeric():
        fractal["centery"] = float(fractal["centery"])
    else:
        raise ValueError("Center Y should be a float!")

    if fractal["axislength"].isnumeric():
        fractal["axislength"] = float(fractal["axislength"])
    else:
        raise ValueError("Axis length should be a float!")

    if fractal["pixels"].isnumeric():
        fractal["pixels"] = int(fractal["pixels"])
    else:
        raise ValueError("Pixels should be an integer!")

    if fractal["iterations"].isnumeric():
        fractal["iterations"] = int(fractal["iterations"])
    else:
        raise ValueError("Iterations should be and integer!")

    axislen = fractal["axislength"]/2
    fractal["min"] = {
        "x" : fractal["centerx"] - axislen,
        "y" : fractal["centerY"] - axislen
        }
    fractal["max"] = {
        "x" : fractal["centerx"] + axislen,
        "y" : fractal["centerx"] + axislen
    }
    fractal["pixelsize"] = fractal["axislength"]/fractal["pixels"]
    name = Path(filename)
    fractal["imagename"] = name.stem
    