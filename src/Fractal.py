
class Fractal:

    def __init__(self, info):
        self.type = info["type"]
        self.centerX = info["centerx"]
        self.centerY = info["centery"]
        self.axislength = info["axislength"]
        self.pixels = info["pixels"]
        self.iterations = info["iterations"]
        self.minX = info["min"]["x"]
        self.minY = info["min"]["y"]
        self.pixelSize = info["pixelsize"]
        self.name = info["imagename"]
    def count(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")


class Mandelbrot(Fractal):
    def __init__(self, info):
        super().__init__(info)

    def count(self, c, end):
        """
        Return the iteration count for a point on the complex plane `c`
        to guess whether it is in the Mandelbrot set (bounded by `end`)
        """
        z = complex(0, 0)  # z0
        for i in range(end):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2.0:
                return i
        return end

    def iterations(self):
        return self.iterations


class Phoenix(Fractal):
    def __init__(self, info):
        super().__init__(info)
        self.pReal = info["preal"]
        self.pImag = info["pimag"]
        self.cReal = info["creal"]
        self.cImag = info["cimag"]
    def count(self, z, end):
        """
        Return the iteration count for a point on the complex plane `c`
        to guess whether it is in the Phoenix set (bounded by `end`)
        """

        # Julia Constant
        c = complex(self.cReal, self.cImag)

        # Phoenix Constant
        p = complex(self.pReal, self.pImag)

        # The first thing we do to the complex number Z is reflect its components,
        # so the imaginary part becomes the real part, and vice versa.
        # If we don't do this, the image comes out SIDEWAYS!!!
        z = complex(z.imag, z.real)

        # zPrevious is the PREVIOUS Z value, except the 1st time through the
        # function, when it starts out as Complex Zero (which is actually the
        # same thing as REAL Zero 0)  MATH IS BEAUTIFUL!
        zPrev = 0 + 0j

        for i in range(end):
            zSave = z
            z = z * z + c + (p * zPrev)
            if abs(z) > 2:
                return i
            zPrev = zSave  # Set the prevZ value for the next iteration
        return end

    def iterations(self):
        return self.iterations

