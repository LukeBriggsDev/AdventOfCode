"""--- Day 9: Smoke Basin ---

--- Part Two ---

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.
"""

import os
import math

def get_basin(heightmap, row, col, pos_list):
    if row >= len(heightmap) or col >= len(heightmap[row]) or row < 0 or col < 0:
        return

    if heightmap[row][col] == 9:
        return

    pos_list.append((row, col))
    if (row, col + 1) not in pos_list:
        get_basin(heightmap, row, col + 1, pos_list)
    if (row, col - 1) not in pos_list:
        get_basin(heightmap, row, col - 1, pos_list)
    if (row - 1, col) not in pos_list:
        get_basin(heightmap, row - 1, col, pos_list)
    if (row + 1, col) not in pos_list:
        get_basin(heightmap, row + 1, col, pos_list)

def find_basins(input_file):
    heightmap = []
    with open(input_file) as f:
        for line in f:
            heightmap.append([int(x) for x in line.strip()])
    

    low_points = []

    for row_index in range(len(heightmap)):
        for col_index in range(len(heightmap[row_index])):
            if (col_index == 0 or heightmap[row_index][col_index-1] > heightmap[row_index][col_index]) and \
               (col_index == len(heightmap[row_index]) -1 or heightmap[row_index][col_index+1] > heightmap[row_index][col_index]) and \
               (row_index == len(heightmap)-1 or heightmap[row_index+1][col_index] > heightmap[row_index][col_index]) and \
               (row_index == 0 or heightmap[row_index-1][col_index] > heightmap[row_index][col_index]):
                low_points.append((row_index, col_index))


    basins = []
    for point in low_points:
        basin = []
        get_basin(heightmap, point[0], point[1], basin)
        basins.append(basin)

    return math.prod(sorted([len(basin) for basin in basins], reverse=True)[:3])

if __name__ == "__main__":
    while True:
        print(find_basins(os.path.dirname(__file__) + "/input.txt"))