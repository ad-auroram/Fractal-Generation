from pathlib import Path
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
        key[1] = key[1].replace(" ", "")
        fractal[key[0]] = key[1]

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
    try:
        fractal["iterations"] = int(fractal["iterations"])
    except ValueError:
        raise ValueError("pixels should be an integer!")


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

    if fractal["type"] == "phoenix":
        try:
            fractal["preal"] = float(fractal["preal"])
        except ValueError:
            raise ValueError("pReal should be a float!")
        try:
            fractal["creal"] = float(fractal["creal"])
        except ValueError:
            raise ValueError("cReal should be a float!")
        try:
            fractal["pimag"] = float(fractal["pimag"])
        except ValueError:
            raise ValueError("pImag should be a float!")
        try:
            fractal["cimag"] = float(fractal["cimag"])
        except ValueError:
            raise ValueError("cImag should be a float!")

    return fractal
    