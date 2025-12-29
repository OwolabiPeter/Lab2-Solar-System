# sirius_ab.py
# Extra Credit: Binary star system simulation (Sirius A and Sirius B)

from cs1lib import *
from body import Body
from system import System

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
PIXELS_PER_METER = 2e-9
TIMESTEP = 24 * 3600

# Sirius A and B data (approximate)
# Sirius A mass: 2.063e30 kg, Sirius B mass: 1.018e30 kg
# Distance: ~2e11 meters (roughly 1.3 AU)
# Orbital velocities chosen for near circular motion

sirius_a = Body(2.063e30, -1.0e11, 0, 0, -25000, 10, 1, 1, 0.8)
sirius_b = Body(1.018e30, 1.0e11, 0, 0, 50000, 8, 0.6, 0.6, 1.0)

binary_system = System([sirius_a, sirius_b])

def draw_frame():
    clear()
    set_clear_color(0, 0, 0)
    binary_system.update(TIMESTEP)
    binary_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

start_graphics(draw_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=30)
