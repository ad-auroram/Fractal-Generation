# CS 1440 Assignment 4.0: Refactoring - Understanding Fractals

This program is intentionally difficult to understand for two reasons:

0.  The code is messy
1.  Fractals are an esoteric subject

Your goal in this sprint is to merely clean up the code.  You do not need to grasp the big picture to know which lines of code are poorly written.  Nor do you actually need to understand precisely how fractals work to refactor this code.  You can clean up *any* program through trial-and-error if you work slowly and carefully:

0.  Make small changes
1.  Focused on only one part of the program at a time
2.  Re-run the program often
3.  Commit code to Git frequently
    *   If your test didn't work, revert the changes instead


## The Interactive Fractal Demo

For a better grasp on fractals, delve into the interactive Mandelbrot program [demo/interactive.py](./demo/interactive.py).   While it isn't much prettier than the starter code, it will help you grasp how the algorithm works.

*   The demo colors a block of pixels simultaneously, acting as a low-resolution fractal plotter.
*   Left-clicking on the image invokes a square painting using the same algorithm as in [src/mbrot_fractal.py](./src/mbrot_fractal.py), but it also prints the Z parameter values at each iteration to the console, besides displaying the iteration count on the image.
*   Right-clicking unveils the entire image.

By examining the demo's source code, running it through a debugger, and reviewing its output, you'll gain insights into how your program generates its images.

**Note:** `demo/interactive.py` is solely for your exploration and learning; it's *not* part of the assignment, so avoid modifying, testing, or documenting it.



## Understanding The Fractal Algorithms

*   Our program uses the [Escape-Time](https://en.wikipedia.org/wiki/Plotting_algorithms_for_the_Mandelbrot_set) plotting algorithm
*   The points *inside* the cardioid are the Mandelbrot set
    *   The escape-time algorithm gets stuck in an infinite loop for points within the Mandelbrot set
    *   Capping the number of iterations prevents the program from hanging
*   An image of the Mandelbrot set produced by this program is a visualization of the complex plane, formed by relating complex numbers to Cartesian coordinates:
    *   The coordinates of pixels in the `PhotoImage` object are pairs of X, Y coordinates.  The origin of the `PhotoImage` object `(0, 0)` is the upper-left corner of the image window.
    *   Complex numbers are ordered pairs of Real and Imaginary components.
    *   The `X` axis of the Mandelbrot set represents the *real* number line.
    *   The `Y` axis of the Mandelbrot set represents the *imaginary* number line.
    *   The function that draws the image (`paint()` in `src/mbrot_fractal.py` and `makePictureOfFractal()` in `src/phoenix_fractal.py`) converts the `(X, Y)` coordinates of the `PhotoImage` into a complex number.  This complex number is called `C` in the Mandelbrot algorithm and `Z` in the Phoenix algorithm.
    *   The image drawing function chooses the color to paint a pixel by counting the number of times the fractal function can be *iterated* before its output exceeds a threshold.
    *   *Iteration* in this context means to use the output of a function as its input value again and again to find out if the function tends toward infinity.
*   The Mandelbrot function is fascinating because *sometimes* iteration makes it go off to infinity and *sometimes* it does not.
    *   The points *inside* the cardioid are the points *within* the Mandelbrot set.  These are the coordinates on the imaginary plane corresponding to `Z` values that stay small after repeated iterations of the Mandelbrot function.
    *   Points *outside* of the cardioid shoot off to infinity under iteration.
    *   Points at the boundary are where all of the pretty and interesting pictures occur.


### More Fractal Resources

You can find ideas for new fractal configurations by exploring the Mandelbrot and Phoenix sets online.  You can also compare your program's output with other Mandelbrot and Phoenix set visualizers to make sure that you haven't made any serious mistakes.  You will find that some fractal viewers draw Phoenix fractals that are rotated 90° relative to ours.  This is a result of our formula "reflecting" the `Z` parameter.

*   The difference between the [Mandelbrot and Julia sets](http://usefuljs.net/fractals/docs/julia_mandelbrot.html)
*   [Interactive Browser Fractal Viewer](http://usefuljs.net/fractals/)
*   [Phoenix Fractal](http://paulbourke.net/fractals/phoenix_julia/)
*   [XaoS](https://xaos-project.github.io/) - a *smooth* desktop fractal zoomer
*   [Fractint](http://eyecandyarchive.com/Fractint/) - the classic *fast* old-school fractal zoomer
*   YouTube videos that I like:
    *   [D!NG - The Mandelbrot Set](https://youtu.be/MwjsO6aniig?t=70)
    *   [Veritasium - this equation will change how you see the world](https://youtu.be/ovJcsL7vyrk?t=410)
    *   [The Mandelbrot Set - Numberphile](https://www.youtube.com/watch?v=NGMRB4O922I)


#### Videos About Fractals

*   [Numberphile: The Mandelbrot Set](https://www.youtube.com/watch?v=NGMRB4O922I)
*   [Numberphile: What's so special about the Mandelbrot Set?](https://www.youtube.com/watch?v=FFftmWSzgmk)
*   [Veritasium: This equation will change how you see the world (the logistic map)](https://www.youtube.com/watch?v=ovJcsL7vyrk)


#### Online Fractal Zoomers

Most of these web sites define their images in `(minX, minY), (maxX, maxY)` coordinates, while our program uses the `(centerX, centerY) + axisLength` scheme.  It is helpful to write a small helper program which converts between the coordinate formats.

*   https://atopon.org/mandel/
*   https://sciencedemos.org.uk/mandelbrot.php (note: this program produces images that are upside down from those generated by our program)
*   http://bl.ocks.org/syntagmatic/3736720
*   http://usefuljs.net/fractals/
*   [jsFractalZoom](https://rockingship.github.io/jsFractalZoom/jsFractalZoom.html)
*   The [GNU XaoS](http://xaos-project.github.io/XaoSjs/) JavaScript engine for your browser


#### Desktop Fractal Zoomers

Fractal rendering software written to go *fast*.

*   [GNU XaoS](https://xaos-project.github.io): A free and open source fractal explorer for Linux, Windows and Mac
*   [Eyecandy](http://eyecandyarchive.com/): Turn your computer into an expensive lava lamp.  Contains links to other programs you can use to explore fractals and other interesting patterns of pixels.
*   [FractInt](https://fractint.org/): A classic MS-DOS program (which is *still* under development!) whose users have made interesting discoveries within the Mandelbrot set and other related fractals over the years
