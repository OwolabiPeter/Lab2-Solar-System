# Author: Owolabi
# Date: 11/04/25
# Purpose: Defines the Body class for the solar system simulation.

from cs1lib import *
class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        # Physical properties
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        # Visual properties
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestep):
        # Update position using velocity
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    def update_velocity(self, ax, ay, timestep):
        # Update velocity using acceleration
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    def draw(self, cx, cy, pixels_per_meter):
        # Convert meters to pixels
        sx = cx + self.x * pixels_per_meter
        sy = cy + self.y * pixels_per_meter
        disable_stroke()
        set_fill_color(self.r, self.g, self.b)
        draw_circle(sx, sy, self.pixel_radius)
