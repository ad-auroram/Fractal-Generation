from pathlib import Path
def parseFractal(filename):
    fractal = dict()
    file = open(filename)
    for line in file:
        if line.startswith("#"):
            continue
        line = line.lower().strip()
        key = line.split(":")
        key[1] = key[1].replace(" ", "")
        fractal[key[0]] = key[1]

    fractal["centerx"] = float(fractal["centerx"])
    fractal["centery"] = float(fractal["centery"])
    fractal["axislength"] = float(fractal["axislength"])
    fractal["pixels"] = int(fractal["pixels"])
    fractal["iterations"] = int(fractal["iterations"])


    axislen = fractal["axislength"]/2
    fractal["min"] = {
        "x" : fractal["centerx"] - axislen,
        "y" : fractal["centery"] - axislen
        }
    fractal["max"] = {
        "x" : fractal["centerx"] + axislen,
        "y" : fractal["centerx"] + axislen
    }
    fractal["pixelsize"] = fractal["axislength"]/fractal["pixels"]
    name = Path(filename)
    fractal["imagename"] = name.stem

    return fractal
    