# Fractal Visualizer User Manual

This program can produce Mandelbrot and Phoenix fractals.


To run the program, run the command 
```commandline
$ python src/main.py [Fractal File] [Palette Name]
```
with [Fractal File] being the name of a fractal configuration file found in the data directory, and 
[Palette Name] being one of the color palettes the program is capable of producing.

Palette options are:
* sunrise
* thunderstorm

When no arguments are given, the program will create a default fractal.

```
$ python src/main.py
[100% =================================]
Done in 2.754 seconds!
Wrote picture default.png
Close the image window to exit the program
Creating Sunset palette
Rendering default fractal
```

When a valid fractal name is given, the program will open a window to render the image, and then save the image as a png.
The pngs follow the naming convention of fractal name + .png. Existing pngs will be overwritten if the same command is run again.

When run with one argument, the name of a fractal configuration file should be given. A default palette will be used.

```
$ python src/main.py data/spiral0.frac
[100% =================================]
Done in 4.507 seconds!
Wrote picture spiral0.png
Close the image window to exit the program
Creating Sunset palette
Rendering spiral0 fractal
```

When run with two arguments, the first will be the name of the fractal configuration file, and the second will be the name of a palette.
```
$ python src/main.py data/monkey-knife-fight.frac thunderstorm
[100% =================================]
Done in 2.503 seconds!
Wrote picture monkey-knife-fight.png
Close the image window to exit the program
Creating Thunderstorm Palette
Rendering monkey-knife-fight fractal
```

If a missing or inaccessible fractal configuration file is given, the program will exit with the error raised by open().
If an invalid palette name is given, the program will exit with NotImplementedError.