# Author: Owolabi
# Date: 11/04/25
# Purpose: Simulates the motion of the Sun and first four planets of the solar system.

from cs1lib import *
from body import Body
from system import System

# Window setup
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

# Simulation constants
PIXELS_PER_METER = 2.5e-9
TIMESTEP = 24 * 3600

# Define bodies: mass (kg), x (m), y (m), vx (m/s), vy (m/s), pixel radius, color (r,g,b)
# Source: approximate NASA data for circular orbits

sun = Body(1.98892e30, 0, 0, 0, 0, 12, 1, 1, 0)

mercury = Body(3.3e23, 5.79e10, 0, 0, 47890, 4, 0.6, 0.6, 0.6)
venus   = Body(4.87e24, 1.082e11, 0, 0, 35020, 6, 1, 0.5, 0)
earth   = Body(5.97e24, 1.496e11, 0, 0, 29783, 6, 0, 0, 1)
mars    = Body(6.42e23, 2.279e11, 0, 0, 24077, 5, 1, 0, 0)

solar_system = System([sun, mercury, venus, earth, mars])

def draw_frame():
    clear()
    set_clear_color(0, 0, 0)  # black background
    solar_system.update(TIMESTEP)
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

start_graphics(draw_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=30)
