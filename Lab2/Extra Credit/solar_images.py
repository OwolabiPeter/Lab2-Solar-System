# solar_images.py
from cs1lib import *
from Assignments.Labs.Lab2.system import System
from body_images import BodyImage

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
pixels_per_meter = 1.5e-9
TIMESTEP = 24 * 3600

sun_color     = (1.0, 0.8, 0.0)
mercury_color = (0.7, 0.7, 0.7)
venus_color   = (0.9, 0.8, 0.6)
earth_color   = (0.2, 0.6, 1.0)
mars_color    = (0.8, 0.3, 0.2)


sun = BodyImage(1.98892e30, 0, 0, 0, 0, "Sun.png", 40, sun_color)

mercury = BodyImage(3.3e23, 5.79e10, 0, 0, 47890, "FinalMercury .tiff", 10, mercury_color)
venus = BodyImage(4.87e24, 1.082e11, 0, 0, 35020, "venus.png", 16, venus_color)
earth = BodyImage(5.97e24, 1.496e11, 0, 0, 29783, "Earth.png", 14, earth_color)
mars = BodyImage(6.42e23, 2.279e11, 0, 0, 24077, "mars.jpeg", 12, mars_color)

solar_system = System([sun, mercury, venus, earth, mars])

def key_press(key):
    global pixels_per_meter

    if key == "+":
        pixels_per_meter *= 1.1   # zoom in
    elif key == "-":
        pixels_per_meter /= 1.1   # zoom out

def draw_frame():
    clear()
    set_clear_color(0, 0, 0)
    solar_system.update(TIMESTEP)
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, pixels_per_meter)

start_graphics(draw_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=30, key_press=key_press)

