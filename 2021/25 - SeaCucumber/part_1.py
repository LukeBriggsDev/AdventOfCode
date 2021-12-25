import os
from copy import deepcopy

class Cucumber:
    def __init__(self, direction, x, y, icon):
        self.direction = direction
        self.x = x
        self.y = y
        self.can_move = False
        self.icon = icon

    def check_move(self, grid):
        x, y = self.get_next_location(grid)
        if grid[y][x] == ".":
            self.can_move = True

    def move(self, grid):
        x, y = self.get_next_location(grid)
        grid[self.y][self.x] = "."
        self.x = x
        self.y = y
        grid[self.y][self.x] = self.icon
        self.can_move = False

    def get_next_location(self, grid):
        x = (self.x + self.direction[0]) % len(grid[0])
        y = (self.y + self.direction[1]) % len(grid)
        return (x, y)


with open(os.path.dirname(__file__) + "/input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]

cucumbers = []

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != ".":
            if grid[row][col] == "v":
                direction = (0, 1)
            else:
                direction = (1, 0)
            cucumbers.append(Cucumber(direction, col, row, grid[row][col]))

counter = 0
grid_copy = ""

while grid != grid_copy:
    grid_copy = deepcopy(grid)
    counter += 1
    # Move right facing
    for cucumber in cucumbers:
        if cucumber.icon == '>':
            cucumber.check_move(grid)
    for cucumber in cucumbers:
        if cucumber.can_move and cucumber.icon == '>':
            cucumber.move(grid)

    # Move down facing
    for cucumber in cucumbers:
        if cucumber.icon == 'v':
            cucumber.check_move(grid)
    for cucumber in cucumbers:
        if cucumber.can_move and cucumber.icon == 'v':
            cucumber.move(grid)

print(counter)

