import os
import enum

visited = []
queue = []

def get_total_paths(matrix, start, end):
    paths = []
    traverse_paths(adjacency_matrix, "start", "end", paths)
    return len(paths)

def traverse_paths(matrix, source, dest, paths):
    visited.append(source)
    queue.append(source)

    if source == dest:
        paths.append(queue.copy())
    else:
        for neighbour in matrix[source]:
            if neighbour.isupper() or\
                (neighbour.islower() and neighbour not in visited):
                # Only allow a visit to the second virtual cave if the first one has already been visited and no other second caves have
                if '2' not in neighbour or ('2' not in ''.join(visited) and neighbour[:-1] in visited):
                    traverse_paths(matrix, neighbour, dest, paths)
    queue.pop()
    visited.remove(source)


if __name__ == "__main__":
    adjacency_matrix = {}
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        for line in f:
            path_list = []
            begin, end = line.strip().split('-')
            path_list.append((begin, end))
            # Create second virtual small caves
            if begin.islower() and begin not in ['start', 'end']:
                path_list.append((begin + '2', end))
            if end.islower() and end not in ['start', 'end']:
                path_list.append((begin, end + '2'))
            if begin.islower() and end.islower() and begin not in ['start', 'end'] and end not in ['start', 'end']:
                path_list.append((begin+'2', end+'2'))
            
            for source, dest in path_list:
                if source not in adjacency_matrix.keys():
                    adjacency_matrix[source] = []
                adjacency_matrix[source].append(dest)
                if dest not in adjacency_matrix.keys():
                    adjacency_matrix[dest] = []
                adjacency_matrix[dest].append(source)

    print(get_total_paths(adjacency_matrix, 'start', 'end'))