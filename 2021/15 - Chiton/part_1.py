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
    
    print(dijkstra(grid, (len(grid) -1, len(grid[0]) -1)))
    