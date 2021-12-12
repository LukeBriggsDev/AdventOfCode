import os
import enum

visited = []
queue = []

def get_total_paths(matrix, start, end):
    total_paths = [0]
    traverse_paths(adjacency_matrix, "start", "end", total_paths)
    return total_paths[0]

def traverse_paths(matrix, source, dest, total_paths):
    visited.append(source)
    queue.append(source)

    if source == dest:
        total_paths[0] += 1
    else:
        for neighbour in matrix[source]:
            if neighbour.isupper() or\
                (neighbour.islower() and neighbour not in visited):
                traverse_paths(matrix, neighbour, dest, total_paths)

    queue.pop()
    visited.remove(source)


if __name__ == "__main__":
    adjacency_matrix = {}
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        for line in f:
            source, dest = line.strip().split('-')
            if source not in adjacency_matrix.keys():
                adjacency_matrix[source] = []
            adjacency_matrix[source].append(dest)
            if dest not in adjacency_matrix.keys():
                adjacency_matrix[dest] = []
            adjacency_matrix[dest].append(source)
    print(get_total_paths(adjacency_matrix, 'start', 'end'))
    