import os
import re
from math import inf

class Target:
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.max_height = -inf

    def in_target(self, position):
        x, y = position
        return x in range(self.min_x, self.max_x + 1) and y in range(self.min_y, self.max_y + 1)

    def process_step(self, velocity, position):
        x, y = position
        vel_x, vel_y = velocity

        x += vel_x
        y += vel_y
        try:
            vel_x -= vel_x/abs(vel_x)
        except ZeroDivisionError:
            vel_x = 0
        vel_y -= 1

        return ((vel_x, vel_y), (x, y))

    def fire_hit(self, velocity, position=(0,0)):
        max_height = -inf
        last_pos = None
        while position[0] <= self.max_x and position[1] >= self.min_y:
            if position[1] > max_height:
                max_height = position[1]
            last_pos = position
            velocity, position = self.process_step(velocity, position)
            if self.in_target(position):
                self.max_height = max_height
                return "HIT"
        if position[0] > self.max_x:
            return "TOO MUCH X"
        elif position[1] < self.min_x:
            return "NOT ENOUGH X"
    

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        coords = [x.split("..") for x in re.findall(r"[-\d]+..[-\d]+", f.read())]
        min_x, max_x = [int(x) for x in coords[0]]
        min_y, max_y = [int(y) for y in coords[1]]
        target = Target(min_x, max_x, min_y, max_y)

        vel_x, vel_y = 0, 0
        result = target.fire_hit((vel_x, vel_y))

        total_hits = 0
        # THIS IS TERRIBLE
        for vel_x in range(300):
            for vel_y in range(-200, 200):
                result = target.fire_hit((vel_x, vel_y))
                if result == "HIT":
                    total_hits += 1
        print(total_hits)
