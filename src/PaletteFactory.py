#return palette object given a palette name

from palette import Sunset, Thunderstorm

def makePalette(palette, steps):
    if palette == '' or palette.lower() == 'sunset':
        print("Creating Sunset palette")
        return Sunset(steps)
    elif palette.lower() == 'thunderstorm':
        print("Creating Thunderstorm Palette")
        return Thunderstorm(steps)
    else:
        raise NotImplementedError(f"PaletteFactory cannot make a {palette} palette")
