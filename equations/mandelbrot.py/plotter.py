from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, MAX_ITER
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Image size (pixels)
WIDTH = 600
HEIGHT = 400

# Plotter window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

palette = []

im = Image.new('RGB', (WIDTH, HEIGHT), (0,0,0))
draw = ImageDraw.Draw(im)

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # Convert pixel coordinate to complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # Compute the number of iterations
        m = mandelbrot(c)
        # The colour depends on the number of iterations
        colour = 255 - int(m * 255 / MAX_ITER)
        # Plot the point
        draw.point([x,y], (colour, colour, colour))

im.show()
#im.save('output.png', 'PNG')
