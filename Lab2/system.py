# Author: Owolabi
# Date: 11/04/25
# Purpose: Defines the System class for managing multiple Body objects and computing gravity.

from math import sqrt

G = 6.67384e-11  # Universal gravitational constant

class System:
    def __init__(self, body_list):
        self.body_list = body_list

    def compute_acceleration(self, n):
        # Compute total acceleration on body n due to all other bodies
        ax_total = 0.0
        ay_total = 0.0
        body_n = self.body_list[n]

        for j in range(len(self.body_list)):
            if j != n:
                body_j = self.body_list[j]

                dx = body_j.x - body_n.x
                dy = body_j.y - body_n.y
                r2 = dx * dx + dy * dy

                # Avoid division by zero
                if r2 != 0:
                    r = sqrt(r2)
                    a = G * body_j.mass / r2
                    ax_total = ax_total + a * (dx / r)
                    ay_total = ay_total + a * (dy / r)

        return ax_total, ay_total

    def update(self, timestep):
        # Compute all accelerations first
        ax_list = []
        ay_list = []

        i = 0
        while i < len(self.body_list):
            (ax, ay) = self.compute_acceleration(i)
            ax_list.append(ax)
            ay_list.append(ay)
            i = i + 1

        # Then update velocities and positions
        i = 0
        while i < len(self.body_list):
            body = self.body_list[i]
            body.update_velocity(ax_list[i], ay_list[i], timestep)
            body.update_position(timestep)
            i = i + 1

    def draw(self, cx, cy, pixels_per_meter):
        # Assume body_list[0] is the Sun
        sun = self.body_list[0]

        for body in self.body_list:
            # Shift everything so the Sun is at the center
            shifted_x = body.x - sun.x
            shifted_y = body.y - sun.y

            body.draw_shifted(cx, cy, pixels_per_meter, shifted_x, shifted_y)
            body.draw_trail_shifted(cx, cy, pixels_per_meter, sun)