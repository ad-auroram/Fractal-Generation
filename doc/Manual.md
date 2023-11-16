# Fractal Visualizer User Manual



To run the program, run the command 
```commandline
$ python src/main.py [Fractal Name]
```
with [Fractal Name] being one of the fractals the program is capable of producing. To see the full list,
run the command without a fractal name.

```
$ python src/main.py
Please provide the name of a fractal as an argument
    phoenix
    peacock
    monkey-knife-fight
    shrimp-cocktail
    elephants
    leaf
    mandelbrot
    mandelbrot-zoomed
    seahorse
    spiral0
    spiral1
    starfish
```

When a valid fractal name is given, the program will open a window to render the image, and then save the image as a png.
The pngs follow the naming convention of fractal name + .png. Existing pngs will be overwritten if the same command is run again.


If the program is given an invalid name, it will return an error and list the valid fractal names.
```commandline
$ python src/main.py mustache
ERROR: mustache is not a valid fractal
Please choose one of the following:
    phoenix
    peacock
    monkey-knife-fight
    shrimp-cocktail
    elephants
    leaf
    mandelbrot
    mandelbrot-zoomed
    seahorse
    spiral0
    spiral1
    starfish

```


The program is case-sensitive. Only lower case arguments are accepted. Capitalized fractal names will return an error,
along with a list of valid fractal names.
```commandline
$ python src/main.py Mandelbrot
ERROR: Mandelbrot is not a valid fractal
Please choose one of the following:
    phoenix
    peacock
    monkey-knife-fight
    shrimp-cocktail
    elephants
    leaf
    mandelbrot
    mandelbrot-zoomed
    seahorse
    spiral0
    spiral1
    starfish

```

Extra arguments given are ignored.
```commandline
$ python src/main.py mandelbrot extra arguments
Rendering mandelbrot fractal
[100% =================================]
Done in 3.152 seconds!
Saved image to file mandelbrot.png
Close the image window to exit the program

```