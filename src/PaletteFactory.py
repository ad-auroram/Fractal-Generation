#return palette object given a palette name

from palette import Sunset, Thunderstorm
def makePalette(fractal, steps):
    if fractal == '' or fractal.lower() == 'sunset':
        return Sunset(steps)
    elif fractal.lower() == 'thunderstorm':
        return Thunderstorm(steps)
    else:
        raise NotImplementedError(f"PaletteFactory cannot make a {fractal} palette")
    