import os

class Octopus:
    grid = []
    def __init__(self, energy_level, row, col):
        self.energy_level = energy_level
        self.flashed = False
        self.row = row
        self.col = col

    def increase_level(self):
        if not self.flashed:
            if self.row == 9 and self.col == 1:
                temp = 1 + 1
            self.energy_level += 1
            if self.energy_level > 9:
                self.flashed = True
                self.increase_neighbours()

    def reset(self):
        self.energy_level = 0
        self.flashed = False

    def increase_neighbours(self):
        vectors = [(1,0), (0,1), (1, 1), (-1, 0), (0, -1), (-1,-1), (1, -1), (-1, 1)]

        for vector in vectors:
            if self.row + vector[0] >=0 and self.col + vector[1] >= 0 and self.row + vector[0] < len(self.grid) and self.col + vector[1] < len(self.grid[self.row]):
                neighbour = self.grid[self.row + vector[0]][self.col + vector[1]]
                neighbour.increase_level()

def get_flashes(input_file, days):
    octopi = []
    flash_counter = 0
    with open(input_file) as f:
        row_count = -1
        for line in f:
            row_count += 1
            row = []
            col_count = -1
            for num in line.strip():
                col_count += 1 
                row.append(Octopus(int(num), row_count, col_count))
            octopi.append(row)

    Octopus.grid = octopi
    for i in range(days):
        # Each day
        for row in range(len(octopi)):
            for col in range(len(octopi[row])):
                octopi[row][col].increase_level()

        for row in range(len(octopi)):
            for col in range(len(octopi[row])):
                if octopi[row][col].flashed:
                    flash_counter += 1
                    octopi[row][col].reset()

    return flash_counter

if __name__ == "__main__":
    print(get_flashes(os.path.dirname(__file__)+ "/input.txt", 100))