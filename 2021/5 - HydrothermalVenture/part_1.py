"""
--- Day 5: Hydrothermal Venture ---

You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
"""
import os
from collections import Counter

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get_all_points(self, include_diagonal=False):
        """Every individual point across the line as long as line is straight"""
        # Vertical line
        if self.x1 == self.x2:
            direction = 1 if self.y1 < self.y2 else -1
            return [(self.x1, y) for y in range(self.y1, self.y2+direction, direction)]
        # Horizontal line
        elif self.y1 == self.y2:
            direction = 1 if self.x1 < self.x2 else -1
            return [(x, self.y1) for x in range(self.x1, self.x2+direction, direction)]
        # Diagonal line
        elif include_diagonal:
            x_direction = 1 if self.x1 < self.x2 else -1
            y_direction = 1 if self.y1 < self.y2 else -1
            points = []
            y_increase = 0
            for x in range(self.x1, self.x2+x_direction, x_direction):
                points.append((x, self.y1 + y_increase))
                y_increase += y_direction
            return points
        else:
            return []


def get_overlaps(input_file, include_diagonal):
    lines = []
    with open(input_file) as f:
        # Initialise lines
        for line in f:
            split_coords = [coord.split(",") for coord in line.strip().split(" -> ")]
            x1, y1 = split_coords[0]
            x2, y2 = split_coords[1]
            lines.append(Line(int(x1), int(y1) , int(x2), int(y2)))

    points = []
    for line in lines:
        for point in line.get_all_points(include_diagonal):
            points.append(point)
    
    point_counts = Counter(points)

    return sum(1 for total in point_counts.values() if total > 1)

if __name__ == "__main__":
    print(get_overlaps(os.path.dirname(__file__) + "/input.txt", include_diagonal=False))
