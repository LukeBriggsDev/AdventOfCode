import os
from copy import deepcopy
    

if __name__ == "__main__":
    with open(os.path.dirname(__file__)+"/input.txt") as f:
        enhancement = f.readline()
        f.readline()
        grid = []
        for line in f:
            grid.append(line.strip())

    lit = set()
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), 0, 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '#':
                lit.add((row, col))
                min_x = min(min_x, row)
                min_y = min(min_y, col)
                max_x = max(max_x, row)
                max_y = max(max_y, col)

    space = '.'
    iterations = 50
    for i in range(iterations):
        min_x -= 1
        min_y -= 1
        max_x += 1
        max_y += 1

        new_lit = set(lit)
        for x in range(min_x, max_x +1):
            for y in range(min_y, max_y + 1):
                idx = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        is_out_of_bounds = not (min_x < x + dx < max_x) or not (min_y < y + dy < max_y)
                        idx <<= 1
                        idx = idx | ((x + dx, y + dy) in lit or (is_out_of_bounds and space == '#'))
                if enhancement[idx] == '#':
                    new_lit.add((x, y))
                else:
                    new_lit.discard((x, y))
        space = enhancement[-1 if space == '#' else 0]
        lit = new_lit

    print(len(lit))
