import os
import heapq

def valid_pos(grid, new_pos):
    return new_pos[0] >= 0 and new_pos[0] < len(grid) \
            and new_pos[1] >= 0 and new_pos[1] < len(grid[new_pos[0]])

visited = []
queue = []


def dijkstra(grid, target, start=(0,0), value=0):
    queue = [(value, start)]
    min_value = {start: value}
    visited = {start}

    while queue:
        value, (x, y) = heapq.heappop(queue)
        if (x, y) == target: return value

        for neighb in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
            if (not valid_pos(grid, neighb)) or neighb in visited: continue
            visited.add(neighb)
            new_value = value + grid[neighb[0]][neighb[1]]
            if new_value < min_value.get(neighb, 999999):
                min_value[neighb] = new_value
                heapq.heappush(queue, (new_value, neighb))
    

if __name__ == "__main__":
    grid =  []
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        for line in f:
            grid.append([int(x) for x in line.strip()])
    
    tiles = [[[] for __ in range(5)] for _ in range(5)]
    tiles[0][0] = grid
    for i in range(1, 5):
        new_grid = []
        for row in tiles[0][i-1]:
            new_row = [x + 1 if x + 1 < 10 else (x + 1) % 9 for x in row]
            new_grid.append(new_row)
        tiles[0][i] = new_grid

    for j in range(1, 5):
        new_tile_row = []
        for tile in tiles[j-1]:
            new_tile = []
            for row in tile:
                new_row = [x + 1 if x + 1 < 10 else (x + 1) % 9 for x in row]
                new_tile.append(new_row)
            new_tile_row.append(new_tile)
        tiles[j] = new_tile_row
    
    new_grid = []
    for tile_row in tiles:
        for i in range(len(grid)):
            new_row = []
            for tile in tile_row:
                for x in tile[i]:
                    new_row.append(x)
            new_grid.append(new_row)
    grid = new_grid
    print(dijkstra(grid, (len(grid) -1, len(grid[0]) -1)))  