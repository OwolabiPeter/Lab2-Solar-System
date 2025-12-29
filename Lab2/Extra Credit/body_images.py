# body_images.py
# Extra Credit: Draw bodies with images instead of circles

from cs1lib import *


class BodyImage:
    def __init__(self, mass, x, y, vx, vy, image_filename, radius, color):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = load_image(image_filename)
        self.radius = radius  # approximate half-size in pixels
        self.color = color
        self.trail = []

    def update_position(self, timestep):
        self.trail.append((self.x, self.y))

        if len(self.trail) > 50:
            self.trail.pop(0)

        self.x += self.vx * timestep
        self.y += self.vy * timestep

    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    def draw(self, cx, cy, pixels_per_meter):
        sx = cx + self.x * pixels_per_meter - self.radius
        sy = cy + self.y * pixels_per_meter - self.radius
        draw_image(self.image, sx, sy)

    def draw_trail_shifted(self, cx, cy, ppm, sun):
        r, g, b = self.color
        set_stroke_color(r, g, b)
        set_stroke_width(1)

        i = 1
        while i < len(self.trail):
            x1, y1 = self.trail[i - 1]
            x2, y2 = self.trail[i]

            sx1 = int(cx + (x1 - sun.x) * ppm)
            sy1 = int(cy + (y1 - sun.y) * ppm)
            sx2 = int(cx + (x2 - sun.x) * ppm)
            sy2 = int(cy + (y2 - sun.y) * ppm)

            draw_line(sx1, sy1, sx2, sy2)
            i += 1

    def draw_shifted(self, cx, cy, ppm, x, y):
        sx = int(cx + x * ppm - self.radius)
        sy = int(cy + y * ppm - self.radius)
        draw_image(self.image, sx, sy)
