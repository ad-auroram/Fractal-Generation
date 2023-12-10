from pathlib import Path

def keyCheck(dict, key):
    if key in dict:
        return True
    else:
        return False
def parseFractal(filename):
    fractal = dict()
    file = open(filename)
    for line in file:
        if line.startswith("#"):
            continue
        if line == "\n":
            continue
        line = line.lower().strip()
        key = line.split(":")
        try:
            key[1] = key[1].replace(" ", "")
        except IndexError:
            raise RuntimeError(f"The value of the {key[0]} parameter is missing")
        fractal[key[0]] = key[1]

    requiredKeys = ("type", "centerx", "centery", "iterations", "axislength", "pixels")
    for key in requiredKeys:
        if not keyCheck(fractal, key):
            raise RuntimeError(f"The required parameter {key} is missing")

    try:
        fractal["centerx"] = float(fractal["centerx"])
    except ValueError:
        raise ValueError("centerX should be a float!")

    try:
        fractal["centery"] = float(fractal["centery"])
    except ValueError:
        raise ValueError("centerY should be a float!")

    try:
        fractal["axislength"] = float(fractal["axislength"])
    except ValueError:
        raise ValueError("axisLength should be a float!")

    try:
        fractal["pixels"] = int(fractal["pixels"])
    except ValueError:
        raise ValueError("pixels should be an integer!")
    if fractal["pixels"]<=0:
        raise ValueError("pixels can't be negative or 0!")

    try:
        fractal["iterations"] = int(fractal["iterations"])
    except ValueError:
        raise ValueError("iterations should be an integer!")


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
    